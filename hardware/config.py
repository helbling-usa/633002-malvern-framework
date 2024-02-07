#------------------- CONSTANTS  -----------------------------------------
BS_THRESHOLD                = 2.5       # Threshold value for bubble sensor 1
PICKUP_UNTIL_BUBBLE_TARGET  = 20000     # Target position when pickup until bubble
DISPENSE_UNTIL_BUBBLE_TARGET  = 0       # Target position when pickup until bubble
BUBBLE_DETECTION_PUMP_SPEED = 50        # speed of pump during bubble detection
DEFAULT_PUMP_SPEEED         = 1000      # speed of pump at start up
GANTRY_VER_SPEED            = 15.0      # vertical gantry speed
GANTRY_HOR_SPEED            = 15.0      # horizontal gantry speed
GANTRY_VER_ACCELERATION     = 1         # vertical gantry acceleration
GANTRY_HOR_ACCELERATION     = 1         # horizontal gantry acceleration
MIXING_ACCELERATION         = 1         # mixing motor acceleration
RPM_2_TML_SPEED             = 0.1365    # conversion from rpm to mixing motor TML unit  (0.267 for Reza's mixer)
TML_LENGTH_2_MM_VER         = 10. /1000      # tml unit for length to um
TML_LENGTH_2_MM_HOR         = 7.5 /1000      # tml unit for length to um
# pumps/valves RS485 addresses
TIRRANT_PUMP_ADDRESS        = 1         # Pump 1
TITRANT_LOOP_ADDRESS        = 2         # pump 1 loop valve
TITRANT_PIPETTE_ADDRESS     = 4         # titrant line: pipette valve
TITRANT_CLEANING_ADDRESS    = 3         # titrant line: cleaning valve
SAMPLE_PUMP_ADDRESS         = 5         # pump 2
SAMPLE_LOOP_ADDRESS         = 6         # pump 2 loop valve
TITRANT_PORT_ADDRESS        = 7         # sample line: titrant port valve
DEGASSER_ADDRESS            = 8         # sample line: degasser valve
SAMPLE_CLEANING_ADDRESS     = 9         # sample line: cleaning valve

TEC_PORT = "COM5"                       # port address for TEC controller
TECHNOSOFT_PORT  = "COM7"               # port address for mixer motor controller
PUMP1_PORT = "COM6"                     # port address for pump 1
MIXER_AXIS_ID = 24                      # axis id of mixer motor
GANTRY_VER_AXIS_ID =  1                 # axis id of vertical gantry
GANTRY_HOR_AXIS_ID =  1                 # axis id of horizontal gantry

SM_EXECUTION_ORDER = ['Startup', 'PumpInit_Reload', 'Degas', 'Load_Prime','Func_NewAirSlugs']

#Bubble semsor IO port address on the labjack
BS1_IO_PORT = 0
BS2_IO_PORT = 1
BS3_IO_PORT = 2
BS4_IO_PORT = 3
BS5_IO_PORT = 4
BS6_IO_PORT = 5
BS7_IO_PORT = 6
BS8_IO_PORT = 7
BS9_IO_PORT = 8
BS10_IO_PORT = 9
BS11_IO_PORT = 10
BS12_IO_PORT = 11
BS13_IO_PORT = 12
BS14_IO_PORT = 13