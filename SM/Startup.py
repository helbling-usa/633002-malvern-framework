import  numpy as np
import  general.General_vars as GENERAL
import  HW
import  time
from    general.recipe import RECIPE





##-----------------   ("next STATE","FUCNCTION") --------------------------------------------------
#-------------   -------E0-------    ------E1-------  -------E2-------  -------E3-------  -------E4-------  -------E5-------  
TT = np.array([[( 1, 'action0_0'),  (0, 'None')     , (0, 'None')     , (0, 'None')     , (0, 'None')     ],  #<---STATE0
               [( 1, 'action1_0'),  (1, 'action1_1'), (2, 'action1_2'), (6, 'action1_3'), (7, 'action1_4')],  #<---STATE1
               [( 2, 'action2_0'),  (2, 'action2_1'), (3, 'action2_2'), (6, 'action2_3'), (7, 'action2_4')],  #<---STATE2
               [( 3, 'action3_0'),  (3, 'action3_1'), (4, 'action3_2'), (6, 'action3_3'), (7, 'action3_4')],  #<---STATE3
               [( 4, 'action4_0'),  (4, 'action4_1'), (5, 'action4_2'), (5, 'action4_3'), (3, 'action4_4')],  #<---STATE4
               [( 5, 'action5_0'),  (5, 'action5_1'), (6, 'action5_2'), (7, 'action5_3'), (0, 'None')     ],  #<---STATE5
               [( 6, 'action6_0'),  (1, 'action6_1'), (2, 'action6_2'), (3, 'action6_3'), (4, 'action6_4')],  #<---STATE6
               [( 7, 'action7_0'),  (0, 'None')     , (0, 'None')     , (0, 'None')     , (0, 'None')     ]   #<---STATE7
               ])  



def name():
    return "Startup"


state_name = {0:"S0: Initialization", 1:"S1: Gantry Z Homing", 2:"S2: Gantry X Homing", 3:"S3: Gantry X to Pos A",
              4:"S4: Gantry Z to Pos A", 5:"S5: Startup Complete", 6:"Pause", 7:"Error"}
#---------------  ACTIONS  --------------
def action0_0():    
    # GENERAL.pump1.pump_Zinit(HW.TIRRANT_PUMP_ADDRESS)
    # # print("\t\tPump1 initialized")
    # time.sleep(3)
    # GENERAL.pump1.pump_Zinit(HW.SAMPLE_PUMP_ADDRESS)    
    # # print("\t\tPump2 initialized")
    # time.sleep(3)
    # #/*	Setup and initialize the axis */	
    if (GENERAL.motors.InitAxis()==False):
        print("Failed to start up the Technosoft drive")    
    print("\t\tMotors are Initialized")        

    AXIS_ID_01 = HW.MIXER_AXIS_ID
    AXIS_ID_02 = HW.GANTRY_HOR_AXIS_ID
    AXIS_ID_03 = HW.GANTRY_VER_AXIS_ID
    GENERAL.motors.select_axis(AXIS_ID_03)    
    GENERAL.motors.set_position() 
    GENERAL.motors.set_POSOKLIM(1)    
    time.sleep(.5)
    GENERAL.motors.select_axis(AXIS_ID_02)    
    GENERAL.motors.set_position() 
    GENERAL.motors.set_POSOKLIM(1)    
    time.sleep(.5)
    GENERAL.vertical_gantry_active_led = True
    GENERAL.SM_TEXT_TO_DIAPLAY ="  Homing Gantry Vertical"
    GENERAL.next_E = 0    


#--------------
def action1_0():
    
    
    if (GENERAL.PAUSE == True):
        GENERAL.next_E = 3          
        GENERAL.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0\n" "  going to S1/E3"
        return 
    if (GENERAL.ERROR == True):
        GENERAL.next_E = 4
        GENERAL.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0\n" "  going to S1/E4"
        return 
    

    # print('Homing Gantry Vertical')
    ret_val = GENERAL.motors.homing(HW.GANTRY_VER_AXIS_ID)    

    if ret_val == False:
        GENERAL.next_E = 4
        GENERAL.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0\n" "  Homing Error!!!\n" "  going to S1/E4"
        return 
    GENERAL.vertical_gantry_homed_led = True
    GENERAL.vertical_gantry_active_led = False
    GENERAL.next_E = 1
    str1 = "  Gantry Z Homing done\n" "  going to S1/E1"
    # print(str1)
    GENERAL.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0\n" + str1


def action1_1():
    if (GENERAL.PAUSE == True):
        GENERAL.next_E = 3
        GENERAL.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" "  going to S1/E3"
        return 
    if (GENERAL.ERROR == True):
        GENERAL.next_E = 4
        GENERAL.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" "  going to S1/E4"
        return 
    
    GENERAL.next_E = 2
    str1 = "  Homing completed\n"  "  going to S1/E2"
    GENERAL.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" + str1


def action1_2():
    if (GENERAL.PAUSE == True):
        GENERAL.next_E = 3
        GENERAL.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" "  going to S1/E3"
        return     
    if (GENERAL.ERROR == True):
        GENERAL.next_E = 4
        GENERAL.SM_TEXT_TO_DIAPLAY = "S1,E2 -> action1_2\n" "  going to S1/E4"
        return     
    GENERAL.horizontal_gantry_active_led = True
    GENERAL.next_E = 0
    GENERAL.prev_S = 1
    GENERAL.SM_TEXT_TO_DIAPLAY ="  Gantry X Homing procedure\n"

def action1_3():
    if (GENERAL.ERROR == True):
        GENERAL.next_E = 4
        GENERAL.SM_TEXT_TO_DIAPLAY = "S1,E2 -> action1_2\n" "  going to S1/E4"
        return     
    GENERAL.next_E = 0
    GENERAL. prev_S = 1
    GENERAL.SM_TEXT_TO_DIAPLAY ="S1,E2 -> action1_2\n" "  going to PAUSE state"
    
    
def action1_4():
    GENERAL.next_E = 0
    GENERAL.SM_TEXT_TO_DIAPLAY = "S1,E3 -> action1_3\n" "  going to ERROR state"

#--------------    
def action2_0():
    if (GENERAL.PAUSE == True):
        GENERAL.next_E = 3            
        GENERAL.SM_TEXT_TO_DIAPLAY = "S2,E0 -> action2_1\n" "  going to S1/E3"
        return 
    if (GENERAL.ERROR == True):
        GENERAL.next_E = 4
        GENERAL.SM_TEXT_TO_DIAPLAY = "S2,E0 -> action2_1\n" "  going to S1/E4"
        return     
    
    # print('Homing Gantry Horizontal')
    ret_val = GENERAL.motors.homing(HW.GANTRY_HOR_AXIS_ID)
    if ret_val == False:
        GENERAL.next_E = 4
        GENERAL.SM_TEXT_TO_DIAPLAY = "S2,E0 -> action2_0\n" "  Homing Error!!!\n" "  going to S2/E4"
        return 
    GENERAL.horizontal_gantry_homed_led = True
    GENERAL.horizontal_gantry_active_led = False

    GENERAL.next_E = 1
    str1 = "  Gantry X Homing is done\n" "  going to S2/E1"
    GENERAL.SM_TEXT_TO_DIAPLAY ="S2,E0 -> action2_0\n" +str1

def action2_1():
    if (GENERAL.PAUSE == True):
        GENERAL.next_E = 3           
        GENERAL.SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1\n" "  going to S1/E3"
        return 
    if (GENERAL.ERROR == True):
        GENERAL.next_E = 4
        GENERAL.SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1\n" "  going to S1/E4"
        return 
    
    GENERAL.next_E = 2
    str1 = "  X Homing completed\n"  "  going to S2/E2"    
    GENERAL.SM_TEXT_TO_DIAPLAY ="S2,E1 -> action2_1\n" + str1
    
def action2_2():
    #preprate to  going to S3
    GENERAL.next_E = 0    
    GENERAL.SM_TEXT_TO_DIAPLAY ="S2,E2 -> action2_2\n" "  Gantry X to position A..."

def action2_3():
    if (GENERAL.ERROR == True):
        GENERAL.next_E = 4
        GENERAL.SM_TEXT_TO_DIAPLAY = "S2,E3 -> action2_3\n" "  going to S1/E4"
        return         
    # print("S2,E3 -> action2_3")
    GENERAL.horizontal_gantry_active_led = True
    GENERAL.next_E = 0
    GENERAL. prev_S = 2
    GENERAL.SM_TEXT_TO_DIAPLAY ="S2,E3 -> action2_3\n"

def action2_4():
    # print("S2,E4 -> action2_4")
    GENERAL.next_E = 0
    GENERAL.SM_TEXT_TO_DIAPLAY ="S2,E4 -> action2_4\n"


#--------------
def action3_0():
    if (GENERAL.PAUSE == True):
        GENERAL.next_E = 3          
        GENERAL.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0\n" "  going to S1/E3"
        return 
    if (GENERAL.ERROR == True):
        GENERAL.next_E = 4
        GENERAL.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0\n" "  going to S1/E4"
        return 
    #check if dose signal is receved 
    fill_pos = RECIPE['Startup']['horizontal_cell_fill_position']
    GENERAL.motors.select_axis(HW.GANTRY_HOR_AXIS_ID)
    GENERAL.motors.set_POSOKLIM(1)
    abs_pos_tml = int(fill_pos / HW.TML_LENGTH_2_MM_HOR )
    # print("=============>",fill_pos, ' = ', abs_pos_tml)
    
    move_speed = RECIPE['Startup']['gantry_move_speed'] 
    # home_speed = RECIPE['Startup']['gantry_home_timeout'] 
    GENERAL.motors.move_absolute_position(abs_pos_tml, move_speed, HW.GANTRY_HOR_ACCELERATION)
    # if ret_val == False:
    #     GENERAL.next_E = 4
    #     GENERAL.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0\n" "  Homing Error!!!\n" "  going to S3/E4"
    #     return 

    cur_motor_pos= GENERAL.motors.read_actual_position()
    while (cur_motor_pos < abs_pos_tml-50):
        time.sleep(1)
        cur_motor_pos= GENERAL.motors.read_actual_position()

    GENERAL.horizontal_gantry_active_led = False
    GENERAL.next_E = 1
    str1 = "  Gantry X reached the position"
    GENERAL.SM_TEXT_TO_DIAPLAY ="S3,E0 -> action3_0\n"+str1

def action3_1():
    if (GENERAL.PAUSE == True):
        GENERAL.next_E = 3        
        GENERAL.SM_TEXT_TO_DIAPLAY = "S3,E1 -> action3_1\n" "  going to S1/E3"
        return 
    if (GENERAL.ERROR == True):
        GENERAL.next_E = 4
        GENERAL.SM_TEXT_TO_DIAPLAY = "S3,E1 -> action3_1\n" "  going to S1/E4"
        return         
    #prepare to  going to S4
    GENERAL.next_E = 2
    GENERAL.SM_TEXT_TO_DIAPLAY ="S3,E1 -> action3_1\n" "  Gantry X in position\n" "  going to S3/E2"

def action3_2():
    if (GENERAL.ERROR == True):
        GENERAL.next_E = 3
        GENERAL.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0\n" "  going to S1/E4"
        return 
    GENERAL.vertical_gantry_active_led = True
    GENERAL.next_E = 0
    GENERAL.SM_TEXT_TO_DIAPLAY ="S3,E2 -> action3_2\n" "  Gantry Z to position \n" "  going to S6/E0"

def action3_3():
    if (GENERAL.ERROR == True):
        GENERAL.next_E = 3
        GENERAL.SM_TEXT_TO_DIAPLAY = "S3,E3 -> action3_3\n" "  going to S3/E4"
        return 
    
    GENERAL.next_E = 0
    GENERAL.SM_TEXT_TO_DIAPLAY ="S3,E3 -> action3_3\n" "  going to S6/E0"

def action3_4():
    # print("S3,E3 -> action3_3")
    GENERAL.next_E = 0
    GENERAL. prev_S = 3
    GENERAL.SM_TEXT_TO_DIAPLAY ="S3,E3 -> action3_3\n" "  going to S7/E0"

#--------------
def action4_0():
    if (GENERAL.PAUSE == True):
        GENERAL.next_E = 3
        GENERAL.SM_TEXT_TO_DIAPLAY = "S4,E0 -> action4_0\n" "  going to S1/E3"
        return 
    if (GENERAL.ERROR == True):
        GENERAL.next_E = 4
        GENERAL.SM_TEXT_TO_DIAPLAY = "S4,E0 -> action4_0\n" "  going to S1/E4"
        return 

    fill_pos = RECIPE['Startup']['vertical_cell_fill_position']    
    GENERAL.motors.select_axis(HW.GANTRY_VER_AXIS_ID)
    GENERAL.motors.set_POSOKLIM(1)
    abs_pos_tml = int(fill_pos / HW.TML_LENGTH_2_MM_VER )
    # print("=============>",fill_pos, ' = ', abs_pos_tml)
    move_speed = RECIPE['Startup']['gantry_move_speed'] 
    GENERAL.motors.move_absolute_position(abs_pos_tml, move_speed, HW.GANTRY_VER_ACCELERATION)
    # if ret_val == False:
    #     GENERAL.next_E = 4
    #     GENERAL.SM_TEXT_TO_DIAPLAY = "S4,E0 -> action4_0\n" "  Homing Error!!!\n" "  going to S4/E4"
    #     return 
    cur_motor_pos= GENERAL.motors.read_actual_position()
    while (cur_motor_pos < abs_pos_tml-50):
        time.sleep(1)
        cur_motor_pos= GENERAL.motors.read_actual_position()
    GENERAL.vertical_gantry_active_led = False
    GENERAL.next_E = 1
    str1 = "  Gantry Z is in  position "
    GENERAL.SM_TEXT_TO_DIAPLAY ="S4,E0 -> action4_0\n" + str1


def action4_1():
    if (GENERAL.PAUSE == True):
        GENERAL.next_E = 3
        GENERAL.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1\n" "  going to S1/E3"
        return 
    if (GENERAL.ERROR == True):
        GENERAL.next_E = 4
        GENERAL.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1\n" "  going to S1/E4"
        return 

    GENERAL.next_E = 2
    str1 = "  wait for gantry Z to get to position...\n""  Gantry Z is in  position \n" "  going to S4/E2"
    GENERAL.SM_TEXT_TO_DIAPLAY ="S4,E1 -> action4_1\n"+ str1

def action4_2():
      
    if (GENERAL.PAUSE == True):
        GENERAL.next_E = 3
        GENERAL.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1\n" "  going to S1/E3"
        return 
    if (GENERAL.ERROR == True):
        GENERAL.next_E = 4
        GENERAL.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1\n" "  going to S1/E4"
        return          
  
    GENERAL.next_E = 0
    str1 = "  Completing the Start up\n " "  going to S5/E0"
    GENERAL.SM_TEXT_TO_DIAPLAY ="S4,E2 -> action4_2\n" + str1


def action4_3():
    if (GENERAL.ERROR == True):
        GENERAL.next_E = 4
        GENERAL.SM_TEXT_TO_DIAPLAY = "S4,E3 -> action4_3\n" "  going to S1/E4"
        return         
    # print("S4,E3 -> action4_3")
    GENERAL.next_E = 0
    GENERAL. prev_S = 4
    GENERAL.SM_TEXT_TO_DIAPLAY = "S4,E3 -> action4_3\n" "  going to S5/E0"


def action4_4():
    GENERAL.next_E = 0
    GENERAL. prev_S = 4
    GENERAL.SM_TEXT_TO_DIAPLAY ="S4,E4 -> action4_4\n" "  going to S7/E0"


#-------------- 
def action5_0():
    if (GENERAL.PAUSE == True):
        GENERAL.next_E = 2
        GENERAL.SM_TEXT_TO_DIAPLAY = "S5,E0 -> action5_0\n" "  going to S1/E2"
        return 
    if (GENERAL.ERROR == True):
        GENERAL.next_E = 3
        GENERAL.SM_TEXT_TO_DIAPLAY = "S5,E0 -> action5_0\n" "  going to S1/E3"
        return    
            
    # experiment is complete
    GENERAL.next_E = 1
    GENERAL.SM_TEXT_TO_DIAPLAY ="S5,E0 -> action5_0\n" "  STATE 5: start up complete"


def action5_1():
    if (GENERAL.PAUSE == True):
        GENERAL.next_E = 2
        GENERAL.SM_TEXT_TO_DIAPLAY = "S5,E1 -> action5_1\n" "  going to S1/E2"
        return 
    if (GENERAL.ERROR == True):
        GENERAL.next_E = 3
        GENERAL.SM_TEXT_TO_DIAPLAY = "S5,E1 -> action5_1\n" "  going to S1/E3"
        return 
    
    GENERAL.terminate_SM = True
    # print("S5,E1 -> action5_1")
    GENERAL.next_E = 1
    GENERAL.SM_TEXT_TO_DIAPLAY ="S5,E1 -> action5_1\n"  "  start up completed\n" "  returning to the main GUI"
    

def action5_2():
    if (GENERAL.ERROR == True):
        GENERAL.next_E = 3
        GENERAL.SM_TEXT_TO_DIAPLAY = "S5,E2 -> action5_2\n" "  going to S1/E3"
        return 
    
    GENERAL.next_E = 0
    GENERAL. prev_S = 5
    GENERAL.SM_TEXT_TO_DIAPLAY ="S5,E2 -> action5_2 \n----> going to S6/E0"
    

def action5_3():
    # print("S5,E4 -> action5_4")
    GENERAL.next_E = 0
    GENERAL. prev_S = 5
    GENERAL.SM_TEXT_TO_DIAPLAY ="S5,E3 -> action5_3\n"


#--------------
def action6_0():
    if (GENERAL.PAUSE == True):
        GENERAL.next_E = 0
    else:
        GENERAL.next_E = GENERAL. prev_S
    GENERAL.SM_TEXT_TO_DIAPLAY ="S6,E0 -> action6_0\n"

def action6_1():
    # print("S6,E1 -> action6_1")
    GENERAL.next_E = 0
    GENERAL.SM_TEXT_TO_DIAPLAY ="S6,E1 -> action6_1"

def action6_2():
    GENERAL.next_E = 0
    GENERAL.SM_TEXT_TO_DIAPLAY ="S6,E2 -> action6_2\n"

def action6_3():
    GENERAL.next_E = 0
    GENERAL.SM_TEXT_TO_DIAPLAY ="S6,E3 -> action6_3\n"

def action6_4():
    GENERAL.next_E = 0
    GENERAL.SM_TEXT_TO_DIAPLAY ="S6,E4 -> action6_4\n"

def action6_5():
    GENERAL.next_E = 0
    # print("S6,E5 -> action6_5")
    GENERAL.SM_TEXT_TO_DIAPLAY ="S6,E5 -> action6_5\n"


#--------------
def action7_0():
    print("S7,E0 -> action7_0")
    GENERAL.next_E = 0
    GENERAL.SM_TEXT_TO_DIAPLAY ="S7,E0 -> action7_0\n"

#--------------

# def execute():
#     global S_cur 
#     global Event 
#     global GENERAL.next_E 
#     global KILL_THREADS
#     global TAKE_STEP
#     global GENERAL.SM_TEXT_TO_DIAPLAY
#     global RESET
#     S_cur = Event = 0
#     print('init S:{}  init E:{}'.format(S_cur, Event))

#     while (terminate_SM == False):
#         # time.sleep(DELAY_TIME) 
#         time.sleep(.5)
#         if (TAKE_STEP == True and KILL_THREADS == False and RESET==False):
#             TAKE_STEP = False
#             S_next = TT[S_cur][Event]
#             Next_State = int(S_next[0])    
#             Next_action= S_next[1]
#             S_cur = Next_State            
#             eval(Next_action+'()')
#             Event = GENERAL.next_E 
            
#         if (KILL_THREADS == True):
#                 break
#         if (RESET == True):
#             S_cur = Event = 0
#             GENERAL.SM_TEXT_TO_DIAPLAY = "reset the SM"
#             RESET = False
#             break

#     print('SM Terminated')
#     .b_run['state']=NORMAL
#     .b_step['state']=DISABLED

#-------------------------------------------------------------
#-------------- END OF ACTIONS -------------------------------
#-------------------------------------------------------------


