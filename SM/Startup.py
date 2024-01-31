import  numpy as np
import  general.General_vars as settings
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
              4:"S4: Gantry Z to Pos A", 5:"S5: Startup Complete"}
#---------------  ACTIONS  --------------
def action0_0():    
    # HW.pump1.pump_Zinit(HW.TIRRANT_PUMP_ADDRESS)
    # # print("\t\tPump1 initialized")
    # time.sleep(3)
    # HW.pump1.pump_Zinit(HW.SAMPLE_PUMP_ADDRESS)    
    # # print("\t\tPump2 initialized")
    # time.sleep(3)
    # #/*	Setup and initialize the axis */	
    if (HW.motors.InitAxis()==False):
        print("Failed to start up the Technosoft drive")    
    print("\t\tMotors are Initialized")        

    AXIS_ID_01 = HW.MIXER_AXIS_ID
    AXIS_ID_02 = HW.GANTRY_HOR_AXIS_ID
    AXIS_ID_03 = HW.GANTRY_VER_AXIS_ID
    HW.motors.select_axis(AXIS_ID_03)    
    HW.motors.set_position() 
    HW.motors.set_POSOKLIM(1)    
    time.sleep(.5)
    HW.motors.select_axis(AXIS_ID_02)    
    HW.motors.set_position() 
    HW.motors.set_POSOKLIM(1)    
    time.sleep(.5)
    # print("---------get FM VER -------------------")
    # HW.motors.get_firmware_version()
    # HW.labjack.writeRegister(50590, 15)     
    # # print("--->", HW.labjack.getAIN(0))   
    # print('\t\tlabjack initialized')        
    # # print(HW.tec.get_data())
    # print("\t\tTEC controller initialized ")
    
    HW.vertical_gantry_active_led = True
    settings.SM_TEXT_TO_DIAPLAY = "S0,E0 -> action0_0\n" "  init. Pump 1\n" "  init. Pump 2\n" "  init. V. Gantry\n"
    settings.SM_TEXT_TO_DIAPLAY += "  init. H. Gantry\n" "  init. TEC Controller\n" "  init. Labjack\n" "SM initialized ..."
    settings.next_E = 0    


#--------------
def action1_0():
    
    
    if (settings.PAUSE == True):
        settings.next_E = 3          
        settings.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0\n" "  going to S1/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0\n" "  going to S1/E4"
        return 
    

    print('Homing Gantry Vertical')
    HW.motors.homing(HW.GANTRY_VER_AXIS_ID)    

    HW.vertical_gantry_homed_led = True
    HW.vertical_gantry_active_led = False
    settings.next_E = 1
    str1 = "  Gantry Z Homing procedure\n" "  going to S1/E1"
    # print(str1)
    settings.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0\n" + str1


def action1_1():
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" "  going to S1/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" "  going to S1/E4"
        return 
    
    settings.next_E = 2
    str1 = "  Homing completed\n"  "  going to S1/E2"
    settings.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" + str1


def action1_2():
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" "  going to S1/E3"
        return     
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S1,E2 -> action1_2\n" "  going to S1/E4"
        return     
    HW.horizontal_gantry_active_led = True
    settings.next_E = 0
    settings.prev_S = 1
    settings.SM_TEXT_TO_DIAPLAY ="S1,E2 -> action1_2\n" "  going to S2/E0 state"

def action1_3():
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S1,E2 -> action1_2\n" "  going to S1/E4"
        return     
    settings.next_E = 0
    settings. prev_S = 1
    settings.SM_TEXT_TO_DIAPLAY ="S1,E2 -> action1_2\n" "  going to PAUSE state"
    
    
def action1_4():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY = "S1,E3 -> action1_3\n" "  going to ERROR state"

#--------------    
def action2_0():
    if (settings.PAUSE == True):
        settings.next_E = 3            
        settings.SM_TEXT_TO_DIAPLAY = "S2,E0 -> action2_1\n" "  going to S1/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S2,E0 -> action2_1\n" "  going to S1/E4"
        return     
    
    print('Homing Gantry Horizontal')
    HW.motors.homing(HW.GANTRY_HOR_AXIS_ID)

    HW.horizontal_gantry_homed_led = True
    HW.horizontal_gantry_active_led = False

    settings.next_E = 1
    str1 = "  Gantry X Homing procedure\n" "  going to S2/E1"
    settings.SM_TEXT_TO_DIAPLAY ="S2,E0 -> action2_0\n" +str1

def action2_1():
    if (settings.PAUSE == True):
        settings.next_E = 3           
        settings.SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1\n" "  going to S1/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1\n" "  going to S1/E4"
        return 
    
    settings.next_E = 2
    str1 = "  X Homing completed\n"  "  going to S2/E2"    
    settings.SM_TEXT_TO_DIAPLAY ="S2,E1 -> action2_1\n" + str1
    
def action2_2():
    #preprate to  going to S3
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S2,E2 -> action2_2\n" "  going to S3/E0"

def action2_3():
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S2,E3 -> action2_3\n" "  going to S1/E4"
        return         
    # print("S2,E3 -> action2_3")
    HW.horizontal_gantry_active_led = True
    settings.next_E = 0
    settings. prev_S = 2
    settings.SM_TEXT_TO_DIAPLAY ="S2,E3 -> action2_3\n"

def action2_4():
    # print("S2,E4 -> action2_4")
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S2,E4 -> action2_4\n"


#--------------
def action3_0():
    if (settings.PAUSE == True):
        settings.next_E = 3          
        settings.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0\n" "  going to S1/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0\n" "  going to S1/E4"
        return 
    #check if dose signal is receved 
    fill_pos = RECIPE['Startup']['horizontal_cell_fill_position']
    HW.motors.select_axis(HW.GANTRY_HOR_AXIS_ID)
    HW.motors.set_POSOKLIM(1)
    abs_pos_tml = int(fill_pos / HW.TML_LENGTH_2_MM_HOR )
    # print("=============>",fill_pos, ' = ', abs_pos_tml)
    
    move_speed = RECIPE['Startup']['gantry_move_speed'] 
    # home_speed = RECIPE['Startup']['gantry_home_timeout'] 
    HW.motors.move_absolute_position(abs_pos_tml, move_speed, HW.GANTRY_HOR_ACCELERATION)

    cur_motor_pos= HW.motors.read_actual_position()
    while (cur_motor_pos < abs_pos_tml-50):
        time.sleep(1)
        cur_motor_pos= HW.motors.read_actual_position()

    


    HW.horizontal_gantry_active_led = False
    settings.next_E = 1
    str1 = "  Gantry X to position A..."
    settings.SM_TEXT_TO_DIAPLAY ="S3,E0 -> action3_0\n"+str1

def action3_1():
    if (settings.PAUSE == True):
        settings.next_E = 3        
        settings.SM_TEXT_TO_DIAPLAY = "S3,E1 -> action3_1\n" "  going to S1/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S3,E1 -> action3_1\n" "  going to S1/E4"
        return         
    #prepare to  going to S4
    settings.next_E = 2
    settings.SM_TEXT_TO_DIAPLAY ="S3,E1 -> action3_1\n""  going to S3/E2"

def action3_2():
    if (settings.ERROR == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0\n" "  going to S1/E4"
        return 
    HW.vertical_gantry_active_led = True
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S3,E2 -> action3_2\n" "  going to S6/E0"

def action3_3():
    if (settings.ERROR == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0\n" "  going to S1/E4"
        return 
    
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S3,E2 -> action3_2\n" "  going to S6/E0"

def action3_4():
    # print("S3,E3 -> action3_3")
    settings.next_E = 0
    settings. prev_S = 3
    settings.SM_TEXT_TO_DIAPLAY ="S3,E3 -> action3_3\n" "  going to S7/E0"

#--------------
def action4_0():
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S4,E0 -> action4_0\n" "  going to S1/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S4,E0 -> action4_0\n" "  going to S1/E4"
        return 

    fill_pos = RECIPE['Startup']['vertical_cell_fill_position']    
    HW.motors.select_axis(HW.GANTRY_VER_AXIS_ID)
    HW.motors.set_POSOKLIM(1)
    abs_pos_tml = int(fill_pos / HW.TML_LENGTH_2_MM_VER )
    # print("=============>",fill_pos, ' = ', abs_pos_tml)
    move_speed = RECIPE['Startup']['gantry_move_speed'] 
    HW.motors.move_absolute_position(abs_pos_tml, move_speed, HW.GANTRY_VER_ACCELERATION)

    cur_motor_pos= HW.motors.read_actual_position()
    while (cur_motor_pos < abs_pos_tml-50):
        time.sleep(1)
    cur_motor_pos= HW.motors.read_actual_position()
    HW.vertical_gantry_active_led = False
    settings.next_E = 1
    str1 = "  Gantry Z to position A..."
    settings.SM_TEXT_TO_DIAPLAY ="S4,E0 -> action4_0\n" + str1


def action4_1():
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1\n" "  going to S1/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1\n" "  going to S1/E4"
        return 

    settings.next_E = 2
    str1 = "  wait for gantry Z to get to position...\n" "  going to S4/E2"
    settings.SM_TEXT_TO_DIAPLAY ="S4,E1 -> action4_1\n"+ str1

def action4_2():
      
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1\n" "  going to S1/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1\n" "  going to S1/E4"
        return          
  
    settings.next_E = 0
    str1 = "  actuator reached position\n" "  going to S5/E0"
    settings.SM_TEXT_TO_DIAPLAY ="S4,E2 -> action4_2\n" + str1


def action4_3():
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S4,E3 -> action4_3\n" "  going to S1/E4"
        return         
    # print("S4,E3 -> action4_3")
    settings.next_E = 0
    settings. prev_S = 4
    settings.SM_TEXT_TO_DIAPLAY = "S4,E3 -> action4_3\n" "  going to S6/E0"


def action4_4():
    settings.next_E = 0
    settings. prev_S = 4
    settings.SM_TEXT_TO_DIAPLAY ="S4,E4 -> action4_4\n" "  going to S7/E0"


#-------------- 
def action5_0():
    if (settings.PAUSE == True):
        settings.next_E = 2
        settings.SM_TEXT_TO_DIAPLAY = "S5,E0 -> action5_0\n" "  going to S1/E2"
        return 
    if (settings.ERROR == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S5,E0 -> action5_0\n" "  going to S1/E3"
        return    
            
    # experiment is complete
    settings.next_E = 1
    settings.SM_TEXT_TO_DIAPLAY ="S5,E0 -> action5_0\n" "  STATE 5: start up complete"


def action5_1():
    if (settings.PAUSE == True):
        settings.next_E = 2
        settings.SM_TEXT_TO_DIAPLAY = "S5,E1 -> action5_1\n" "  going to S1/E2"
        return 
    if (settings.ERROR == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S5,E1 -> action5_1\n" "  going to S1/E3"
        return 
    
    settings.terminate_SM = True
    # print("S5,E1 -> action5_1")
    settings.next_E = 1
    settings.SM_TEXT_TO_DIAPLAY ="S5,E1 -> action5_1\n"  "  start up completed\n" "  returning to the main GUI"
    

def action5_2():
    if (settings.ERROR == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S5,E2 -> action5_2\n" "  going to S1/E3"
        return 
    
    settings.next_E = 0
    settings. prev_S = 5
    settings.SM_TEXT_TO_DIAPLAY ="S5,E2 -> action5_2 \n----> going to S6/E0"
    

def action5_3():
    # print("S5,E4 -> action5_4")
    settings.next_E = 0
    settings. prev_S = 5
    settings.SM_TEXT_TO_DIAPLAY ="S5,E3 -> action5_3\n"


#--------------
def action6_0():
    if (settings.PAUSE == True):
        settings.next_E = 0
    else:
        settings.next_E = settings. prev_S
    settings.SM_TEXT_TO_DIAPLAY ="S6,E0 -> action6_0\n"

def action6_1():
    # print("S6,E1 -> action6_1")
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S6,E1 -> action6_1"

def action6_2():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S6,E2 -> action6_2\n"

def action6_3():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S6,E3 -> action6_3\n"

def action6_4():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S6,E4 -> action6_4\n"

def action6_5():
    settings.next_E = 0
    # print("S6,E5 -> action6_5")
    settings.SM_TEXT_TO_DIAPLAY ="S6,E5 -> action6_5\n"


#--------------
def action7_0():
    print("S7,E0 -> action7_0")
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S7,E0 -> action7_0\n"

#--------------

# def execute():
#     global S_cur 
#     global Event 
#     global settings.next_E 
#     global KILL_THREADS
#     global TAKE_STEP
#     global settings.SM_TEXT_TO_DIAPLAY
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
#             Event = settings.next_E 
            
#         if (KILL_THREADS == True):
#                 break
#         if (RESET == True):
#             S_cur = Event = 0
#             settings.SM_TEXT_TO_DIAPLAY = "reset the SM"
#             RESET = False
#             break

#     print('SM Terminated')
#     .b_run['state']=NORMAL
#     .b_step['state']=DISABLED

#-------------------------------------------------------------
#-------------- END OF ACTIONS -------------------------------
#-------------------------------------------------------------


