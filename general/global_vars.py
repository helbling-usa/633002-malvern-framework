
#------------ SM GLOBAL VARIABLES -------------------------------------------
next_E = 0 
cur_S = 0
prev_S = 0
terminate_SM = False
doescount = 5
dose_number = 0
SM_TEXT_TO_DIAPLAY = "--"
PAUSE = False
ERROR = False
NEXT = False
activate_NEXT_button = False

pump1 = None
motors = None
labjack = None
tec = None

pump1_titrant_active_led = False
pump1_titrant_homed_led = False
pump2_sample_active_led = False
pump2_sample_homed_led = False
horizontal_gantry_active_led = False
horizontal_gantry_homed_led = False
vertical_gantry_active_led = False
vertical_gantry_homed_led = False
mixing_motor_active_led = False
mixing_motor_homed_led = False

current_Aspiration_count = 0

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

VALVE_1 = "--v1--"
VALVE_2 = "--v2--"
VALVE_3 = "--v3--"
VALVE_4 = "--v4--"
VALVE_5 = "--v5--"
VALVE_6 = "--v6--"
VALVE_7 = "--v7--"
VALVE_8 = "--v8--"
VALVE_9 = "--v9--"

TEC_TARGET = "target"
TEC_ACTUAL = "actual"
TEC_IS_ON = False
DOSE_VOLUME = "0 ul"
DOSE_COMPLETED = "0 ul"
TOTAL_DOSES = "0 ul"
MIXING_SPEED = "0 RPM"




SM_list = None      # Note: this varialbe must be filled as soon as run_GUI is executed (it's in run_SM_GUI.init)
SM_list_str = None  # Note: this varialbe must be filled as soon as run_GUI is executed (it's in run_SM_GUI.init)


SM_enabled_dic = None


DoseSignalRecived = False
EquilibriumReached = False
MixingSignalReady = False
current_dose_volume = 0

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
   