#!/usr/bin/python3

# ---------------------------------------------------
# -                Print Header                     -
# ---------------------------------------------------
def funPrintHeader (vHeader, vLogFile=""):

	# Set variables -------------------------------------
	vLine = vHeader.upper()

	# Log -----------------------------------------------
	vega_Log_mod.funAppendToLog ( "---------------------------------------------------", vLogFile=vLogFile )
	vega_Log_mod.funAppendToLog ( vLine, vLogFile=vLogFile )
	vega_Log_mod.funAppendToLog ( "---------------------------------------------------", vLogFile=vLogFile )


# ---------------------------------------------------
# -                    T O P                        -
# ---------------------------------------------------
import pdb

import vega_Log_mod
