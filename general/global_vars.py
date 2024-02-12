
#------------ SM GLOBAL VARIABLES -------------------------------------------
# The following variables are used in the statemachine for keeping track of the states
next_E          = 0 
cur_S           = 0
prev_S          = 0
terminate_SM    = False
doescount       = 5       #??????????????????????????????????????????
dose_number     = 0


SM_TEXT_TO_DIAPLAY = "--"       # This is the text that will be displayed on the status section of statemachiens on GUI
PAUSE = False                   # Boolean that shows if pause button is pressed
ERROR = False                   # Boolean that shows if an error happened
NEXT = False                    # Boolean that shows if Next button is pressed
activate_NEXT_button = False    # boolean that specify if Nex button is enable/disabled

# The following object are used to create instances of hardware classes
pump1   = None
motors  = None
labjack = None
tec     = None

# The followings are boolean variables that are used to turn the pump/gantry LEDs on/off
pump1_titrant_active_led    = False
pump1_titrant_homed_led     = False
pump2_sample_active_led     = False
pump2_sample_homed_led      = False
horizontal_gantry_active_led= False
horizontal_gantry_homed_led = False
vertical_gantry_active_led  = False
vertical_gantry_homed_led   = False
mixing_motor_active_led     = False
mixing_motor_homed_led      = False


current_Aspiration_count = 0        #?????????????????????????????

# Sacling factor for converting volume to pump internal units
PUMP_SAMPLE_SCALING_FACTOR = 1
PUMP_TITRANT_SCALING_FACTOR = 1

# The folloiwng varialbes hold the value read from bubble sensors
BS1 = 0
BS2 = 0
BS3 = 0
BS4 = 0
BS5 = 0
BS6 = 0
BS7 = 0
BS8 = 0
BS9 = 0
BS10 = 0
BS11 = 0
BS12 = 0
BS13 = 0
BS14 = 0
# The following booleans are in the GUI to show bubble sensor LEDS to be on or off
BS1_LED = False
BS2_LED = False
BS3_LED = False
BS4_LED = False
BS5_LED = False
BS6_LED = False
BS7_LED = False
BS8_LED = False
BS9_LED = False
BS10_LED = False
BS11_LED = False
BS12_LED = False
BS13_LED = False
BS14_LED = False

# The followings are the strings that will be displayed on the experiment section of GUI
VALVE_1 = "--v1--"              # Valve 1 position
VALVE_2 = "--v2--"              # Valve 2 position
VALVE_3 = "--v3--"              # Valve 3 position
VALVE_4 = "--v4--"              # Valve 4 position
VALVE_5 = "--v5--"              # Valve 5 position
VALVE_6 = "--v6--"              # Valve 6 position
VALVE_7 = "--v7--"              # Valve 7 position
VALVE_8 = "--v8--"              # Valve 8 position
VALVE_9 = "--v9--"              # Valve 9 position

# The following strings will be displayed on the TEC section of GUI
TEC_TARGET      = "target"
TEC_ACTUAL      = "actual"
TEC_IS_ON       = False
DOSE_VOLUME     = "0 ul"
DOSE_COMPLETED  = "0 ul"
TOTAL_DOSES     = "0 ul"
MIXING_SPEED    = "0 RPM"


SM_list     = None                  # Note: this varialbe must be filled as soon as run_GUI is executed (it's in run_SM_GUI.init)
SM_list_str = None              # Note: this varialbe must be filled as soon as run_GUI is executed (it's in run_SM_GUI.init)

SM_enabled_dic = None           # a dictionary that keeps track of what statemchines are enabled in the recipe

# the folowwing variables are used to keep track of Dose/Mixing/Equilibrium signals
DoseSignalRecived   = False     # is the Dose signal recieved from Malvern box?
EquilibriumReached  = False     # is the equilibrium reached in Malvern box?
MixingSignalReady   = False     # is the mxing signal ready received from Malvern box?
current_dose_volume = 0         # current dose number (updates after each dose delivery in Experiment SM)

grPC_Client = None



def reset():
    next_E = 0 
    cur_S = 0
    prev_S = 0
    terminate_SM = False
    doescount = 5
    dose_number = 0
    SM_TEXT_TO_DIAPLAY = "--"
    PAUSE = False
    ERROR = False


def init():
    # GENERAL = General_vars()
    reset()
   