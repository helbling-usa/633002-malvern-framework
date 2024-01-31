#------------------- CONSTANTS  -----------------------------------------
BS_THRESHOLD                = 2.5       # Threshold value for bubble sensor 1
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

pump1 = None
motors = None
labjack = None
tec = None

TEC_PORT = 0
TECHNOSOFT_PORT  = 0
PUMP1_PORT = 0
MIXER_AXIS_ID = 0
GANTRY_VER_AXIS_ID = 0
GANTRY_HOR_AXIS_ID = 0
MIXER_AXIS_ID = 0