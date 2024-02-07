import  numpy as np
import  general.global_vars as GV
import  hardware.config as HW
import  time
from    general.recipe import RECIPE

##-----------------   ("next STATE","FUCNCTION") --------------------------------------------------
#-------------   -------E0-------    ------E1-------  -------E2-------  -------E3-------  -------E4-------  -------E5-------  
TT = np.array([[( 1, 'action0_0'),  (0, 'None')     , (0, 'None')     , (0, 'None')     , (0, 'None')     , (0, 'None')     ],  #<---STATE0
               [( 1, 'action1_0'),  (1, 'action1_1'), (2, 'action1_2'), (5, 'action1_3'), (5, 'action1_4'), (0, 'None')     ],  #<---STATE1
               [( 2, 'action2_0'),  (2, 'action2_1'), (3, 'action2_2'), (5, 'action2_3'), (6, 'action2_4'), (0, 'None')     ],  #<---STATE2
               [( 3, 'action3_0'),  (3, 'action3_1'), (4, 'action3_2'), (5, 'action3_3'), (6, 'action3_4'), (0, 'None')     ],  #<---STATE3
               [( 4, 'action4_0'),  (4, 'action4_1'), (5, 'action4_2'), (6, 'action4_3'), (0, 'None')     , (0, 'None')     ],  #<---STATE4
               [( 5, 'action5_0'),  (1, 'action5_1'), (2, 'action5_2'), (3, 'action5_3'), (4, 'action5_3'), (7, 'action5_4')],  #<---STATE5
               [( 6, 'action7_0'),  (0, 'None')     , (0, 'None')     , (0, 'None')     , (0, 'None')     , (0, 'None')     ]   #<---STATE6
               ])


def name():
    return "GantrytoA"


state_name = {0:"S0: Initialization", 1:"S1: GantryZUp", 2:"S2: GantryXRight", 3:"S3: GantryZDown",
              4:"S4: GantryBComp", 5:"Pause", 6:"Error"}





#---------------  ACTIONS  --------------
def action0_0():
    str1 = "Initialization\n" "raise Z actuator to position"
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

    
    # h_gantry_homed = GV.horizontal_gantry_homed_led
    v_gantry_homed = GV.vertical_gantry_homed_led
    
    GV.vertical_gantry_active_led = True

    if (v_gantry_homed == False):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "Gantry not homed\n""going to ERROR state"
    else:        
        GV.SM_TEXT_TO_DIAPLAY = "Raize Z actuator to position"
        GV.next_E = 1


def action1_1():
    timeout = False
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "go to S1/E3"
        return 
    
    if (GV.ERROR == True or timeout==True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "go to S1/E4"
        return 

    GV.motors.select_axis(HW.GANTRY_VER_AXIS_ID)
    cur_motor_pos= GV.motors.read_actual_position()    
    h_position = RECIPE["GantrytoA"]["vertical_titration_position"]
    
    GV.motors.set_POSOKLIM(1)
    abs_pos_tml = int(h_position / HW.TML_LENGTH_2_MM_VER )
    next_pos = abs_pos_tml  + cur_motor_pos
    move_speed = RECIPE['GantrytoA']['gantry_move_speed'] 
    GV.motors.move_absolute_position(next_pos, move_speed, HW.GANTRY_VER_ACCELERATION)

    cur_motor_pos= GV.motors.read_actual_position()
    while (abs(cur_motor_pos - next_pos) > 50):
        time.sleep(1)
        cur_motor_pos= GV.motors.read_actual_position()
    GV.vertical_gantry_active_led = False


    GV.vertical_gantry_active_led = False
    str1 = "Actuator reached position\n" 
    GV.SM_TEXT_TO_DIAPLAY = str1
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
    

    
    # HW.vertical_gantry_active_led
    # HW.vertical_gantry_homed_led 
    GV.motors.select_axis(HW.GANTRY_HOR_AXIS_ID)
    cur_motor_pos= GV.motors.read_actual_position()
    v_position = RECIPE["GantrytoA"]["horizontal_titration_position"]
    
    GV.motors.set_POSOKLIM(1)
    abs_pos_tml = int(v_position / HW.TML_LENGTH_2_MM_HOR )
    move_speed = RECIPE['GantrytoA']['gantry_move_speed'] 
    next_pos = abs_pos_tml + cur_motor_pos
    GV.motors.move_absolute_position(next_pos, move_speed, HW.GANTRY_HOR_ACCELERATION)

    cur_motor_pos= GV.motors.read_actual_position()
    while (abs(cur_motor_pos - next_pos) > 50):
        time.sleep(1)
        cur_motor_pos= GV.motors.read_actual_position()

    GV.horizontal_gantry_active_led = False
    GV.SM_TEXT_TO_DIAPLAY = "Move X actuator to position"
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
    
    GV.vertical_gantry_active_led = True

    GV.SM_TEXT_TO_DIAPLAY ="Lower Z actuator to position"
    GV.next_E = 1


def action3_1():
    timeout = False
    Done = True
    if (GV.PAUSE == True):
        GV.next_E = 3        
        GV.SM_TEXT_TO_DIAPLAY =  "  going to S3/E3"
        return 
    if (GV.ERROR == True or timeout==True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "  going to S3/E4"
        return    
         

    GV.motors.select_axis(HW.GANTRY_VER_AXIS_ID)
    cur_motor_pos= GV.motors.read_actual_position()    
    h_position = RECIPE["GantrytoA"]["vertical_titration_position"]
    
    GV.motors.set_POSOKLIM(1)
    abs_pos_tml = int(h_position / HW.TML_LENGTH_2_MM_VER )
    next_pos =  cur_motor_pos - abs_pos_tml
    move_speed = RECIPE['GantrytoA']['gantry_move_speed'] 
    GV.motors.move_absolute_position(next_pos, move_speed, HW.GANTRY_VER_ACCELERATION)

    cur_motor_pos= GV.motors.read_actual_position()
    while ( abs(cur_motor_pos - next_pos) > 50):
        time.sleep(1)
        cur_motor_pos= GV.motors.read_actual_position()
    GV.vertical_gantry_active_led = False




    if (Done == False):
        GV.next_E = 1
        GV.SM_TEXT_TO_DIAPLAY = "   waiting for pump to reach position"
    else:
        GV.next_E = 2
        GV.SM_TEXT_TO_DIAPLAY ="  Terminating statemachine"


def action3_2():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY =  "  going to Next state"
        return 
    GV.terminate_SM = True
    GV.SM_TEXT_TO_DIAPLAY ="Terminating statemachine"
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


#--------------
def action4_0():
    if (GV.PAUSE == True):
        GV.SM_TEXT_TO_DIAPLAY ="Statemachined Paused"
        GV.next_E = 0
    else:
        GV.SM_TEXT_TO_DIAPLAY ="56,E0 -> action5_0\n" " prepare to resume workflow"
        GV.next_E = GV. prev_S
    

def action4_1():
    # print("S6,E1 -> action5_1")
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY = "  going back to S1/E0"

def action4_2():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="  going back to S2/E0"

def action4_3():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="  going back to S3/E0"

def action4_4():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="  going to ERROR state"


#--------------
def action5_0():
    # print("S6,E0 -> action6_0")
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="Error state"
