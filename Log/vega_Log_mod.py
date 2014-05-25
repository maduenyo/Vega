#!/usr/bin/python3

# ---------------------------------------------------
# -                Append to Log                    -
# ---------------------------------------------------
def funAdjustStringLength (vString, vLength):

	# Check length --------------------------------------
	if vLength < 10:

		# Exit ----------------------------------------------
		return vString

	# Check string lenght -------------------------------
	if len(vString) < vLength:

		# Add padding to string -----------------------------
		vString = vString + " " * (vLength - len(vString))

	elif len(vString) > vLength:

		# Cut string length ---------------------------------
		vString = vString[0:vLength-3] + '...'

	# Exit ----------------------------------------------
	return vString


# ---------------------------------------------------
# -                Append to Log                    -
# ---------------------------------------------------
def funAppendToLog (vLogLine='', vEnd='\n', vLogHeader=True, vSilentMode=False, vLogFile=""):

	# Check vShowLog ------------------------------------
	if vSilentMode == True:

		# Silent mode -------------------------------
		return

	# Get caller info -----------------------------------
	vFrame    = inspect.currentframe()

	# Back to needed frame ------------------------------
	vContinue = True
	while vContinue == True: 
		if vFrame.f_code.co_name == 'funAppendToLog':
			vFrame = vFrame.f_back
			vContinue = False

		else:
			vFrame = vFrame.f_back

	# Set variables -------------------------------------
	vCode     = vFrame.f_code
	vModule   = vCode.co_filename.split('/')[-1]
	vFunction = vCode.co_name

	# Adjust string lenghts -----------------------------
	vLength   = 40
	vModule   = funAdjustStringLength (vModule, vLength)
	vFunction = funAdjustStringLength (vFunction, vLength)

	# Set variables -------------------------------------
	vTimestamp = vega_CommonFunctions_mod.funGetTimestamp()
	if vLogFile == "":
		vPath_Log = vega_SetVariables_mod.funSetVariable('PATH_LOG')
	else:
		vPath_Log = vLogFile
	
	# Write to Log --------------------------------------
	with open(vPath_Log, 'a') as vLogFile:
		if vLogHeader == False:
			# Log without timestamp -----------------------------
			vLogFile.write( vLogLine )

		else:
			# Log with timestamp --------------------------------
			if vLogLine != '':
				vLogFile.write(vTimestamp + " (" + vModule + ", " + vFunction + "): " + vLogLine )

		vLogFile.write( vEnd )


# ---------------------------------------------------
# -         Append To Log Traceback Info            -
# ---------------------------------------------------
def funAppendToLogTracebackInfo (vError, vMessage, vLogFile=""):

	# Set Varaibles -------------------------------------
	vDetail    =  vError.args[0]
	vTraceBack = traceback.extract_tb(sys.exc_info()[2])

	# Log -----------------------------------------------
	funAppendToLog ( "ERROR DETECTED " + "-" * 87 + ": " + "-" * 51 , vLogHeader=False, vLogFile=vLogFile )
	funAppendToLog ( "ERROR:\t " + vMessage, vLogFile=vLogFile)
	funAppendToLog ( "DETAIL:\t " + vDetail[0].upper() + vDetail[1:], vLogFile=vLogFile )

	# Traceback -----------------------------------------
	vIndex = 0
	for vFrame in vTraceBack:

		# Set variables -------------------------------------
		vIndex = vIndex + 1
		vFileName, vCodeLineNumber, vFunctionName, vCode = vFrame

		# Log -----------------------------------------------
		funAppendToLog ( " ", vLogFile=vLogFile )
		funAppendToLog ( "FRAME " + str(vIndex) + ": " + "File Name:\t"  + vFileName     + " (Line " + str(vCodeLineNumber) + ")", vLogFile=vLogFile )
		funAppendToLog ( "\t "                         + "Function:\t"   + vFunctionName, vLogFile=vLogFile )
		funAppendToLog ( "\t "                         + "Code Line:\t"  + vCode        , vLogFile=vLogFile )

	funAppendToLog ( "ERROR DETECTED " + "-" * 87 + ": " + "-" * 51 , vLogHeader=False, vLogFile=vLogFile )


# ---------------------------------------------------
# -                    T O P                        -
# ---------------------------------------------------
import inspect
import datetime
import pdb
import traceback
import sys

import vega_SetVariables_mod
import vega_CommonFunctions_mod
