#!/usr/bin/python
# coding: latin-1

# ---------------------------------------------------
# -                Execute Command                  -
# ---------------------------------------------------
def funExecuteComand (lsDevice, sAction):

	# Set variables -------------------------------------
	bExit     = True
	lsCommand = []

	# Execute command device by device ------------------
	for sDevice in lsDevice:

		# Set variables -------------------------------------
		sCommand = ""

		# Check device --------------------------------------
		if int(sDevice) < 100:
			sCommand = "/usr/bin/curl -s -LN --globoff 'http://raspberry01.madnet.home:8083/ZWaveAPI/Run/devices[" + sDevice \
					+ "].instances[0].commandClasses[38].Set(" + sAction + ")'"

		elif sDevice in ["101"]:
			pass

		elif sDevice in ["201"]:
			#pdb.set_trace()
			if type(sAction) is list:
				# Execute action by action ---------------------------
				for sItem in sAction:
					sCommand = "/usr/bin/curl -s -LN --globoff 'http://roomba780.madnet.home/roomba.cgi?button=" + sItem + "'"
					lsCommand.append(sCommand)
					os.system(sCommand)
					time.sleep(11.5)

				# Exit -----------------------------------------------
				return lsCommand, bExit

			else:	
				sCommand = "/usr/bin/curl -s -LN --globoff 'http://roomba780.madnet.home/roomba.cgi?button=" + sAction + "'"

		# Check sCommand ------------------------------------
		if sCommand <> "":
			lsCommand.append(sCommand)
			os.system(sCommand)

	# Exit ----------------------------------------------
	return lsCommand, bExit


# ---------------------------------------------------
# -           Extract Action From Msg               -
# ---------------------------------------------------
def funExtractActionFromMsg (sCurrMsg):

	# Set variables -------------------------------------
	dActionDict = {  'BAJAR'    : '0',      'BAJA'    : '0',     \
			 'CERRAR'   : '0',      'CIERRA'  : '0',     u'CIÉRRA'  : '0',     'CERRANDO'   : '0',     u'CERRÁNDO'   : '0',    \
			 'CHAPAR'   : '0',      'CHAPA'   : '0',     u'CHÁPA'   : '0',     'CHAPANDO'   : '0',     u'CHAPÁNDO'   : '0',    \
			 'ABRIR'    : '75',     'ABRE'    : '75',    u'ÁBRE'    : '75',    'ABRIENDO'   : '75',    u'ABRIÉNDO'   : '75',   \
			 'SUBIR'    : '75',     'SUBE'    : '75',    u'SÚBE'    : '75',    'SUBIENDO'   : '75',    u'SUBIÉNDO'   : '75',   \
			 'LEVANTAR' : '75',     'LEVANTA' : '75',    u'LEVÁNTA' : '75',    'LEVANTANDO' : '75',    u'LEVANTÁNDO' : '75',   \
			 'LIMPIAR'  : 'CLEAN',  'LIMPIA'  : 'CLEAN', u'LÍMPIA'  : 'CLEAN', 'LIMPIANDO'  : 'CLEAN', u'LIMPIÁNDO'  : 'CLEAN', 'LIMPIE'  : 'CLEAN', \
			 'BARRER'   : 'CLEAN',  'BARRE'   : 'CLEAN', u'BÁRRE'   : 'CLEAN', 'BARRIENDO'  : 'CLEAN', u'BARRIÉNDO'  : 'CLEAN', 'BARRA'   : 'CLEAN', \
			 'PARAR'    : 'CLEAN',  'PARA'    : 'CLEAN', u'PÁRA'    : 'CLEAN', 'PARANDO'    : 'CLEAN', u'PARÁNDO'    : 'CLEAN', 'PARE'    : 'CLEAN', \
			 'DETENER'  : 'CLEAN', u'DET?N'   : 'CLEAN', u'DETÉN'   : 'CLEAN', 'DETENIENDO' : 'CLEAN', u'DETENIÉNDO' : 'CLEAN', 'DETENGA' : 'CLEAN', \
			 'RECOGER'  : 'DOCK',   'RECOGE'  : 'DOCK',  u'RECÓGE'  : 'DOCK',  'RECOGIENDO' : 'DOCK',  u'RECOGIÉNDO' : 'DOCK',  'RECOJA'  : 'DOCK',  \
			 'MANTENIMIENTO' : ['CLEAN', 'CLEAN'] }

	# Set variables -------------------------------------
	sAction = ""

	# Check Action --------------------------------------
	for sKey in dActionDict:

		# Check if match ------------------------------------
		if sCurrMsg.find(sKey) >= 0: 
			sAction = dActionDict[sKey]

	# Return --------------------------------------------
	return sAction
	

# ---------------------------------------------------
# -         Extract Device List From Msg            -
# ---------------------------------------------------
def funExtractDeviceListFromMsg (sCurrMsg):

	#pdb.set_trace()

	# Set variables -------------------------------------
	dDevIdDict = { 'PERSIANA'    : {  'DORMITORIO' : '3',   'ENCUENTRO Y AMOR'  : '3', \
				          'COCINA'     : '4',   \
					 u'SALÓN'      : '5',   'COMEDOR'           : '5', \
					 u'ÁLVARO'     : '6',   'ALVARITO'          : '6', 'PILAR' : '6', 'PILI' : '6', 'INVITADOS' : '6', \
					  'OFICINA'    : '7',   }, \
			'TELE'       : {  'TELE'       : '101'  }, \
			'ASPIRADORA' : {  'ROOMBA'     : '201', '780' : '201', 'RUMBA' : '201' }, \
			'ASPIRADOR'  : {  'ROOMBA'     : '201', '780' : '201', 'RUMBA' : '201' } }

	# Set variables -------------------------------------
	bKey            = False
	lsDeviceList    = []
	bDevTypePattern = False

	# Check Device Type ---------------------------------
	for sKey in dDevIdDict:
		if sCurrMsg.find(sKey) >= 0 :
			dDevIdDict = dDevIdDict[sKey]
			bKey = True
			break

	# Check Device Id -----------------------------------
	if bKey == True:

		for sKey in dDevIdDict:

			# Check if match ------------------------------------
			if sCurrMsg.find(sKey) >= 0 or sCurrMsg.find("TODAS") >= 0: 

				if dDevIdDict[sKey] not in lsDeviceList:

					lsDeviceList.append(dDevIdDict[sKey])

	# Return --------------------------------------------
	return lsDeviceList


# ---------------------------------------------------
# -               Command Analysis                  -
# ---------------------------------------------------
def funCommandAnalysis (cWhatsappListener, lPrevCounter, vTab = ""):

	# Set variables -------------------------------------
	sComment = "Command not executed, sorry."
	bExit    = False
	vNextTab = "     "
	vPathLog = vega_SetVariables_mod.funSetVariable('WAPP_LOG')
	sCurrMsg = cWhatsappListener.lvMessage[lPrevCounter][2]
	#sCurrMsg = sCurrMsg.decode('utf-8').encode('ascii','replace')
	sCurrMsg = sCurrMsg.decode('utf-8').upper()

	# Check exit condition ------------------------------
	if sCurrMsg.find(u'ADIÓS') >= 0:
		bExit = True
		sComment = "Bye"
		return bExit, sComment

	# Get Device List -----------------------------------
	lsDevice = funExtractDeviceListFromMsg (sCurrMsg)
	vega_Log_mod.funAppendToLog ( vTab + vNextTab + "Device List:\t" + str(lsDevice), vLogFile = vPathLog )
	
	# Get Action ----------------------------------------
	sAction = funExtractActionFromMsg (sCurrMsg)
	vega_Log_mod.funAppendToLog ( vTab + vNextTab + "Action:\t" + str(sAction), vLogFile = vPathLog )

	# Execute Action ------------------------------------
	if lsDevice <> [] and sAction <> "":

		# Execute command ------------------------------------
		lsCommand, bExit = funExecuteComand (lsDevice, sAction)
		if bExit == True:
			sComment  = "Done!"
			sResult   = "OK"
		else:
			sComment = "Unable to execute command."
			sResult   = "NOK"

		# Log -----------------------------------------------
		vega_Log_mod.funAppendToLog ( vTab + vNextTab + "Executing:\t" + sResult + " (" + sComment[:-1] + ")", vLogFile = vPathLog )


	# Exit ----------------------------------------------
	return False, sComment

# ---------------------------------------------------
# -                    T O P                        -
# ---------------------------------------------------
import time
import pdb
import os

import vega_Log_mod
import vega_SetVariables_mod
