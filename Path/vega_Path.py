#!/usr/bin/python3
# Add root subdirectories to PYTHON PATH

# ---------------------------------------------------
# -                 Get Root Path                   -
# ---------------------------------------------------
def funGetRootPath():

	# Set variables -------------------------------------
	vCurrPath = os.path.dirname(os.path.abspath(__file__))
	vDirName  = "/" + vCurrPath.split("/")[-1]
	vRootPath = vCurrPath[:-len(vDirName)]

	# Exit ----------------------------------------------
	return vRootPath

# ---------------------------------------------------
# -          Get Subdirectory Path List             -
# ---------------------------------------------------
def funGetSubdirectoryPathList(vRootPath):

	# Set variables -------------------------------------
	vRootSubdirectoryList = []
	vRoorSubpathList = os.listdir(vRootPath)

	# Get subdirectory list -----------------------------
	for vItem in vRoorSubpathList:

		# Set variables -------------------------------------
		vItem = vRootPath + "/" + vItem

		# Check subdirectory --------------------------------
		if os.path.isdir(vItem) == True and vItem.find("__pycache__") < 0 and vItem.find("__init__.pyc") <0:
			vRootSubdirectoryList.append(vItem)

	# Sort subdirectory list ----------------------------
	vRootSubdirectoryList.sort()
	
	# Exit ----------------------------------------------
	return vRootSubdirectoryList


# ---------------------------------------------------
# -             Update Python Path                  -
# ---------------------------------------------------
def funUpdatePythonPath(vRootPath, vRootSubdirectoryPathList):

	# Set variables -------------------------------------
	vTab           = "     "
	vAddedPathList = []

	# Append to PYTHON PATH -----------------------------
	for vRootSubdirectoryPath in vRootSubdirectoryPathList:
		if str(sys.path).find(vRootSubdirectoryPath) < 0:
			sys.path.append(vRootSubdirectoryPath)
			vAddedPathList.append(vRootSubdirectoryPath)

	# Import modules ------------------------------------
	import vega_Log_mod

	# Log -----------------------------------------------
	#vega_Log_mod.funAppendToLog ( "-" * 51 )
	#vega_Log_mod.funAppendToLog ( "UPDATING PYTHON PATH" )
	#vega_Log_mod.funAppendToLog ( vTab + "Root directory found:")
	#vega_Log_mod.funAppendToLog ( vTab * 2 + vRootPath)

	# Check vRootSubdirectoryPath ----------------------
	if vRootSubdirectoryPath != []:

		# Log ----------------------------------------------
		#vega_Log_mod.funAppendToLog ( vTab + "Its Subdirectories will be added to PYTHON PATH:")

		# Add path to PYTHON PATH ----------------------------------
		#for vPath in vAddedPathList:

			# Log -------------------------------------------------------
			#vega_Log_mod.funAppendToLog (vTab * 2 + vPath)

		# Log -------------------------------------------------------
		#vega_Log_mod.funAppendToLog (vTab * 2 + "Paths added:\t" + str(len(vAddedPathList)) )

		pass

	# Log -----------------------------------------------
	#vega_Log_mod.funAppendToLog ( "-" * 51 )

# ---------------------------------------------------
# -                      main                       -
# ---------------------------------------------------
def main():

	# Get root path -------------------------------------
	vRootPath = funGetRootPath()
	if vRootPath == "":
		return

	# Get subdirectory list -----------------------------
	vRootSubdirectoryPathList = funGetSubdirectoryPathList(vRootPath)
	if vRootSubdirectoryPathList == []:
		return

	# Update PYTHON PATH --------------------------------
	funUpdatePythonPath(vRootPath, vRootSubdirectoryPathList)

	
# ---------------------------------------------------
# -                    T O P                        - 
# ---------------------------------------------------
import pdb
import sys
import os

main()
