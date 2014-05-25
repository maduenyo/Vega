#!/usr/bin/python3

# ---------------------------------------------------
# -               Set Variable                      -
# ---------------------------------------------------
def funSetVariable (vVarName):

	# PATH and FILEs ------------------------------------
	vVarDict = {}
	vVarDict.update ( { 'PATH_BASE' : '/home/pi/SCRIPTS/Python/Projects/vega' } )
	vVarDict.update ( { 'PATH_CRON' : '/home/pi/SCRIPTS/Python/Projects/vega/logs' } )
	vVarDict.update ( { 'PATH_DB'   : '/home/pi/SCRIPTS/Python/Projects/vega/db/vega.db' } )
	vVarDict.update ( { 'PATH_EXE'  : '/home/pi/SCRIPTS/Python/Projects/vega/root/ExecuteCommand/vega_ExecuteCommand.py' } )
	vVarDict.update ( { 'PATH_LOG'  : '/home/pi/SCRIPTS/Python/Projects/vega/logs/vega_general.log' } )

	# EXECUTE COMMAND ------------------------------------
	vVarDict.update ( { 'EXEC_LOG' : '/home/pi/SCRIPTS/Python/Projects/vega/logs/vega_execute.log' } )

	# TECHNOLOGY -----------------------------------------
	vVarDict.update ( { 'VAR_TECH'       : { 'Z-Wave' : ['ZWaveAPI', 'Run'], 'Linux' : ['/bin/sh -exec '] } } )
	vVarDict.update ( { 'EXE_ARGS'       : [ [ 'LITERAL', ' -Standby OVERRIDE -Operation ENABLED -Calendar "*" -DoM "*" -DoW "*" -Cmd ' ] ] } ) 
	vVarDict.update ( { 'ZWAVE_CMD_BASE' : [ [ 'LITERAL', '/usr/bin/curl -s -LN --globoff ' ], \
				 		 [ 'LITERAL', "'http://" ], \
						 [ 'POINTER', [ 'DEVICE', 'DEVPROP', 'CONNECTION', 'CONTROLLER', 'Host' ] ], \
						 [ 'LITERAL', '.' ], \
						 [ 'POINTER', [ 'DEVICE', 'DEVPROP', 'CONNECTION', 'CONTROLLER', 'Domain' ] ], \
						 [ 'LITERAL', ':' ], \
						 [ 'POINTER', [ 'DEVICE', 'DEVPROP', 'CONNECTION', 'CONTROLLER', 'Port' ] ], \
						 [ 'LITERAL', '/ZWaveAPI/Run/devices[' ], \
						 [ 'POINTER', [ 'DEVICE', 'DEVPROP', 'CONNECTION', 'Parameter01' ] ], \
						 [ 'LITERAL', '].instances[' ], \
						 [ 'POINTER', [ 'DEVICE', 'DEVPROP', 'CONNECTION', 'Parameter02' ] ], \
						 [ 'LITERAL', '].commandClasses[' ], \
						 [ 'POINTER', [ 'DEVICE', 'DEVPROP', 'CONNECTION', 'Parameter03' ] ], \
						 [ 'LITERAL', ']' ] 	] } )
	vVarDict.update ( { 'ZWAVE_CMD_GET'  : [ [ 'LITERAL', '.data.level.value' + "'" ] ] } )
	vVarDict.update ( { 'ZWAVE_CMD_SET'  : [ [ 'LITERAL', '.Set(' ], \
						 [ 'VALUE' ], \
						 [ 'LITERAL', ')' + "'"  ] ] } )


	# WEATHER -------------------------------------------
	vVarDict.update ( { 'WEAT_LOG' : '/home/pi/SCRIPTS/Python/Projects/vega/logs/vega_weather.log' } )
	vVarDict.update ( { 'YAHOO'    : [ 'yahoo.com',   ['Rain', 'Showers', 'Thunderstorms', 'T-Storms', 'Snow' ] ] } )
	vVarDict.update ( { 'WEATHER'  : [ 'weather.com', ['Rain', 'Showers', 'Thunderstorms', 'T-Storms', 'Snow' ] ] } )

	# STATES ---------------------------------------------
	vVarDict.update ( { 'TOLERANCE'  : 2  } )
	vVarDict.update ( { 'WAITTIME'   : 1  } )
	vVarDict.update ( { 'WAITCYCLES' : 25 } )

	# WHATSAPP -------------------------------------------
	vVarDict.update ( { 'WAPP_LOG'      : '/home/pi/SCRIPTS/Python/Projects/vega/logs/vega_whatsapp.log' } )
	vVarDict.update ( { 'WAPP_USERNAME' : '34668857875' } )
	vVarDict.update ( { 'WAPP_PASSWORD' : 'GDma1sXwkTORBQSkbJXApLVBZnQ=' } )
	vVarDict.update ( { 'WAPP_CALLER'   : { '34668857875' : 'Vega', '34619809398' : 'Juan', '34619365132' : 'Marta'}  } )
	vVarDict.update ( { 'WAPP_PIC'      : '/home/pi/SCRIPTS/Python/Projects/vega/db/whatsapp_pic.jpeg' } )
	vVarDict.update ( { 'WAPP_STATUS'   : 'At your command' } )

	vVarDict.update ( { 'WAPP_ACTION_EXIT' : ['reboot', 'bye', 'adi?s'] } )
	vVarDict.update ( { 'WAPP_ANSWER_EXIT' : ['reboot', 'bye', 'adi?s'] } )

	# DEBUG ----------------------------------------------
	vVarDict.update ( { 'DEBUG'  : False } )

	# Exit ----------------------------------------------
	return vVarDict[vVarName.upper()]


# ---------------------------------------------------
# -                    T O P                        -
# ---------------------------------------------------
import pdb
