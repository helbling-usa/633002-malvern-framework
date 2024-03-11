import  numpy as np
import  general.global_vars as GV
import  hardware.config as HW
import  time
from    general.recipe import RECIPE
import  logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(levelname)s:%(message)s')
file_handler = logging.FileHandler('./logs/error.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

##-----------------   ("next STATE","FUCNCTION") --------------------------------------------------
#-------------   -------E0-------    ------E1-------  -------E2-------  -------E3-------  -------E4-------  -------E5-------  
TT = np.array([[( 1, 'action0_0'),  (0, 'None')     , (0, 'None')     , (0, 'None')     , (0, 'None')     , (0, 'None')     ],  #<---STATE0
               [( 1, 'action1_0'),  (1, 'action1_1'), (2, 'action1_2'), (6, 'action1_3'), (7, 'action1_4'), (0, 'None')     ],  #<---STATE1
               [( 2, 'action2_0'),  (2, 'action2_1'), (3, 'action2_2'), (6, 'action2_3'), (7, 'action2_4'), (0, 'None')     ],  #<---STATE2
               [( 3, 'action3_0'),  (3, 'action3_1'), (4, 'action3_2'), (6, 'action3_3'), (7, 'action3_4'), (0, 'None')     ],  #<---STATE3
               [( 4, 'action4_0'),  (4, 'action4_1'), (5, 'action4_2'), (6, 'action4_3'), (7, 'action4_4'), (0, 'None')     ],  #<---STATE4
               [( 5, 'action5_0'),  (5, 'action5_1'), (6, 'action5_2'), (7, 'action5_3'), (0, 'None')     , (0, 'None')     ],  #<---STATE5
               [( 6, 'action6_0'),  (1, 'action6_1'), (2, 'action6_2'), (3, 'action6_3'), (4, 'action6_4'), (5, 'action6_5')],  #<---STATE6
               [( 7, 'action7_0'),  (0, 'None')     , (0, 'None')     , (0, 'None')     , (0, 'None')     , (0, 'None')     ]   #<---STATE7
               ])  


def name():
    return "Startup"


state_name = {0:"S0: Initialization", 1:"S1: Gantry Z Homing", 2:"S2: Gantry X Homing", 3:"S3: Gantry X to Pos A",
              4:"S4: Gantry Z to Pos A", 5:"S5: Startup Complete", 6:"Pause", 7:"Error"}


#---------------  ACTIONS  --------------
def action0_0():    
    # #/*	Setup and initialize the axis */	
    if (GV.motors.InitAxis()==False):
        logger.error("Failed to start up the Technosoft drive")    
    logger.info("\t\tMotors are Initialized")
    AXIS_ID_01 = HW.MIXER_AXIS_ID
    AXIS_ID_02 = HW.GANTRY_HOR_AXIS_ID
    AXIS_ID_03 = HW.GANTRY_VER_AXIS_ID
    GV.motors.select_axis(AXIS_ID_03)    
    GV.motors.set_position() 
    GV.motors.set_POSOKLIM(3)    
    time.sleep(.5)
    GV.motors.select_axis(AXIS_ID_02)    
    GV.motors.set_position() 
    GV.motors.set_POSOKLIM(3)    
    time.sleep(.5)
    GV.vertical_gantry_active_led = True
    GV.SM_TEXT_TO_DIAPLAY ="Homing Gantry Vertical"
    GV.next_E = 0    


#--------------
def action1_0():
    homing_speed_ver = HW.GANTRY_VER_HOMING_SPEED / HW.TML_SPEED_2_MM_PER_SEC_VER
    ret_val = GV.motors.homing(HW.GANTRY_VER_AXIS_ID, homing_speed_ver)    
    if ret_val == False:
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY =  "Homing Error!!!\n""going to Error state"
        return 
    print('--------------homing is done')
    GV.vertical_gantry_homed_led = True
    GV.vertical_gantry_active_led = False    
    GV.SM_TEXT_TO_DIAPLAY =  "  Gantry Z Homing done\n" 
    if (GV.PAUSE == True):
        GV.next_E = 3          
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "going to Error state"
        return 
    else:
        GV.next_E = 1


def action1_1():
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY ="going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "going to Error state"
        return
    else:
        GV.next_E = 2    
        GV.SM_TEXT_TO_DIAPLAY = "  Homing completed\n"  


def action1_2():
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return     
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "going to Error state"
        return   
    else:  
        GV.horizontal_gantry_active_led = True
        GV.next_E = 0
        GV.prev_S = 1
        GV.SM_TEXT_TO_DIAPLAY ="  Gantry X Homing procedure\n"


def action1_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "going to Error state"
        return
    else:
        GV.next_E = 0
        GV. prev_S = 1
        GV.SM_TEXT_TO_DIAPLAY ="S1,E2 -> action1_2\n" "  going to PAUSE state"
    
    
def action1_4():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY = "S1,E3 -> action1_3\n" "  going to ERROR state"


#--------------    
def action2_0():
    # print('Homing Gantry Horizontal')
    homing_speed_hor = HW.GANTRY_HOR_HOMING_SPEED / HW.TML_SPEED_2_MM_PER_SEC_HOR
    ret_val = GV.motors.homing(HW.GANTRY_HOR_AXIS_ID, homing_speed_hor)
    if ret_val == False:
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "  Homing Error!!!\n" "going to Error state"
        return 
    GV.horizontal_gantry_homed_led = True
    GV.horizontal_gantry_active_led = False
    if (GV.PAUSE == True):
        GV.next_E = 3            
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "going to Error state"
        return     
    else:
        GV.next_E = 1    
        GV.SM_TEXT_TO_DIAPLAY = "  Gantry X Homing is done\n" 


def action2_1():
    if (GV.PAUSE == True):
        GV.next_E = 3           
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "going to Error state"
        return  
    else:   
        GV.next_E = 2    
        GV.SM_TEXT_TO_DIAPLAY =str1 = "  X Homing completed\n" 
    

def action2_2():
    if (GV.PAUSE == True):
        GV.next_E = 3           
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "going to Error state"
        return 
    else:    
        #preprate to  going to S3
        GV.next_E = 0    
        GV.SM_TEXT_TO_DIAPLAY ="  Gantry X to position A..."
        GV.horizontal_gantry_active_led = True


def action2_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "going to Error state"
        return  
    else:       
        # print("S2,E3 -> action2_3")
        GV.next_E = 0
        GV. prev_S = 2
        GV.SM_TEXT_TO_DIAPLAY ="going to Pause state"

def action2_4():
    # print("S2,E4 -> action2_4")
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="going to Error state"


#--------------
def action3_0():
    #check if dose signal is receved 
    fill_pos = RECIPE['Startup']['horizontal_cellfill_position']
    GV.motors.select_axis(HW.GANTRY_HOR_AXIS_ID)
    GV.motors.set_POSOKLIM(3)
    abs_pos_tml = int(fill_pos / HW.TML_LENGTH_2_MM_HOR )
    # print("=============>",fill_pos, ' = ', abs_pos_tml)    
    move_speed = RECIPE['Startup']['gantry_move_speed_hor'] / HW.TML_SPEED_2_MM_PER_SEC_HOR
    # home_speed = RECIPE['Startup']['gantry_home_timeout'] 
    GV.motors.move_absolute_position(abs_pos_tml, move_speed, HW.GANTRY_HOR_ACCELERATION)
    cur_motor_pos= GV.motors.read_actual_position()
    while (abs (cur_motor_pos - abs_pos_tml)>50):
        time.sleep(1)
        cur_motor_pos= GV.motors.read_actual_position()

    GV.horizontal_gantry_active_led = False
    if (GV.PAUSE == True):
        GV.next_E = 3          
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "going to Error state"
        return 
    else:    
        GV.next_E = 1
        GV.SM_TEXT_TO_DIAPLAY ="Gantry X reached the position"


def action3_1():
    if (GV.PAUSE == True):
        GV.next_E = 3        
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "going to Error state"
        return
    else:
        #prepare to  going to S4
        GV.next_E = 2
        GV.SM_TEXT_TO_DIAPLAY = "  Gantry X in position\n"


def action3_2():
    if (GV.PAUSE == True):
        GV.next_E = 3        
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"    
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    else:
        GV.vertical_gantry_active_led = True
        GV.next_E = 0
        GV.SM_TEXT_TO_DIAPLAY ="  Gantry Z to position \n"


def action3_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "going to Error state"
        return  
    else:   
        GV.next_E = 0
        GV. prev_S = 3
        GV.SM_TEXT_TO_DIAPLAY ="Going to Pause state"


def action3_4():
    # print("S3,E3 -> action3_3")
    GV.next_E = 0
    GV. prev_S = 3
    GV.SM_TEXT_TO_DIAPLAY ="going to Error state"


#--------------
def action4_0():
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "going to Error state"
        return 
    else:
        GV.next_E = 1
        GV.SM_TEXT_TO_DIAPLAY = "  wait for gantry Z to get to position...\n" 
 

def action4_1():
    fill_pos = RECIPE['Startup']['vertical_cellfill_position']    
    GV.motors.select_axis(HW.GANTRY_VER_AXIS_ID)
    GV.motors.set_POSOKLIM(3)
    abs_pos_tml = int(fill_pos / HW.TML_LENGTH_2_MM_VER )
    # print("=============>",fill_pos, ' = ', abs_pos_tml)
    move_speed = RECIPE['Startup']['gantry_move_speed_ver']  / HW.TML_SPEED_2_MM_PER_SEC_VER
    GV.motors.move_absolute_position(abs_pos_tml, move_speed, HW.GANTRY_VER_ACCELERATION)
    cur_motor_pos= GV.motors.read_actual_position()
    while (abs(cur_motor_pos - abs_pos_tml)>50):
        time.sleep(1)
        cur_motor_pos= GV.motors.read_actual_position()
    GV.vertical_gantry_active_led = False
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "going to Error state"
        return 
    else:    
        GV.next_E = 2
        GV.SM_TEXT_TO_DIAPLAY =" Gantry Z is in  position \n" 


def action4_2():      
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "going to Error state"
        return  
    else:
        GV.next_E = 0
        GV.SM_TEXT_TO_DIAPLAY = "Completing the Start up\n "


def action4_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "going to Error state"
        return  
    else:       
        # print("S4,E3 -> action4_3")
        GV.next_E = 0
        GV. prev_S = 4
        GV.SM_TEXT_TO_DIAPLAY = "going to Puase state"


def action4_4():
    GV.next_E = 0
    GV. prev_S = 4
    GV.SM_TEXT_TO_DIAPLAY =" going to Error state"


#-------------- 
def action5_0():
    if (GV.PAUSE == True):
        GV.next_E = 2
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to Error state"
        return
    else:         
        # experiment is complete
        GV.next_E = 1
        GV.SM_TEXT_TO_DIAPLAY = "  STATE 5: start up complete"


def action5_1():
    if (GV.PAUSE == True):
        GV.next_E = 2
        GV.SM_TEXT_TO_DIAPLAY ="going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to Error state"
        return    
    else:
        GV.terminate_SM = True
        GV.next_E = 1
        GV.SM_TEXT_TO_DIAPLAY =" start up completed\n" "  returning to the main GUI"
    

def action5_2():
    if (GV.ERROR == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to Error state"
        return  
    else:  
        GV.next_E = 0
        GV. prev_S = 5
        GV.SM_TEXT_TO_DIAPLAY ="going to Pause state"
    

def action5_3():
    # print("S5,E4 -> action5_4")
    GV.next_E = 0
    GV. prev_S = 5
    GV.SM_TEXT_TO_DIAPLAY ="going to Error satete"


#--------------
def action6_0():
    if (GV.PAUSE == True):
        GV.next_E = 0
    else:
        GV.next_E = GV. prev_S
    GV.SM_TEXT_TO_DIAPLAY ="System Paused"

def action6_1():
    # print("S6,E1 -> action6_1")
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S6,E1 -> action6_1"

def action6_2():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S6,E2 -> action6_2\n"

def action6_3():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S6,E3 -> action6_3\n"

def action6_4():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S6,E4 -> action6_4\n"

def action6_5():
    GV.next_E = 0
    # print("S6,E5 -> action6_5")
    GV.SM_TEXT_TO_DIAPLAY ="S6,E5 -> action6_5\n"


#--------------
def action7_0():
    # print("S7,E0 -> action7_0")
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="system in Error State"

#--------------
