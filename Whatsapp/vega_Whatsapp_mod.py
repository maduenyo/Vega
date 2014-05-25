#!/usr/bin/python
# coding: latin-1

# ---------------------------------------------------
# -                Whatsapp Set Pic                 -
# ---------------------------------------------------
def funWhatsappSetPic (cWhatsappCmdClient, sPicFile, sTab="     "):

	# Set variables -------------------------------------
	sNextTab = "     "
	bSuccess = True
	sComment = "OK"
	vPathLog  = vega_SetVariables_mod.funSetVariable('WAPP_LOG')

	# Set profile picture -------------------------------
	vega_Log_mod.funAppendToLog ( sTab + "Setting pic:\t", vEnd="", vLogFile=vPathLog )

	# Try up to 5 times ---------------------------------
	for lIteration in range(0,5):

		# Set status ----------------------------------------
		cWhatsappCmdClient.setProfile(sPicFile)
		time.sleep(1)

		# Check pic file ------------------------------------
		if cWhatsappCmdClient.bSetProfileFile == False:

			# Profile file NOK ----------------------------------
			bSuccess = False
			sComment = "NOK (Pic file not found)"
			vega_Log_mod.funAppendToLog ( sComment, vLogHeader=False, vLogFile=vPathLog )

			# Exit ----------------------------------------------
			return bSuccess, sComment

		# Check set pic -------------------------------------
		elif cWhatsappCmdClient.bSetProfileSuccess == False:

			# Set pic NOK ---------------------------------------
			bSuccess = False
			sComment = "."
			vega_Log_mod.funAppendToLog ( sComment, vLogHeader=False, vEnd="", vLogFile=vPathLog )
			time.sleep(5)

		else:

			# Log -----------------------------------------------
			sComment = "OK"
			vega_Log_mod.funAppendToLog ( sComment, vLogHeader=False, vLogFile=vPathLog )
			break


	# Check bSuccess -------------------------------------
	if bSuccess == False:

		# Set pic NOK ---------------------------------------
		bSuccess = False
		sComment = "Unable to set pic"
		vega_Log_mod.funAppendToLog ( "NOK (" + sComment + ")", vLogHeader=False, vLogFile=vPathLog )


	# Exit ----------------------------------------------
	return bSuccess, sComment


# ---------------------------------------------------
# -               Whatsapp Set Status               -
# ---------------------------------------------------
def funWhatsappSetStatus (cWhatsappCmdClient, sStatus, sTab="     "):

	# Set variables -------------------------------------
	sNextTab = "     "
	bSuccess = True
	sComment = "OK"
	sStatus  = "At your command"
	vPathLog  = vega_SetVariables_mod.funSetVariable('WAPP_LOG')

	# Set status ----------------------------------------
	vega_Log_mod.funAppendToLog ( sTab + "Setting status:\t", vEnd="", vLogFile=vPathLog )

	# Try up to 5 times ---------------------------------
	for lIteration in range(0,5):

		# Set status ----------------------------------------
		cWhatsappCmdClient.setStatus(sStatus)
		time.sleep(1)

		# Check status --------------------------------------
		if cWhatsappCmdClient.bSetStatus == False:

			# Set Status NOK ------------------------------------
			bSuccess = False
			sComment = "."
			vega_Log_mod.funAppendToLog ( sComment, vLogHeader=False, vEnd="", vLogFile=vPathLog )
			time.sleep(5)

		else:

			# Log -----------------------------------------------
			sComment = "OK"
			vega_Log_mod.funAppendToLog ( sComment, vLogHeader=False, vLogFile=vPathLog )
			break


	# Check bSuccess -------------------------------------
	if bSuccess == False:

		# Set Status NOK ------------------------------------
		sComment = "Unable to set status"
		vega_Log_mod.funAppendToLog ( "NOK (" + sComment + ")", vLogHeader=False, vLogFile=vPathLog )

	# Exit ----------------------------------------------
	return bSuccess, sComment


# ---------------------------------------------------
# -                 Whatsapp Login                  -
# ---------------------------------------------------
def funWhatsappLogin (cWhatsappCmdClient, sUserName, sPassword, sTab="     "):

	# Set variables -------------------------------------
	sNextTab = "     "
	bSuccess = True
	sComment = "OK"
	vPathLog  = vega_SetVariables_mod.funSetVariable('WAPP_LOG')

	# Login ---------------------------------------------
	vega_Log_mod.funAppendToLog ( sTab + "Authenticating:\t", vEnd="", vLogFile=vPathLog )
	cWhatsappCmdClient.login(sUserName, sPassword)
	time.sleep(1)

	# Check login ---------------------------------------
	if cWhatsappCmdClient.bAuthSuccess == False:

		# Login NOK -----------------------------------------
		bSuccess = False
		sComment = "NOK (Authentication failed)"
		vega_Log_mod.funAppendToLog ( sComment, vLogHeader=False, vLogFile=vPathLog )
		return bSuccess, sComment

	else:

		# Log -----------------------------------------------
		sComment = "OK"
		vega_Log_mod.funAppendToLog ( sComment, vLogHeader=False, vLogFile=vPathLog )

	# Exit ----------------------------------------------
	return bSuccess, sComment

# ---------------------------------------------------
# -              Connect To Whatsapp                -
# ---------------------------------------------------
def funConnectToWhatsapp (sTab=""):

	# Set variables -------------------------------------
	sNextTab  = "     "
	bSuccess  = True
	vPathLog  = vega_SetVariables_mod.funSetVariable('WAPP_LOG')
	sUserName = vega_SetVariables_mod.funSetVariable('WAPP_USERNAME')
	sPassword = vega_SetVariables_mod.funSetVariable('WAPP_PASSWORD')
	sPassword = base64.b64decode(bytes(sPassword.encode('utf-8')))
	sStatus   = vega_SetVariables_mod.funSetVariable('WAPP_STATUS')
	sPicFile  = vega_SetVariables_mod.funSetVariable('WAPP_PIC')
	cWhatsappCmdClient = Examples.CmdClient.WhatsappCmdClient(phoneNumber='', keepAlive = True, sendReceipts = True)

	# Log -----------------------------------------------
	vega_Log_mod.funAppendToLog ( sTab + "Connecting to Whatsapp server:", vLogFile=vPathLog )

	# ---------------------------------------------------
	# Login 
	# ---------------------------------------------------
	bSuccess, sComment = funWhatsappLogin (cWhatsappCmdClient, sUserName, sPassword, sNextTab)
	if bSuccess == False:

		# Login NOK -----------------------------------------
		return cWhatsappCmdClient, bSuccess, sComment

	# ---------------------------------------------------
	# Set status
	# ---------------------------------------------------
	bSuccess, sComment = funWhatsappSetStatus (cWhatsappCmdClient, sStatus, sNextTab)
	if bSuccess == False:

		# Set status NOK ------------------------------------
		return cWhatsappCmdClient, bSuccess, sComment

	# ---------------------------------------------------
	# Set Pic
	# ---------------------------------------------------
	bSuccess, sComment = funWhatsappSetPic (cWhatsappCmdClient, sPicFile, sNextTab)
	if bSuccess == False:

		# Set pic NOK ---------------------------------------
		return cWhatsappCmdClient, bSuccess, sComment

	# ---------------------------------------------------
	# Set presence
	# ---------------------------------------------------




	

	# Exit ----------------------------------------------
	# Ignore errors in set status / set pic
	bSuccess = True
	return cWhatsappCmdClient, bSuccess, sComment


# ---------------------------------------------------
# -            Reconnect To Whatsapp                -
# ---------------------------------------------------
def funReconnectToWhatsapp (sComment, sTab=""):

	# Set variables -------------------------------------
	sNextTab = "     "
	vPathLog = vega_SetVariables_mod.funSetVariable('WAPP_LOG')

	# Log -----------------------------------------------
	vega_Log_mod.funAppendToLog ( " ", vLogFile=vPathLog )
	vega_Log_mod.funAppendToLog ( sTab + "Disconnected from Whatsapp server:", vLogFile=vPathLog )
	vega_Log_mod.funAppendToLog ( sTab + sNextTab + "Reason:\t" + sComment, vLogFile=vPathLog )

	# Log -----------------------------------------------
	vega_Log_mod.funAppendToLog ( " ", vLogFile=vPathLog )
	vega_Log_mod.funAppendToLog ( sTab + "Retrying connection in 5 seconds", vEnd='', vLogFile=vPathLog )
	for vItem in range(0,4):
		vega_Log_mod.funAppendToLog ( ".", vEnd='', vLogHeader=False, vLogFile=vPathLog )
		time.sleep(1)
	vega_Log_mod.funAppendToLog ( ".", vLogHeader=False, vLogFile=vPathLog )

	# Log -----------------------------------------------
	vega_Log_mod.funAppendToLog ( " ", vLogFile=vPathLog )


	# Retry connection ----------------------------------
	time.sleep(5)
	cWhatsappCmdClient, bSuccess, sComment = funConnectToWhatsapp(sTab)
	if bSuccess == False:

		# Log -----------------------------------------------
		sComment = "Unable to re-connect"
		vega_Log_mod.funAppendToLog ( " ", vLogFile=vPathLog )
		vega_Log_mod.funAppendToLog ( sTab + "Disconnected from Whatsapp server:", vLogFile=vPathLog )
		vega_Log_mod.funAppendToLog ( sTab + sNextTab + "Reason:\t" + sComment, vLogFile=vPathLog )

		# Disconnected --------------------------------------
		return cWhatsappCmdClient, bSuccess, sComment

	# Log -----------------------------------------------
	vega_Log_mod.funAppendToLog ( " ", vLogFile=vPathLog )
	vega_Log_mod.funAppendToLog ( sTab + "Listening to incomming messages:", vLogFile=vPathLog )

	# Exit ----------------------------------------------
	vExit = False
	return cWhatsappCmdClient, bSuccess, sComment


# ---------------------------------------------------
# -     Whatsapp Set Variables Incoming Msg         -
# ---------------------------------------------------
def funWhatsappSetVariablesIncomingMsg (lvMessage):

	# Set variables -------------------------------------
	sJid         = lvMessage[0]
	sPhone       = sJid.split("@")[0]
	sRxTimestamp = lvMessage[1]
	sRxMessage   = lvMessage[2]
	# sRxMessage   = sRxMessage.decode('utf-8').encode('ascii','replace')
	sRxMessage   = sRxMessage.decode('utf-8').encode('latin-1')

	# Exit ----------------------------------------------
	return sJid, sPhone, sRxTimestamp, sRxMessage


# ---------------------------------------------------
# -        Get Party Name From Phone Number         -
# ---------------------------------------------------
def funGetPartyNameFromPhoneNumber (sPhone):

	# Set varaibles -------------------------------------
	lsCaller     = vega_SetVariables_mod.funSetVariable('WAPP_CALLER')
	
	# Check Phone number --------------------------------
	if sPhone in lsCaller:

		# Name found ----------------------------------------
		sPartyName = lsCaller[sPhone]

	else:

		# Name not found ------------------------------------
		sPartyName = sPhone

	# Exit ----------------------------------------------
	return sPartyName


# ---------------------------------------------------
# -            Check Whatsapp Message               -
# ---------------------------------------------------
def funCheckWhatsappMessage (cWhatsappCmdClient, lPrevCounter, sTab=""):

	# Set variables -------------------------------------
	sNextTab     = "     "
	bExitWhile   = False
        vPathLog     = vega_SetVariables_mod.funSetVariable('WAPP_LOG')
	lsCaller     = vega_SetVariables_mod.funSetVariable('WAPP_CALLER')
	lCurrCounter = len(cWhatsappCmdClient.lvMessage)

	# Check if new message ------------------------------
	if lCurrCounter > lPrevCounter:

		# Set variables -------------------------------------
		sJid, sPhone, sRxTimestamp, sRxMessage = funWhatsappSetVariablesIncomingMsg (cWhatsappCmdClient.lvMessage[lPrevCounter])
		sPartyName = funGetPartyNameFromPhoneNumber(sPhone)

		# Log -----------------------------------------------
		vega_Log_mod.funAppendToLog ( sTab + sNextTab + "RX (" + sPartyName + " - " + sRxTimestamp + "): " + sRxMessage, vLogFile=vPathLog )

		# Check if vega command -----------------------------
		if sRxMessage.upper().find("VEGA") >=0 and sPhone in lsCaller:

			# Interpret Command ---------------------------------
			bExitWhile, sTxMessage = vega_Whatsapp_CommandAnalysis_mod.funCommandAnalysis (cWhatsappCmdClient, lPrevCounter, sTab + sNextTab)

			# Set variables -------------------------------------
			cWhatsappCmdClient.sendMessage(sJid, sTxMessage)
			sTxTimestamp = vega_CommonFunctions_mod.funGetTimestamp()

			# Answering to message ------------------------------
			vega_Log_mod.funAppendToLog ( sTab + sNextTab + "TX (" + "Vega" + " - " + sTxTimestamp + "): " + sTxMessage, vLogFile=vPathLog )

		# Set variables -------------------------------------
		lPrevCounter = lPrevCounter + 1

	# Exit ---------------------------------------------
	return lPrevCounter, bExitWhile

# ---------------------------------------------------
# -                 Whatsapp Loop                   -
# ---------------------------------------------------
def funWhatsappLoop (cWhatsappCmdClient, sTab=""):

	# Set variables -------------------------------------
	sNextTab     = "     "
	lPrevCounter = 0
	lCurrCounter = 0
	lsCaller     = vega_SetVariables_mod.funSetVariable('WAPP_CALLER')
        vPathLog     = vega_SetVariables_mod.funSetVariable('WAPP_LOG')

	# Log -----------------------------------------------
	vega_Log_mod.funAppendToLog ( " ", vLogFile=vPathLog )
	vega_Log_mod.funAppendToLog ( sTab + "Listening to incomming messages:", vLogFile=vPathLog )

	# Loop for messages ---------------------------------
	while True:

		# Check if disconnected -----------------------------
		if cWhatsappCmdClient.bDisconnected == True:

			# Reset variables -----------------------------------
			lCurrCounter = 0
			lPrevCounter = 0
			sComment     = cWhatsappCmdClient.sDisconnectReason
			del cWhatsappCmdClient

			# Reconnect To Whatsapp -----------------------------
			cWhatsappCmdClient, bSuccess, sComment = funReconnectToWhatsapp (sComment, sTab)
			if bSuccess == False:

				# Exit ----------------------------------------------
				return sComment

		# Check if Message List not empty -------------------
		elif cWhatsappCmdClient.lvMessage <> []:

			# Check whatsapp message ------------------------------
			lPrevCounter, bExitWhile = funCheckWhatsappMessage (cWhatsappCmdClient, lPrevCounter, sTab)
			if bExitWhile == True:

				# Exit While ----------------------------------------
				break

		# Wait for incoming message -------------------------
		time.sleep(0.5)

		# DEBUG #############################################
		#if lCurrCounter == 3:
			#pdb.set_trace()
			#cWhatsappCmdClient.connectionManager.disconnect("DEBUG")
		# DEBUG #############################################

	# Disconnect ----------------------------------------
	sComment = "User request"
	cWhatsappCmdClient.connectionManager.disconnect(sComment)

	# Log -----------------------------------------------
	vega_Log_mod.funAppendToLog ( " ", vLogFile=vPathLog )
	vega_Log_mod.funAppendToLog ( sTab + "Disconnected from Whatsapp server:", vLogFile=vPathLog )
	vega_Log_mod.funAppendToLog ( sTab + sNextTab + "Reason:\t" + sComment, vLogFile=vPathLog )

	# Exit ----------------------------------------------
	return sComment


# ---------------------------------------------------
# -                     main                        -
# ---------------------------------------------------
def main():

	# Set variables -------------------------------------
	sTab         = ""
	sNextTab     = "     "
        vPathLog     = vega_SetVariables_mod.funSetVariable('WAPP_LOG')

	# Connect to Whatsapp -------------------------------
	cWhatsappCmdClient, bSuccess, sComment = funConnectToWhatsapp(sTab)
	if bSuccess == True:

		# Loop ----------------------------------------------
		sComment = funWhatsappLoop (cWhatsappCmdClient, sTab)

	else:
		# Unable to connect ---------------------------------
		cWhatsappCmdClient.connectionManager.disconnect(sComment)

		# Log -----------------------------------------------
		vega_Log_mod.funAppendToLog ( " ", vLogFile=vPathLog )
		vega_Log_mod.funAppendToLog ( "Disconnected from Whatsapp server:", vLogFile=vPathLog )
		vega_Log_mod.funAppendToLog ( sNextTab + "Reason:\t" + sComment, vLogFile=vPathLog )

		# Exit ----------------------------------------------
		return

	# Log ---------------------------------------
	vega_Log_mod.funAppendToLog ( " ", vLogFile=vPathLog )
	vega_Log_mod.funAppendToLog ( "Listening finished.", vLogFile=vPathLog )


# ---------------------------------------------------
# -                    T O P                        -
# ---------------------------------------------------
import datetime
import base64
import time
import sys
import pdb

import Examples.ListenerClient
import Examples.CmdClient
import vega_Log_mod
import vega_SetVariables_mod
import vega_CommonFunctions_mod
import vega_Whatsapp_CommandAnalysis_mod

