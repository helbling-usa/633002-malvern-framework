
import numpy as np
import General_vars


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



#---------------  ACTIONS  --------------
def action0_0():


    General_vars.SM_TEXT_TO_DIAPLAY = "S0,E0 -> action0_0\n"         
    "\tinitialize Pump 1\n"
    "\tinitialize Pump 2\n"
    "\tinitialize V. Gantry\n"
    "\tinitialize H. Gantry\n"
    "\tinitialize TEC Controller\n"
    "\tinitialize Labjack\n"
    "SM initialized ..."
    General_vars.next_E = 0    


#--------------
def action1_0():
    
    
    if (General_vars.PAUSE == True):
        General_vars.next_E = 3          
        General_vars.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0\n" "Prepare to go to Pause State"
        return 
    if (General_vars.ERROR == True):
        General_vars.next_E = 4
        General_vars.SM_TEXT_TO_DIAPLAY = "S1,Esettings. prev_S0 -> action1_0\n" "Prepare to go to error State"
        return 
    
    General_vars.next_E = 1
    str1 = "  Gantry Z Homing procedure" "  go to S1/E1"
    # print(str1)
    General_vars.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0\n" + str1


def action1_1():
    if (General_vars.PAUSE == True):
        General_vars.next_E = 3
        General_vars.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" "Prepare to go to Pause State"
        return 
    if (General_vars.ERROR == True):
        General_vars.next_E = 4
        General_vars.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" "Prepare to go to error State"
        return 
    
    General_vars.next_E = 2
    str1 = "  Homing completed"  "  go to S1/E2"
    General_vars.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" + str1

def action1_2():
    if (General_vars.PAUSE == True):
        General_vars.next_E = 3
        General_vars.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" "Prepare to go to Pause State"
        return     
    if (General_vars.ERROR == True):
        General_vars.next_E = 4
        General_vars.SM_TEXT_TO_DIAPLAY = "S1,E2 -> action1_2\n" "Prepare to go to error State"
        return     
    General_vars.next_E = 0
    General_vars.prev_S = 1
    General_vars.SM_TEXT_TO_DIAPLAY ="S1,E2 -> action1_2\n" "  go to S2/E0 state"

def action1_3():
    if (General_vars.ERROR == True):
        General_vars.next_E = 4
        General_vars.SM_TEXT_TO_DIAPLAY = "S1,E2 -> action1_2\n" "Prepare to go to error State"
        return     
    General_vars.next_E = 0
    General_vars. prev_S = 1
    General_vars.SM_TEXT_TO_DIAPLAY ="S1,E2 -> action1_2\n\tgo to settings.PAUSE state"
    
    
def action1_4():
    General_vars.next_E = 0
    General_vars.SM_TEXT_TO_DIAPLAY = "S1,E3 -> action1_3\n\tgoing to settings.ERROR state"

#--------------    
def action2_0():
    if (General_vars.PAUSE == True):
        General_vars.next_E = 3            
        General_vars.SM_TEXT_TO_DIAPLAY = "S2,E0 -> action2_1\n" "Prepare to go to Pause State"
        return 
    if (General_vars.ERROR == True):
        General_vars.next_E = 4
        General_vars.SM_TEXT_TO_DIAPLAY = "S2,E0 -> action2_1\n" "Prepare to go to error State"
        return 
    General_vars.next_E = 1
    str1 = "  Gantry X Homing procedure" "  go to S2/E1"
    General_vars.SM_TEXT_TO_DIAPLAY ="S2,E0 -> action2_0\n" +str1

def action2_1():
    if (General_vars.PAUSE == True):
        General_vars.next_E = 3           
        General_vars.SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1\n" "Prepare to go to Pause State"
        return 
    if (General_vars.ERROR == True):
        General_vars.next_E = 4
        General_vars.SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1\n" "Prepare to go to error State"
        return 
    
    General_vars.next_E = 2
    str1 = "  X Homing completed"  "  go to S2/E2"    
    General_vars.SM_TEXT_TO_DIAPLAY ="S2,E1 -> action2_1\n" + str1
    
def action2_2():
    #preprate to go to S3
    General_vars.next_E = 0
    General_vars.SM_TEXT_TO_DIAPLAY ="S2,E2 -> action2_2\n" "\t go to S3/E0"

def action2_3():
    if (General_vars.ERROR == True):
        General_vars.next_E = 4
        General_vars.SM_TEXT_TO_DIAPLAY = "S2,E3 -> action2_3\n" "Prepare to go to error State"
        return         
    # print("S2,E3 -> action2_3")
    General_vars.next_E = 0
    General_vars. prev_S = 2
    General_vars.SM_TEXT_TO_DIAPLAY ="S2,E3 -> action2_3\n"

def action2_4():
    # print("S2,E4 -> action2_4")
    General_vars.next_E = 0
    General_vars.SM_TEXT_TO_DIAPLAY ="S2,E4 -> action2_4\n"


#--------------
def action3_0():
    if (General_vars.PAUSE == True):
        General_vars.next_E = 3          
        General_vars.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0\n" "Prepare to go to Pause State"
        return 
    if (General_vars.ERROR == True):
        General_vars.next_E = 4
        General_vars.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0\n" "Prepare to go to error State"
        return 
    #check if dose signal is receved 
    General_vars.next_E = 1
    str1 = "  Gantry X to position A..."
    General_vars.SM_TEXT_TO_DIAPLAY ="S3,E0 -> action3_0\n"+str1

def action3_1():
    if (General_vars.PAUSE == True):
        General_vars.next_E = 3        
        General_vars.SM_TEXT_TO_DIAPLAY = "S3,E1 -> action3_1\n" "Prepare to go to Pause State"
        return 
    if (General_vars.ERROR == True):
        General_vars.next_E = 4
        General_vars.SM_TEXT_TO_DIAPLAY = "S3,E1 -> action3_1\n" "Prepare to go to error State"
        return         
    #prepare to go to S4
    General_vars.next_E = 2
    General_vars.SM_TEXT_TO_DIAPLAY ="S3,E1 -> action3_1\n""\tgo to S3/E2"

def action3_2():
    if (General_vars.ERROR == True):
        General_vars.next_E = 3
        General_vars.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0\n" "Prepare to go to error State"
        return 
    
    General_vars.next_E = 0
    General_vars.SM_TEXT_TO_DIAPLAY ="S3,E2 -> action3_2\n" " go to S6/E0"

def action3_3():
    if (General_vars.ERROR == True):
        General_vars.next_E = 3
        General_vars.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0\n" "Prepare to go to error State"
        return 
    
    General_vars.next_E = 0
    General_vars.SM_TEXT_TO_DIAPLAY ="S3,E2 -> action3_2\n" "  go to S6/E0"

def action3_4():
    # print("S3,E3 -> action3_3")
    General_vars.next_E = 0
    General_vars. prev_S = 3
    General_vars.SM_TEXT_TO_DIAPLAY ="S3,E3 -> action3_3\n" " go to S7/E0"

#--------------
def action4_0():
    if (General_vars.PAUSE == True):
        General_vars.next_E = 3
        General_vars.SM_TEXT_TO_DIAPLAY = "S4,E0 -> action4_0\n" "Prepare to go to Pause State"
        return 
    if (General_vars.ERROR == True):
        General_vars.next_E = 4
        General_vars.SM_TEXT_TO_DIAPLAY = "S4,E0 -> action4_0\n" "Prepare to go to error State"
        return 

    General_vars.next_E = 1
    str1 = "  Gantry Z to position A..."
    General_vars.SM_TEXT_TO_DIAPLAY ="S4,E0 -> action4_0\n" + str1


def action4_1():
    if (General_vars.PAUSE == True):
        General_vars.next_E = 3
        General_vars.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1\n" "Prepare to go to Pause State"
        return 
    if (General_vars.ERROR == True):
        General_vars.next_E = 4
        General_vars.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1\n" "Prepare to go to error State"
        return 

    General_vars.next_E = 2
    str1 = "  wait for gantry Z to go to position..." "  go to S4/E2"
    General_vars.SM_TEXT_TO_DIAPLAY ="S4,E1 -> action4_1\n"+ str1

def action4_2():
      
    if (General_vars.PAUSE == True):
        General_vars.next_E = 3
        General_vars.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1\n" "Prepare to go to Pause State"
        return 
    if (General_vars.ERROR == True):
        General_vars.next_E = 4
        General_vars.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1\n" "Prepare to go to error State"
        return          
  
    General_vars.next_E = 0
    str1 = "  actuator reached position" "  go to S5/E0"
    General_vars.SM_TEXT_TO_DIAPLAY ="S4,E2 -> action4_2\n" + str1


def action4_3():
    if (General_vars.ERROR == True):
        General_vars.next_E = 4
        General_vars.SM_TEXT_TO_DIAPLAY = "S4,E3 -> action4_3\n" "Prepare to go to error State"
        return         
    # print("S4,E3 -> action4_3")
    General_vars.next_E = 0
    General_vars. prev_S = 4
    General_vars.SM_TEXT_TO_DIAPLAY = "S4,E3 -> action4_3\n" "  going to S6/E0"


def action4_4():
    General_vars.next_E = 0
    General_vars. prev_S = 4
    General_vars.SM_TEXT_TO_DIAPLAY ="S4,E4 -> action4_4\n" " going to S7/E0"


#-------------- 
def action5_0():
    if (General_vars.PAUSE == True):
        General_vars.next_E = 2
        General_vars.SM_TEXT_TO_DIAPLAY = "S5,E0 -> action5_0\n" "Prepare to go to Pause State"
        return 
    if (General_vars.ERROR == True):
        General_vars.next_E = 3
        General_vars.SM_TEXT_TO_DIAPLAY = "S5,E0 -> action5_0\n" "Prepare to go to error State"
        return    
            
    # experiment is complete
    General_vars.next_E = 1
    General_vars.SM_TEXT_TO_DIAPLAY ="S5,E0 -> action5_0\n" "\tSTATE 5: start up complete"


def action5_1():
    if (General_vars.PAUSE == True):
        General_vars.next_E = 2
        General_vars.SM_TEXT_TO_DIAPLAY = "S5,E1 -> action5_1\n" "Prepare to go to Pause State"
        return 
    if (General_vars.ERROR == True):
        General_vars.next_E = 3
        General_vars.SM_TEXT_TO_DIAPLAY = "S5,E1 -> action5_1\n" "Prepare to go to error State"
        return 
    
    terminate_SM = True
    # print("S5,E1 -> action5_1")
    General_vars.next_E = 1
    General_vars.SM_TEXT_TO_DIAPLAY ="S5,E1 -> action5_1\n"  "  start up completed" "  returning to the main GUI"
    

def action5_2():
    if (General_vars.ERROR == True):
        General_vars.next_E = 3
        General_vars.SM_TEXT_TO_DIAPLAY = "S5,E2 -> action5_2\n" "Prepare to go to error State"
        return 
    
    General_vars.next_E = 0
    General_vars. prev_S = 5
    General_vars.SM_TEXT_TO_DIAPLAY ="S5,E2 -> action5_2 \n----> going to S6/E0"
    

def action5_3():
    # print("S5,E4 -> action5_4")
    General_vars.next_E = 0
    General_vars. prev_S = 5
    General_vars.SM_TEXT_TO_DIAPLAY ="S5,E3 -> action5_3\n"


#--------------
def action6_0():
    if (General_vars.PAUSE == True):
        General_vars.next_E = 0
    else:
        General_vars.next_E = General_vars. prev_S
    General_vars.SM_TEXT_TO_DIAPLAY ="S6,E0 -> action6_0\n"

def action6_1():
    # print("S6,E1 -> action6_1")
    General_vars.next_E = 0
    General_vars.SM_TEXT_TO_DIAPLAY ="S6,E1 -> action6_1"

def action6_2():
    General_vars.next_E = 0
    General_vars.SM_TEXT_TO_DIAPLAY ="S6,E2 -> action6_2\n"

def action6_3():
    General_vars.next_E = 0
    General_vars.SM_TEXT_TO_DIAPLAY ="S6,E3 -> action6_3\n"

def action6_4():
    General_vars.next_E = 0
    General_vars.SM_TEXT_TO_DIAPLAY ="S6,E4 -> action6_4\n"

def action6_5():
    General_vars.next_E = 0
    # print("S6,E5 -> action6_5")
    General_vars.SM_TEXT_TO_DIAPLAY ="S6,E5 -> action6_5\n"


#--------------
def action7_0():
    print("S7,E0 -> action7_0")
    General_vars.next_E = 0
    General_vars.SM_TEXT_TO_DIAPLAY ="S7,E0 -> action7_0\n"

#--------------

def execute():
    global KILL_THREADS
    global TAKE_STEP
    global RESET
    
    General_vars.S_cur = General_vars.Event = 0
    print('init S:{}  init E:{}'.format(General_vars.S_cur, General_vars.Event))

    while (terminate_SM == False):
        # time.sleep(DELAY_TIME) 
        time.sleep(.5)
        if (TAKE_STEP == True and KILL_THREADS == False and RESET==False):
            TAKE_STEP = False
            S_next = TT[General_vars.S_cur][General_vars.Event]
            Next_State = int(S_next[0])    
            Next_action= S_next[1]
            General_vars.S_cur = Next_State            
            eval(Next_action+'()')
            General_vars.Event = General_vars.next_E 
            
        if (KILL_THREADS == True):
                break
        if (RESET == True):
            General_vars.S_cur = General_vars.Event = 0
            General_vars.SM_TEXT_TO_DIAPLAY = "reset the SM"
            RESET = False
            break

    print('SM Terminated')
    .b_run['state']=NORMAL
    .b_step['state']=DISABLED

#-------------------------------------------------------------
#-------------- END OF ACTIONS -------------------------------
#-------------------------------------------------------------


