'''
Copyright (c) <2012> Tarek Galal <tare2.galal@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this 
software and associated documentation files (the "Software"), to deal in the Software 
without restriction, including without limitation the rights to use, copy, modify, 
merge, publish, distribute, sublicense, and/or sell copies of the Software, and to 
permit persons to whom the Software is furnished to do so, subject to the following 
conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR 
A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF 
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE 
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
from Yowsup.connectionmanager import YowsupConnectionManager
import time, datetime, sys
import os.path
import pdb

if sys.version_info >= (3, 0):
	raw_input = input

class WhatsappCmdClient:

	bAuthFinished      = False
	bAuthSuccess       = False
	bSetProfileFile    = False
	bSetProfileSuccess = False
	bSetStatus         = False
	bDisconnected      = True
	sDisconnectReason  = ""
	lvMessage          = []
	
	def __init__(self, phoneNumber, keepAlive = False, sendReceipts = False):
		self.sendReceipts = sendReceipts
		self.phoneNumber = phoneNumber
		self.jid = "%s@s.whatsapp.net" % phoneNumber
		self.myjid=""
		
		self.sentCache = {}
		WhatsappCmdClient.lvMessage = []
		
		self.connectionManager = YowsupConnectionManager(False)
		self.connectionManager.setAutoPong(keepAlive)
		self.signalsInterface = self.connectionManager.getSignalsInterface()
		self.methodsInterface = self.connectionManager.getMethodsInterface()
		
		self.signalsInterface.registerListener("auth_success", self.onAuthSuccess)
		self.signalsInterface.registerListener("auth_fail", self.onAuthFailed)
		self.signalsInterface.registerListener("message_received", self.onMessageReceived)
		self.signalsInterface.registerListener("receipt_messageSent", self.onMessageSent)
		self.signalsInterface.registerListener("presence_updated", self.onPresenceUpdated)
		self.signalsInterface.registerListener("disconnected", self.onDisconnected)
		self.signalsInterface.registerListener("profile_setPictureSuccess",self.onPictureSuccess)
		self.signalsInterface.registerListener("profile_setPictureError",self.onPictureError)
		self.signalsInterface.registerListener("contact_gotProfilePicture",self.onProfilePicture),
		self.signalsInterface.registerListener("profile_setStatusSuccess",self.onStatusSuccess)
		
		#0: method, 1: parameter name in prompt, 2: position in prompt  
		#self.commandMappings = {"lastseen":    (lambda: self.methodsInterface.call("presence_request", (self.jid,)),"",6),
								#"available":   (lambda: self.methodsInterface.call("presence_sendAvailable"),"",1),
								#"unavailable": (lambda: self.methodsInterface.call("presence_sendUnavailable"),"",2),
								#"setprofile":  (lambda file: self.setProfile(file,),"filename",4),
								#"setstatus":   (lambda status: self.setStatus(status,),"status",5),
								#"getprofile":  (lambda: self.methodsInterface.call("contact_getProfilePicture", (self.jid,)),"",3),
								#"exit": 	   (self.done,"",7)
								 #}

		#self.done = False
		#self.signalsInterface.registerListener("receipt_messageDelivered", lambda jid, messageId: self.methodsInterface.call("delivered_ack", (jid, messageId)))
	
	def login(self, username, password):
		self.username = username
		self.myjid = "%s@s.whatsapp.net" % username
		self.methodsInterface.call("auth_login", (username, password))

	def onAuthSuccess(self, username):
		self.methodsInterface.call("ready")
		WhatsappCmdClient.bAuthFinished = True
		WhatsappCmdClient.bAuthSuccess  = True
		WhatsappCmdClient.bDisconnected = False

	def onAuthFailed(self, username, err):
		WhatsappCmdClient.bAuthFinished = True
		WhatsappCmdClient.bAuthSuccess  = False

	def setProfile(self,file):
		if os.path.isfile(file):
			self.methodsInterface.call("profile_setPicture", (file,))
			WhatsappCmdClient.bSetProfileFile = True
		else:
			WhatsappCmdClient.bSetProfileFile = False
			
	def onPictureSuccess(self, id):
		WhatsappCmdClient.bSetProfileSuccess = True

	def onPictureError(self, error):
		WhatsappCmdClient.bSetProfileSuccess = False

	def onMessageReceived(self, messageId, jid, messageContent, timestamp, wantsReceipt, pushName, isBroadcast):
		formattedDate = datetime.datetime.fromtimestamp(timestamp).strftime('%Y%m%d %H:%M.%S')
		WhatsappCmdClient.lvMessage.append((jid, formattedDate, messageContent, messageId))
		
		if wantsReceipt and self.sendReceipts:
			self.methodsInterface.call("message_ack", (jid, messageId))

	def onMessageSent(self, jid, messageId):
		pass

	def sendMessage (self, jid, message):
		msgId = self.methodsInterface.call("message_send", (jid, message))
		self.sentCache[msgId] = [int(time.time()), message]

	def setStatus(self, status):
		self.methodsInterface.call("profile_setStatus", (status,)),
		WhatsappCmdClient.bSetStatus = False

	def onStatusSuccess(self, jid, messageId):
		self.methodsInterface.call("message_ack", (jid, messageId))
		WhatsappCmdClient.bSetStatus = True

	def onDisconnected(self, reason):
		WhatsappCmdClient.bDisconnected = True
		WhatsappCmdClient.sDisconnectReason = reason




		
	def onProfilePicture(self, jid, pictureid, path):
		print("Got profile picture of %s: id: %s path:%s" % (jid, pictureid, path))

	def onPresenceUpdated(self, jid, lastSeen):
		formattedDate = datetime.datetime.fromtimestamp(long(time.time()) - lastSeen).strftime('%d-%m-%Y %H:%M')
		self.onMessageReceived(0, jid, "LAST SEEN RESULT: %s"%formattedDate, long(time.time()), False, None, False)
