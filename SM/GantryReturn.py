import  numpy as np
import  general.global_vars as GV
import  hardware.config as HW
import  time
from    general.recipe import RECIPE

##-----------------   ("next STATE","FUCNCTION") --------------------------------------------------
#-------------   -------E0-------    ------E1-------  -------E2-------  -------E3-------  -------E4-------  ----------  
TT = np.array([[( 1, 'action0_0'),  (0, 'None')     , (0, 'None')     , (0, 'None')     , (0, 'None')     ],  #<---STATE0
               [( 1, 'action1_0'),  (1, 'action1_1'), (2, 'action1_2'), (4, 'action1_3'), (5, 'action1_4')],  #<---STATE1
               [( 2, 'action2_0'),  (2, 'action2_1'), (3, 'action2_2'), (4, 'action2_3'), (5, 'action2_4')],  #<---STATE2
               [( 3, 'action3_0'),  (3, 'action3_1'), (4, 'action3_2'), (5, 'action3_3'), (0, 'None')     ],  #<---STATE3
               [( 4, 'action5_0'),  (1, 'action4_1'), (2, 'action4_2'), (3, 'action4_3'), (0, 'None')     ],  #<---STATE4
               [( 5, 'action5_0'),  (0, 'None')     , (0, 'None')     , (0, 'None')     , (0, 'None')     ]   #<---STATE5
               ])


def name():
    return "GantryReturn"


state_name = {0:"S0: Initialization", 1:"S1: GantryZReturn", 2:"S2: GantryXReturn", 3:"S3: GantryReturnComp",
               4:"Pause", 5:"Error"}



#---------------  ACTIONS  --------------
def action0_0():
    str1 = "Initialization\n" "Cantry Zreturn"
    GV.SM_TEXT_TO_DIAPLAY = str1
    GV.current_Aspiration_count = 0
    GV.next_E = 0    


#--------------
def action1_0():
    if (GV.PAUSE == True):
        GV.next_E = 3          
        GV.SM_TEXT_TO_DIAPLAY = "Prepare to go to Pause State"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "Prepare to go to error State"
        return 
    
    h_gantry_homed = GV.horizontal_gantry_homed_led
    v_gantry_homed = GV.vertical_gantry_homed_led

    if (h_gantry_homed == False):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "Gantry Z not homed\n""going to ERROR state"
    if (v_gantry_homed == False):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "Gantry Z not homed\n""going to ERROR state"
    else:        
        GV.SM_TEXT_TO_DIAPLAY = "Raize Z actuator to position"
        GV.vertical_gantry_active_led = True
        GV.next_E = 1


def action1_1():
    timeout = False
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" "go to S1/E3"
        return 
    if (GV.ERROR == True or timeout==True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" "go to S1/E4"
        return 

    GV.motors.select_axis(HW.GANTRY_VER_AXIS_ID)
    high_position = RECIPE["GantryReturn"]["vertical_base_position"]    
    GV.motors.set_POSOKLIM(1)
    next_pos = int(high_position / HW.TML_LENGTH_2_MM_VER )
    move_speed = RECIPE['GantryReturn']['gantry_move_speed'] / HW.TML_SPEED_2_MM_PER_SEC_VER
    GV.motors.move_absolute_position(next_pos, move_speed, HW.GANTRY_VER_ACCELERATION)
    
    cur_motor_pos= GV.motors.read_actual_position()
    while (abs(cur_motor_pos - next_pos) > 10):
        time.sleep(1)
        cur_motor_pos= GV.motors.read_actual_position()
        print("\t\tcur Z pos: {},  target pos: {}".format(cur_motor_pos, next_pos))

    GV.vertical_gantry_active_led = False  
    GV.SM_TEXT_TO_DIAPLAY = "Z actuator base position\n"
    GV.next_E = 2


def action1_2():
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "go to S1/E3"
        return     
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "go to S1/E4"
        return     
    GV.SM_TEXT_TO_DIAPLAY ="  go to  State 2"
    GV.next_E = 0


def action1_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "  go to S1/E4"
        return     
    
    GV.SM_TEXT_TO_DIAPLAY ="  go to PAUSE state"
    GV.next_E = 0
    GV. prev_S = 1
    
    
def action1_4():
    GV.SM_TEXT_TO_DIAPLAY = "  go to ERROR state"
    GV.next_E = 0

#------------------------------------------------------------------------------------------------
def action2_0():
    if (GV.PAUSE == True):
        GV.next_E = 3        
        GV.SM_TEXT_TO_DIAPLAY =  "  going  pasue state"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY =  "  going to erro state"
        return 
    
    GV.horizontal_gantry_active_led = True
    GV.SM_TEXT_TO_DIAPLAY = "Move X actuator to position"
    GV.next_E = 1


def action2_1():
    timeout = False
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY =  "  goint to pause state"
        return 
    if (GV.ERROR == True  or  timeout==True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "  going to erro state"
        return 
    
    GV.motors.select_axis(HW.GANTRY_HOR_AXIS_ID)
    v_position = RECIPE["GantryReturn"]["horizontal_base_position"]
    GV.motors.set_POSOKLIM(1)
    next_pos = int(v_position / HW.TML_LENGTH_2_MM_HOR )
    move_speed = RECIPE['GantryReturn']['gantry_move_speed'] / HW.TML_SPEED_2_MM_PER_SEC_VER
    GV.motors.move_absolute_position(next_pos, move_speed, HW.GANTRY_HOR_ACCELERATION)

    cur_motor_pos= GV.motors.read_actual_position()
    while (abs(cur_motor_pos - next_pos) > 10):
        time.sleep(1)
        cur_motor_pos= GV.motors.read_actual_position()
        print("\t\tcur Z pos: {},  target pos: {}".format(cur_motor_pos, next_pos))

    GV.horizontal_gantry_active_led = False
    GV.SM_TEXT_TO_DIAPLAY = "X actuator in base position"
    GV.next_E = 2
    

def action2_2():
    timeout = False
    # passed_time = 10 # measure the  heating time
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "  goint to pause state"
        return 
    if (GV.ERROR == True  or  timeout==True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "  going to erro state"
        return        

    GV.SM_TEXT_TO_DIAPLAY ="Lower Z actuator to position"
    GV.next_E = 0


def action2_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY =  "  going to Error state"
        return         
    
    GV.SM_TEXT_TO_DIAPLAY ="going to Pause state"
    GV.next_E = 0
    GV. prev_S = 2


def action2_4():
    GV.SM_TEXT_TO_DIAPLAY ="goin to Error state"
    GV.next_E = 0

#--------------------------------------------------------------------------------------------
def action3_0():
    if (GV.PAUSE == True):
        GV.next_E = 3          
        GV.SM_TEXT_TO_DIAPLAY = "  going to S3/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "  going to S3/E4"
        return 
    
    GV.SM_TEXT_TO_DIAPLAY ="Terminating GantryReturn Statemachine"
    GV.next_E = 1


def action3_1():
    if (GV.PAUSE == True):
        GV.next_E = 3        
        GV.SM_TEXT_TO_DIAPLAY =  "  going to S3/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "  going to S3/E4"
        return         
    GV.next_E = 2
    GV.SM_TEXT_TO_DIAPLAY ="Terminating GantryReturn Statemachine"


def action3_2():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY =  "  going to Next state"
        return 
    GV.terminate_SM = True
    GV.SM_TEXT_TO_DIAPLAY ="Terminating GantryReturn Statemachine"
    GV.next_E = 0


def action3_3():
    if (GV.ERROR == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY =  "  going to Error State"
        return 
    
    GV.SM_TEXT_TO_DIAPLAY ="  go to PAUSE state"
    GV. prev_S = 3
    GV.next_E = 0

def action3_4():
    # print("S3,E3 -> action3_3")
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY =" go to ERROR state"


#----------------------------------------------------------------------------------------------
def action4_0():
    if (GV.PAUSE == True):
        GV.SM_TEXT_TO_DIAPLAY ="S4,E0 -> action4_0"
        GV.next_E = 0
    else:
        GV.SM_TEXT_TO_DIAPLAY ="54,E0 -> action4_0\n" " prepare to resume workflow"
        GV.next_E = GV. prev_S


def action4_1():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S4,E1 -> action4_1\n" "  going back to S1/E0"


def action4_2():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S4,E2 -> action4_2\n""  going back to S2/E0"      


def action4_3():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S4,E3 -> action4_3\n""  going back to S3/E0"


#--------------
def action5_0():
    print("S5,E0 -> action5_0")
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S5,E0 -> action5_0"

