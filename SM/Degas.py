
import numpy as np
import settings


##-----------------   ("next STATE","FUCNCTION") --------------------------------------------------
#-------------   -------E0-------    ------E1-------  -------E2-------  -------E3-------  -------E4-------  -------E5-------  
TT = np.array([[( 1, 'action0_0'),  (0, 'None')     , (0, 'None')     , (0, 'None')     , (0, 'None')     , (0, 'None')     , (0, 'None')     ],  #<---STATE0
               [( 1, 'action1_0'),  (1, 'action1_1'), (2, 'action1_2'), (6, 'action1_3'), (7, 'action1_4'), (0, 'None')     , (0, 'None')     ],  #<---STATE1
               [( 2, 'action2_0'),  (2, 'action2_1'), (2, 'action2_2'), (3, 'action2_3'), (6, 'action2_4'), (7, 'action2_5'), (0, 'None')     ],  #<---STATE2
               [( 3, 'action3_0'),  (3, 'action3_1'), (4, 'action3_2'), (6, 'action3_3'), (7, 'action3_4'), (0, 'None')     , (0, 'None')     ],  #<---STATE3
               [( 4, 'action4_0'),  (4, 'action4_1'), (4, 'action4_2'), (2, 'action4_3'), (5, 'action4_4'), (6, 'action4_5'), (7, 'action4_6')],  #<---STATE4
               [( 5, 'action5_0'),  (5, 'action5_1'), (5, 'action5_2'), (6, 'action5_3'), (7, 'action5_3'), (0, 'None')     , (0, 'None')     ],  #<---STATE5
               [( 6, 'action6_0'),  (1, 'action6_1'), (2, 'action6_2'), (3, 'action6_3'), (4, 'action6_4'), (5, 'action6_5'), (7, 'action6_6')],  #<---STATE6
               [( 7, 'action7_0'),  (0, 'None')     , (0, 'None')     , (0, 'None')     , (0, 'None')     , (0, 'None')     , (0, 'None')     ]   #<---STATE7
               ])


def name():
    return "Degas"
#---------------  ACTIONS  --------------
def action0_0():
    settings.SM_TEXT_TO_DIAPLAY = "S0,E0 -> action0_0"
    "  Aspirationcount = 0"
    "  SM initialized ..."
    settings.next_E = 0    


#--------------
def action1_0():
    if (settings.PAUSE == True):
        settings.next_E = 3          
        settings.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0" "Prepare to go to Pause State"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0" "Prepare to go to error State"
        return 
    
    str1 = "  -V1 to LinetoPump"
    "  -V3 to TitrantLine"
    "  -V5 to TitrantPort"
    "  -V2 to LinetoGas"
    "  -V4 to SampleLine"
    "  -V7 to SamplePort"
    "  go to S1/E1"
    settings.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0" + str1
    settings.next_E = 1


def action1_1():
    timeout = False
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1" "go to S1/E3"
        return 
    if (settings.ERROR == True or timeout==True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1" "go to S1/E4"
        return 
    
    str1 = "  Valves in position"  "  go to S1/E2"
    settings.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1" + str1
    settings.next_E = 2

def action1_2():
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S1,E2 -> action1_2" "go to S1/E3"
        return     
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S1,E2 -> action1_2" "go to S1/E4"
        return     
    settings.SM_TEXT_TO_DIAPLAY ="S1,E2 -> action1_2" "  go to S2/E0 state"
    settings.next_E = 0

def action1_3():
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S1,E3 -> action1_3" "  go to S1/E4"
        return     
    
    settings.SM_TEXT_TO_DIAPLAY ="S1,E2 -> action1_2"  "  go to PAUSE state"
    settings.next_E = 0
    settings. prev_S = 1
    
    
def action1_4():
    settings.SM_TEXT_TO_DIAPLAY = "S1,E4 -> action1_4" "  go to ERROR state"
    settings.next_E = 0

#------------------------------------------------------------------------------------------------
def action2_0():
    if (settings.PAUSE == True):
        settings.next_E = 4        
        settings.SM_TEXT_TO_DIAPLAY = "S2,E0 -> action2_1" "  going to S2/E4"
        return 
    if (settings.ERROR == True):
        settings.next_E = 5
        settings.SM_TEXT_TO_DIAPLAY = "S2,E0 -> action2_1" "  going to S2/E5"
        return 
    
    str1 = "  set TEC to temp" "  going to S2/E1"
    settings.SM_TEXT_TO_DIAPLAY ="S2,E0 -> action2_0" +str1
    settings.next_E = 1

def action2_1():
    timeout = False
    if (settings.PAUSE == True):
        settings.next_E = 4        
        settings.SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1" "  going to S2/E4"
        return 
    if (settings.ERROR == True  or  timeout==True):
        settings.next_E = 5
        settings.SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1" "  going to S2/E5"
        return 
    
    settings.next_E = 2
    str1 = "  TEC temp is set"  "  go to S2/E2"    
    settings.SM_TEXT_TO_DIAPLAY ="S2,E1 -> action2_1" + str1
    
def action2_2():
    timeout = False
    passed_time = 10 # measure the  heating time
    if (settings.PAUSE == True):
        settings.next_E = 4        
        settings.SM_TEXT_TO_DIAPLAY = "S2,E2 -> action2_2" "  going to S2/E4"
        return 
    if (settings.ERROR == True  or  timeout==True):
        settings.next_E = 5
        settings.SM_TEXT_TO_DIAPLAY = "S2,E2 -> action2_2" "  going to S2/E5"
        return
        
    if (passed_time < settings.heat_time):
        settings.SM_TEXT_TO_DIAPLAY ="S2,E2 -> action2_2" "  witing to reach. heat time .."
        settings.next_E = 2
    else:
        settings.SM_TEXT_TO_DIAPLAY ="S2,E2 -> action2_2" "  Heat time reached"  "  go to S3/E0"
        settings.next_E = 3

def action2_3():
    if (settings.PAUSE == True):
        settings.next_E = 4        
        settings.SM_TEXT_TO_DIAPLAY = "S2,E3 -> action2_3" "  going to S2/E4"
        return 
    if (settings.ERROR == True):
        settings.next_E = 5
        settings.SM_TEXT_TO_DIAPLAY = "S2,E3 -> action2_3" "  going to S2/E5"
        return
    
    settings.SM_TEXT_TO_DIAPLAY ="S2,E3 -> action2_3" "  going to S3/E0"
    settings.next_E = 0


def action2_4():
    if (settings.ERROR == True):
        settings.next_E = 5
        settings.SM_TEXT_TO_DIAPLAY = "S2,E4 -> action2_4" "  going to S2/E5"
        return         
    
    settings.SM_TEXT_TO_DIAPLAY ="S2,E4 -> action2_4"
    settings.next_E = 0
    settings. prev_S = 2


def action2_5():
    settings.SM_TEXT_TO_DIAPLAY ="S2,E5 -> action2_5"
    settings.next_E = 0

#--------------------------------------------------------------------------------------------
def action3_0():
    if (settings.PAUSE == True):
        settings.next_E = 3          
        settings.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0" "  going to S3/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0" "  going to S3/E4"
        return 
    #check if dose signal is receved 
    settings.next_E = 1
    str1 = "  pump 1 pickup Var.: Tit. Vol. +Asp. Overshoot"
    "  pump 2 pickup Var.: Sample Vol. +Asp. Overshoot"
    settings.SM_TEXT_TO_DIAPLAY ="S3,E0 -> action3_0" + str1

def action3_1():
    timeout = False
    Done = True
    if (settings.PAUSE == True):
        settings.next_E = 3        
        settings.SM_TEXT_TO_DIAPLAY = "S3,E1 -> action3_1" "  going to S3/E3"
        return 
    if (settings.ERROR == True or timeout==True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S3,E1 -> action3_1" "  going to S3/E4"
        return    
         
    if (Done == False):
        settings.next_E = 1
        settings.SM_TEXT_TO_DIAPLAY ="S3,E1 -> action3_1""   waiting for pump to reach position"
    else:
        settings.next_E = 2
        settings.SM_TEXT_TO_DIAPLAY ="S3,E1 -> action3_1""  go to S3/E2"


def action3_2():
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0" "  going to S3/E4"
        return 
    
    settings.SM_TEXT_TO_DIAPLAY ="S3,E2 -> action3_2" " go to S4/E0"
    settings.next_E = 0

def action3_3():
    if (settings.ERROR == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0" "  going to S3/E3"
        return 
    
    settings.SM_TEXT_TO_DIAPLAY ="S3,E2 -> action3_2" "  go to PAUSE state"
    settings. prev_S = 3
    settings.next_E = 0

def action3_4():
    # print("S3,E3 -> action3_3")
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S3,E3 -> action3_3" " go to ERROR state"

#----------------------------------------------------------------------------------------------
def action4_0():
    if (settings.PAUSE == True):
        settings.next_E = 5
        settings.SM_TEXT_TO_DIAPLAY = "S4,E0 -> action4_0" "  going to S4/E5"
        return 
    if (settings.ERROR == True):
        settings.next_E = 6
        settings.SM_TEXT_TO_DIAPLAY = "S4,E0 -> action4_0" " going to S4/E6"
        return 

    str1 =  "  pump 1 dispense Var.: Tit. Vol. +Asp. Overshoot"
    "  pump 2 dispense Var.: Sample Vol. +Asp. Overshoot"
    settings.SM_TEXT_TO_DIAPLAY ="S4,E0 -> action4_0" + str1
    settings.next_E = 1


def action4_1():
    timeout = False
    Done = True
    if (settings.PAUSE == True):
        settings.next_E = 5
        settings.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1" " going to S4/E5"
        return 
    if (settings.ERROR == True or timeout==True):
        settings.next_E = 6
        settings.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1" " going to S4/E6"
        return 

    if (Done == False):
        settings.SM_TEXT_TO_DIAPLAY ="S4,E1 -> action4_1""   waiting for pump to reach position"
        settings.next_E = 1
    else:
        str1 = "  pumps in  position..." "  go to S4/E2"
        settings.SM_TEXT_TO_DIAPLAY ="S4,E1 -> action4_1"+ str1
        settings.next_E = 2

def action4_2():
    settings.current_Aspiration_count += 1
      
    if (settings.PAUSE == True):
        settings.next_E = 5
        settings.SM_TEXT_TO_DIAPLAY = "S4,E2 -> action4_2" " going to S4/E5"
        return 
    if (settings.ERROR == True):
        settings.next_E = 6
        settings.SM_TEXT_TO_DIAPLAY = "S4,E2 -> action4_2" " going to S4/E6"
        return          
  
    str0 = "current # Aspiration:{}  Total Aspirations:{}".format(settings.current_Aspiration_count, settings.total_Aspiration_count)
    if (settings.current_Aspiration_count < settings.total_Aspiration_count):
        settings.next_E = 3
        str1 = "  aspiration count not reached yet" "  go to S4/E0"
        settings.SM_TEXT_TO_DIAPLAY ="S4,E2 -> action4_2" + str1 + str0
    else:
        settings.next_E = 4
        str1 = "  aspiratin count reached" "  go to S4/E3"
        settings.SM_TEXT_TO_DIAPLAY ="S4,E2 -> action4_2" + str1+ str0



def action4_3():
    if (settings.PAUSE == True):
        settings.next_E = 5
        settings.SM_TEXT_TO_DIAPLAY = "S4,E3 -> action4_3" "  going to S4/E5"    
    if (settings.ERROR == True):
        settings.next_E = 6
        settings.SM_TEXT_TO_DIAPLAY = "S4,E3 -> action4_3" " going to S4/E6"
        return         

    settings.SM_TEXT_TO_DIAPLAY = "S4,E3 -> action4_3" "  going back to S2/E0"
    settings.next_E = 0


def action4_4():
    if (settings.PAUSE == True):
        settings.next_E = 5
        settings.SM_TEXT_TO_DIAPLAY = "S4,E4 -> action4_4" "  going to S4/E5"
    if (settings.ERROR == True):
        settings.next_E = 6
        settings.SM_TEXT_TO_DIAPLAY = "S4,E4 -> action4_4" " going to S4/E6"
        return         

    settings.SM_TEXT_TO_DIAPLAY = "S4,E4 -> action4_4" "  going to S5/E0"
    settings.next_E = 0



def action4_5():
    if (settings.ERROR == True):
        settings.next_E = 6
        settings.SM_TEXT_TO_DIAPLAY = "S4,E5 -> action4_5" " going to S4/E6"
        return         
    
    settings.next_E = 0
    settings. prev_S = 4
    settings.SM_TEXT_TO_DIAPLAY = "S4,E5 -> action4_3" "  going to S6/E0"


def action4_6():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S4,E6 -> action4_6" " going to ERROR state"


#-------------------------------------------------------------------------------------------
def action5_0():
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S5,E0 -> action5_0" "  goint to S5/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S5,E0 -> action5_0" "  goint to S5/E4"
        return    
            
    settings.SM_TEXT_TO_DIAPLAY ="S5,E0 -> action5_0" "  set TEC to experiment temperature"
    settings.next_E = 1

def action5_1():
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S5,E1 -> action5_1" "  goint to S5/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S5,E1 -> action5_1" "  goint to S5/E4"
        return 
    
    settings.terminate_SM = True
    settings.next_E = 2
    settings.SM_TEXT_TO_DIAPLAY ="S5,E1 -> action5_1"  "  start up completed" "  returning to the main GUI"
    

def action5_2():
    if (settings.ERROR == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S5,E2 -> action5_2" "  goint to S5/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S5,E2 -> action5_2" "  goint to S5/E4"
        return 

    settings.SM_TEXT_TO_DIAPLAY ="S5,E2 -> action5_2 ----> terminate the SM"
    settings.terminate_SM = True
    settings.next_E = 0

def action5_3():
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S5,E3 -> action5_3" "  goint to S5/E4"
        return 
    
    settings.SM_TEXT_TO_DIAPLAY ="S5,E3 -> action5_3 ----> going to PAUSE state"
    settings.next_E = 0
    settings. prev_S = 5
    

def action5_3():
    settings.SM_TEXT_TO_DIAPLAY ="S5,E4 -> action5_4" "  going to ERROR state"
    settings.next_E = 0
    settings. prev_S = 5


#--------------
def action6_0():
    if (settings.PAUSE == True):
        settings.SM_TEXT_TO_DIAPLAY ="S6,E0 -> action6_0"
        settings.next_E = 0
    else:
        settings.SM_TEXT_TO_DIAPLAY ="S6,E0 -> action6_0" " prepare to resume workflow"
        settings.next_E = settings. prev_S
    

def action6_1():
    # print("S6,E1 -> action6_1")
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S6,E1 -> action6_1" "  going back to S1/E0"

def action6_2():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S6,E2 -> action6_2""  going back to S2/E0"

def action6_3():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S6,E3 -> action6_3""  going back to S3/E0"

def action6_4():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S6,E4 -> action6_4""  going back to S4/E0"

def action6_5():
    settings.next_E = 0
    # print("S6,E5 -> action6_5")
    settings.SM_TEXT_TO_DIAPLAY ="S6,E5 -> action6_5""  going back to S5/E0"

def action6_6():
    settings.next_E = 0
    # print("S6,E5 -> action6_5")
    settings.SM_TEXT_TO_DIAPLAY ="S6,E6 -> action6_6""  going to S6/E6"

#--------------
def action7_0():
    print("S7,E0 -> action7_0")
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S7,E0 -> action7_0"

