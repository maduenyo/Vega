#!/usr/bin/python3

# ---------------------------------------------------
# -           Get own IP and Hostname               -
# ---------------------------------------------------
def GetOwnIpAndHostname ():

    sHostname  = socket.gethostname()
    sIPAddress = socket.gethostbyname(sHostname)

    return sIPAddress, sHostname


# ---------------------------------------------------
# -                 VLookUp Table 2                 -
# ---------------------------------------------------
def funVLookUpTable2 (vDbConn, vTableName, vInputColNameList, vInputValueMatrix, vOutputColName):

	# Set variables -----------------------------
	vFilterMatrix = [ str(tuple(vInputValueList)).replace(',)',')') for vInputValueList in vInputValueMatrix ]

	# Set SQL Query -----------------------------
	vIndex = 0
	vSqlQueryInitial = "SELECT * FROM " + vTableName # + " WHERE "
	vSqlQuery        = vSqlQueryInitial 
	for vInputColName in vInputColNameList:

		# Check for wildcard ------------------------
		if '*' not in vFilterMatrix[vIndex]:

			# Check if vSqlQuery needs " WHERE" ---------
			if vSqlQuery ==  vSqlQueryInitial:
				vSqlQuery = vSqlQuery + " WHERE "

			# Set variables -----------------------------
			vSqlQuery = vSqlQuery + vInputColName + " IN " + vFilterMatrix[vIndex] + " AND "

		# Set variables -----------------------------
		vIndex = vIndex + 1

	# Remove last " AND " from vSqlQuery ----------------
	vSqlQuery = vSqlQuery[:-5]

	# Get records -------------------------------
	vCursor = vDbConn.cursor()
	vCursor.execute(vSqlQuery)
	vData = vCursor.fetchall()

	# Get List ----------------------------------
	vTableDict  = funGetTableDictionary (vDbConn, vTableName)
	vOutputCol  = vTableDict[vOutputColName]
	vOutputList = [ vRow[vOutputCol] for vRow in vData ]

	# Exit --------------------------------------
	return vOutputList


# ---------------------------------------------------
# -                  VLookUp Table                  -
# ---------------------------------------------------
def funVLookUpTable (vDbConn, vTableName, vInputColName, vInputValueList, vOutputColName):

	# Set variables -----------------------------
	vSqlQuery = "SELECT * FROM " + vTableName
	if '*' not in vInputValueList:
		vSqlQuery = vSqlQuery + " WHERE " + vInputColName + " IN " + str(tuple(vInputValueList)).replace(',)',')')

	# Get records -------------------------------
	vCursor = vDbConn.cursor()
	vCursor.execute(vSqlQuery)
	vData = vCursor.fetchall()

	# Get List ----------------------------------
	vTableDict  = funGetTableDictionary (vDbConn, vTableName)
	vOutputCol  = vTableDict[vOutputColName]
	vOutputList = [ vRow[vOutputCol] for vRow in vData ]

	# Exit --------------------------------------
	return vOutputList


# ---------------------------------------------------
# -             Get Table Dictionary                -
# ---------------------------------------------------
def funGetTableDictionary (vDbConn, vTableName):

	with vDbConn:

		# Set variables -------------------------------------
		vTableDictionary = {}

		# Get header of table -------------------------------
		vCursor = vDbConn.cursor()
		vCursor.execute("SELECT * FROM " + vTableName)
		vColumnNameList = [vColName[0] for vColName in vCursor.description]

		# Create dictionary ---------------------------------
		vCol = 0
		for vColumName in vColumnNameList:
			vTableDictionary.update ( { vColumName : vCol } )
			vCol = vCol + 1

		# Exit ----------------------------------------------
		return vTableDictionary


# ---------------------------------------------------
# -                Get Timestamp                    -
# ---------------------------------------------------
def funGetTimestamp ():

	# Set variables -------------------------------------
	vToday     = datetime.datetime.now()
	vTimeStamp = vToday.strftime('%Y%m%d %H:%M.%S')
	
	# Exit ----------------------------------------------
	return vTimeStamp


# ---------------------------------------------------
# -                    T O P                        -
# ---------------------------------------------------
import datetime
import socket
import pdb

