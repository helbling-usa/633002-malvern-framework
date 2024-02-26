#------------------------------ Gantry Parameters -------------------------------------------------
GANTRY_VER_SPEED                = 15.0      # vertical gantry speed
GANTRY_HOR_SPEED                = 15.0      # horizontal gantry speed
GANTRY_VER_ACCELERATION         = 1         # vertical gantry acceleration
GANTRY_HOR_ACCELERATION         = 1         # horizontal gantry acceleration
MIXING_ACCELERATION             = 1         # mixing motor acceleration
RPM_2_TML_SPEED                 = 0.1365    # conversion from rpm to mixing motor TML unit  (0.267 for Reza's mixer)
TML_LENGTH_2_MM_VER             = 10. /1000      # tml unit for length to um
TML_LENGTH_2_MM_HOR             = 7.5 /1000      # tml unit for length to um
TML_SPEED_2_MM_PER_SEC_HOR      = 7.5
TML_SPEED_2_MM_PER_SEC_VER      = 7.5
#------------------------------ Com Ports ---------------------------------------------------------
TEC_PORT                        = "COM5"                       # port address for TEC controller
TECHNOSOFT_PORT                 = "COM7"               # port address for mixer motor controller
PUMP1_PORT                      = "COM6"                     # port address for pump 1

#------------------------------ Technosoft controller axes ----------------------------------------
MIXER_AXIS_ID                   = 24                      # axis id of mixer motor
GANTRY_VER_AXIS_ID              =  1                 # axis id of vertical gantry
GANTRY_HOR_AXIS_ID              =  1                 # axis id of horizontal gantry

#------------------------------ Bubble semsor IO port address on the labjack ----------------------
BS1_IO_PORT     = 0
BS2_IO_PORT     = 1
BS3_IO_PORT     = 2
BS4_IO_PORT     = 3
BS5_IO_PORT     = 4
BS6_IO_PORT     = 5
BS7_IO_PORT     = 7#6  #set this to 7 for Reza's setupyea
BS8_IO_PORT     = 7
BS9_IO_PORT     = 8
BS10_IO_PORT    = 9
BS11_IO_PORT    = 10
BS12_IO_PORT    = 11
BS13_IO_PORT    = 12
BS14_IO_PORT    = 13

#-------------------------------- Bubble sensor detection threshold -------------------------------
BS_THRESHOLD                    = 2.5       # Threshold value for bubble sensor 1

#-------------------------------- Temperature threshold for TEC -----------------------------------
TEC_ACCEPTABLE_TEMP_DIFF        = 1         # This is acceptable temp. difference of current temp. to the target temp.
                                            #  is considered close enough once the tec temp reahced this 
                                            #  distance from target temp, it will move to next state

#------------------------------ Pumps Parameters --------------------------------------------------
PICKUP_UNTIL_BUBBLE_TARGET_SAMPLE   = 192000     # Target position when pickup until bubble (sample pump)
PICKUP_UNTIL_BUBBLE_TARGET_TITRANT  = 192000     # Target position when pickup until bubble (titrant pump)
DISPENSE_UNTIL_BUBBLE_TARGET        = 0         # Target position when pickup until bubble
BUBBLE_DETECTION_PUMP_SPEED         = 50        # speed of pump during bubble detection
DEFAULT_PUMP_SPEEED                 = 1000      # speed of pump at start up
SAMPLE_PUMP_VOLUM_2_STEP            = 9.6       # conversion ratio fro sample pump for full step mode
SAMPLE_PUMP_VOLUM_2_MICROSTEP       = 76.8      # conversion ratio fro sample pump for full microstep mode
TITRANT_PUMP_VOLUM_2_STEP           = 96        # conversion ratio fro titrant pump for full step mode
TITRANT_PUMP_VOLUM_2_MICROSTEP      = 768       # conversion ratio fro titrant pump for full microstep mode

#------------------------------- Pumps/valves RS485 addresses -------------------------------------
TIRRANT_PUMP_ADDRESS            = 1         #4way- Pump 1
TITRANT_LOOP_ADDRESS            = 3         #4way- pump 1 loop valve
TITRANT_PIPETTE_ADDRESS         = 5         #3way- titrant line: pipette valve
TITRANT_CLEANING_ADDRESS        = 9         #6way- titrant line: cleaning valve
SAMPLE_PUMP_ADDRESS             = 2         #4way- pump 2
SAMPLE_LOOP_ADDRESS             = 4         #4way- pump 2 loop valve
TITRANT_PORT_ADDRESS            = 6         #3way- sample line: titrant port valve
DEGASSER_ADDRESS                = 7         #6way- sample line: degasser valve
SAMPLE_CLEANING_ADDRESS         = 8         #6way- sample line: cleaning valve

#------------------------------- Valves port assignment -------------------------------------------
VALVE1_P1   = 'E'
VALVE1_P2   = 'O'
VALVE1_P3   = 'I'
VALVE1_P4   = 'B'

VALVE2_P1   = 'E'
VALVE2_P2   = 'O'
VALVE2_P3   = 'I'
VALVE2_P4   = 'B'

VALVE3_P1   = 'E'
VALVE3_P2   = 'O'
VALVE3_P3   = 'I'
VALVE3_P4   = 'B'

VALVE4_P1   = 'E'
VALVE4_P2   = 'O'
VALVE4_P3   = 'I'
VALVE4_P4   = 'B'

VALVE5_P1   =  'I'
VALVE5_P2   =  'E' 
VALVE5_P3   =  'O'

VALVE6_P1   =  'I'
VALVE6_P2   =  'E' 
VALVE6_P3   =  'O'

VALVE7_P1   = 1
VALVE7_P2   = 2
VALVE7_P3   = 3
VALVE7_P4   = 4
VALVE7_P5   = 5
VALVE7_P6   = 6

VALVE8_P1   = 1
VALVE8_P2   = 2
VALVE8_P3   = 3
VALVE8_P4   = 4
VALVE8_P5   = 5
VALVE8_P6   = 6

VALVE9_P1   = 1
VALVE9_P2   = 2
VALVE9_P3   = 3
VALVE9_P4   = 4
VALVE9_P5   = 5
VALVE9_P6   = 6
