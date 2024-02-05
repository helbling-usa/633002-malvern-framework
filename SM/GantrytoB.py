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
    return "GantrytoB"


state_name = {0:"S0: Initialization", 1:"S1: GantryZUp", 2:"S2: GantryXRight", 3:"S3: GantryZDown",
              4:"S4: GantryBComp", 5:"Pause", 6:"Error"}





#---------------  ACTIONS  --------------
def action0_0():
    str1 = "S0,E0 -> action0_0\n" "Initialization\n" "raise Z actuator to position"
    GV.SM_TEXT_TO_DIAPLAY = str1
    GV.current_Aspiration_count = 0
    GV.next_E = 0    


#--------------
def action1_0():
    if (GV.PAUSE == True):
        GV.next_E = 3          
        GV.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0\n" "Prepare to go to Pause State"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0\n" "Prepare to go to error State"
        return 

    
    # h_gantry_homed = GV.horizontal_gantry_homed_led
    v_gantry_homed = GV.vertical_gantry_homed_led
    
    GV.vertical_gantry_active_led = True

    if (v_gantry_homed == False):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0\n" "Gantry not homed\n""going to ERROR state"
    else:        
        GV.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0\n" "raize Z actuator to position"
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
    cur_motor_pos= GV.motors.read_actual_position()    
    h_position = RECIPE["GantrytoB"]["vertical_titration_position"]
    
    GV.motors.set_POSOKLIM(1)
    abs_pos_tml = int(h_position / HW.TML_LENGTH_2_MM_VER )
    next_pos = abs_pos_tml  + cur_motor_pos
    move_speed = RECIPE['GantrytoB']['gantry_move_speed'] 
    GV.motors.move_absolute_position(next_pos, move_speed, HW.GANTRY_VER_ACCELERATION)

    cur_motor_pos= GV.motors.read_actual_position()
    while (abs(cur_motor_pos - next_pos) > 50):
        time.sleep(1)
        cur_motor_pos= GV.motors.read_actual_position()
    GV.vertical_gantry_active_led = False


    GV.vertical_gantry_active_led = False
    str1 = "actuator reached position\n" "going to S1/E2"
    GV.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" + str1
    GV.next_E = 2

def action1_2():
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S1,E2 -> action1_2\n" "go to S1/E3"
        return     
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S1,E2 -> action1_2\n" "go to S1/E4"
        return     
    GV.SM_TEXT_TO_DIAPLAY ="S1,E2 -> action1_2\n" "  go to S2/E0 state"
    GV.next_E = 0

def action1_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S1,E3 -> action1_3\n" "  go to S1/E4"
        return     
    
    GV.SM_TEXT_TO_DIAPLAY ="S1,E2 -> action1_2\n"  "  go to PAUSE state"
    GV.next_E = 0
    GV. prev_S = 1
    
    
def action1_4():
    GV.SM_TEXT_TO_DIAPLAY = "S1,E4 -> action1_4\n" "  go to ERROR state"
    GV.next_E = 0

#------------------------------------------------------------------------------------------------
def action2_0():
    if (GV.PAUSE == True):
        GV.next_E = 3        
        GV.SM_TEXT_TO_DIAPLAY = "S2,E0 -> action2_1\n" "  going  pasue state"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S2,E0 -> action2_1\n" "  going to erro state"
        return 
    
    GV.horizontal_gantry_active_led = True
    GV.SM_TEXT_TO_DIAPLAY ="S2,E0 -> action2_0\n" "move X actuator to position"
    GV.next_E = 1

def action2_1():
    timeout = False
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1\n" "  goint to pause state"
        return 
    if (GV.ERROR == True  or  timeout==True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1\n" "  going to erro state"
        return 
    

    
    # HW.vertical_gantry_active_led
    # HW.vertical_gantry_homed_led 
    GV.motors.select_axis(HW.GANTRY_HOR_AXIS_ID)
    cur_motor_pos= GV.motors.read_actual_position()
    v_position = RECIPE["GantrytoB"]["horizontal_titration_position"]
    
    GV.motors.set_POSOKLIM(1)
    abs_pos_tml = int(v_position / HW.TML_LENGTH_2_MM_HOR )
    move_speed = RECIPE['GantrytoB']['gantry_move_speed'] 
    next_pos = abs_pos_tml + cur_motor_pos
    GV.motors.move_absolute_position(next_pos, move_speed, HW.GANTRY_HOR_ACCELERATION)

    cur_motor_pos= GV.motors.read_actual_position()
    while (abs(cur_motor_pos - next_pos) > 50):
        time.sleep(1)
        cur_motor_pos= GV.motors.read_actual_position()

    GV.horizontal_gantry_active_led = False
    GV.SM_TEXT_TO_DIAPLAY ="S2,E1 -> action2_1\n" "move X actuator to position"
    GV.next_E = 2
    

def action2_2():
    timeout = False
    # passed_time = 10 # measure the  heating time
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S2,E2 -> action2_2\n" "  goint to pause state"
        return 
    if (GV.ERROR == True  or  timeout==True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S2,E2 -> action2_2\n" "  going to erro state"
        return
        

    GV.SM_TEXT_TO_DIAPLAY ="S2,E2 -> action2_2\n"
    GV.next_E = 0


def action2_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S2,E4 -> action2_3\n" "  going to erro state"
        return         
    
    GV.SM_TEXT_TO_DIAPLAY ="S2,E4 -> action2_3"
    GV.next_E = 0
    GV. prev_S = 2


def action2_4():
    GV.SM_TEXT_TO_DIAPLAY ="S2,E4 -> action2_4"
    GV.next_E = 0

#--------------------------------------------------------------------------------------------
def action3_0():
    if (GV.PAUSE == True):
        GV.next_E = 3          
        GV.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0\n" "  going to S3/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0\n" "  going to S3/E4"
        return 
    
    GV.vertical_gantry_active_led = True

    GV.SM_TEXT_TO_DIAPLAY ="S3,E0 -> action3_0\n" + "lower Z actuator to position"
    GV.next_E = 1


def action3_1():
    timeout = False
    Done = True
    if (GV.PAUSE == True):
        GV.next_E = 3        
        GV.SM_TEXT_TO_DIAPLAY = "S3,E1 -> action3_1\n" "  going to S3/E3"
        return 
    if (GV.ERROR == True or timeout==True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S3,E1 -> action3_1\n" "  going to S3/E4"
        return    
         

    GV.motors.select_axis(HW.GANTRY_VER_AXIS_ID)
    cur_motor_pos= GV.motors.read_actual_position()    
    h_position = RECIPE["GantrytoB"]["vertical_titration_position"]
    
    GV.motors.set_POSOKLIM(1)
    abs_pos_tml = int(h_position / HW.TML_LENGTH_2_MM_VER )
    next_pos =  cur_motor_pos - abs_pos_tml
    move_speed = RECIPE['GantrytoB']['gantry_move_speed'] 
    GV.motors.move_absolute_position(next_pos, move_speed, HW.GANTRY_VER_ACCELERATION)

    cur_motor_pos= GV.motors.read_actual_position()
    while ( abs(cur_motor_pos - next_pos) > 50):
        time.sleep(1)
        cur_motor_pos= GV.motors.read_actual_position()
    GV.vertical_gantry_active_led = False




    if (Done == False):
        GV.next_E = 1
        GV.SM_TEXT_TO_DIAPLAY ="S3,E1 -> action3_1\n""   waiting for pump to reach position"
    else:
        GV.next_E = 2
        GV.SM_TEXT_TO_DIAPLAY ="S3,E1 -> action3_1\n""  go to S3/E2"


def action3_2():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0\n" "  going to S3/E4"
        return 

    GV.SM_TEXT_TO_DIAPLAY ="S3,E2 -> action3_2\n"
    GV.next_E = 0


def action3_3():
    if (GV.ERROR == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0\n" "  going to S3/E3"
        return 
    
    GV.SM_TEXT_TO_DIAPLAY ="S3,E2 -> action3_2\n" "  go to PAUSE state"
    GV. prev_S = 3
    GV.next_E = 0

def action3_4():
    # print("S3,E3 -> action3_3")
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S3,E3 -> action3_3\n" " go to ERROR state"

#----------------------------------------------------------------------------------------------
def action4_0():
    if (GV.PAUSE == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S4,E0 -> action4_0\n" "  going to S4/E5"
        return 
    if (GV.ERROR == True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = "S4,E0 -> action4_0\n" " going to S4/E6"
        return 


    GV.SM_TEXT_TO_DIAPLAY ="S4,E0 -> action4_0\n"  "Stop components and return control to GUI"
    GV.next_E = 1


def action4_1():

    if (GV.PAUSE == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1\n" " going to S4/E5"
        return 
    if (GV.ERROR == True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1\n" " going to S4/E6"
        return 


    GV.terminate_SM = True
    GV.SM_TEXT_TO_DIAPLAY ="Terminating statemachine"
    GV.next_E = 0



def action4_2():
    if (GV.ERROR == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S4,E2 -> action4_5\n" " going to Pause state"
        return         
    
    GV.next_E = 0
    GV. prev_S = 4
    GV.SM_TEXT_TO_DIAPLAY = "S4,E5 -> action4_3\n" "  going to S6/E0"


def action4_3():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S4,E3 -> action4_6\n" " going to ERROR state"


#-------------------------------------------------------------------------------------------

#--------------
def action5_0():
    if (GV.PAUSE == True):
        GV.SM_TEXT_TO_DIAPLAY ="S5,E0 -> action5_0"
        GV.next_E = 0
    else:
        GV.SM_TEXT_TO_DIAPLAY ="56,E0 -> action5_0\n" " prepare to resume workflow"
        GV.next_E = GV. prev_S
    

def action5_1():
    # print("S6,E1 -> action5_1")
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S5,E1 -> action5_1\n" "  going back to S1/E0"

def action5_2():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S5,E2 -> action5_2\n""  going back to S2/E0"

def action5_3():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S5,E3 -> action5_3\n""  going back to S3/E0"

def action5_4():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S5,E4 -> action5_4\n""  going back to S4/E0"

def action5_5():
    GV.next_E = 0
    # print("S6,E5 -> action5_5")
    GV.SM_TEXT_TO_DIAPLAY ="S5,E5 -> action5_5\n""  going to ERROR state"


#--------------
def action6_0():
    print("S6,E0 -> action6_0")
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S7,E0 -> action7_0"

