#!/usr/bin/python
# coding: latin-1
# ---------------------------------------------------
# -                    T O P                        -
# ---------------------------------------------------
import sys
import pdb

import vega_Path
import vega_Log_mod
import vega_ScreenHeader_mod
import vega_SetVariables_mod
import vega_Whatsapp_mod

# Set variables -------------------------------------
vPathLog = vega_SetVariables_mod.funSetVariable('WAPP_LOG')

# Starting execution --------------------------------
vega_ScreenHeader_mod.funPrintHeader ("                  STARTING EXECUTION", vLogFile=vPathLog)
vega_ScreenHeader_mod.funPrintHeader ("Whatsapp", vLogFile=vPathLog)

# Startup Whatsapp ----------------------------------
vega_Whatsapp_mod.main()

# End of execution ----------------------------------
vega_ScreenHeader_mod.funPrintHeader ("                  END OF EXECUTION", vLogFile=vPathLog)
vega_Log_mod.funAppendToLog ( "", vLogFile=vPathLog)

