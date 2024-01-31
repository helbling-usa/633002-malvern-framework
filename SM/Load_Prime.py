import numpy as np
import settings


##-----------------   ("next STATE","FUCNCTION") --------------------------------------------------
#-------------   -------E0-------    ------E1-------  -------E2-------  -------E3-------  -------E4-------  -------E5------ -------E6------- -------E7-------  -------E8-------  -------E9-------  
TT = np.array([[( 1, 'action0_0')  ,(0, 'None')      ,(0, 'None')      ,(0, 'None')       ,(0,'None')      ,(0, 'None')      , (0, 'None')     , (0, 'None')      , (0, 'None')      ],  #<---STATE0
               [( 1, 'action1_0')  ,(1, 'action1_1') ,(2, 'action1_2') ,(8 , 'action1_3'),(9 , 'action1_4'),(0, 'None')      , (0, 'None')     , (0, 'None')      , (0, 'None')      ],  #<---STATE1
               [( 2, 'action2_0')  ,(2, 'action2_1') ,(3, 'action2_2') ,(8 ,'action2_3') ,(9 ,'action2_4') ,(0, 'None')      , (0, 'None')     , (0, 'None')      , (0, 'None')      ],  #<---STATE2
               [( 3, 'action3_0')  ,(3, 'action3_1') ,(4, 'action3_2') ,(8 ,'action3_3') ,(9 ,'action3_4') ,(0, 'None')      , (0, 'None')     , (0, 'None')      , (0, 'None')      ],  #<---STATE3
               [( 4, 'action4_0')  ,(4, 'action4_1') ,(5, 'action4_2') ,(8 ,'action4_3') ,(9 ,'action4_4') ,(0, 'None')      , (0, 'None')     , (0, 'None')      , (0, 'None')      ],  #<---STATE4
               [( 5, 'action5_0')  ,(5, 'action5_1') ,(6, 'action5_2') ,(8, 'action5_3') ,(9, 'action5_4') ,(0, 'Mone')      , (0,'None')      , (0, 'None')      , (0, 'None')      ],  #<---STATE5
               [( 6, 'action6_0')  ,(6, 'action6_1') ,(6, 'action6_2') ,(6 ,'action6_3') ,(7 ,'action6_4') ,(8, 'action6_5') , (9, 'action6_6'), (0, 'None')      , (0, 'None')      ],  #<---STATE6
               [( 7, 'action7_0')  ,(7, 'action7_1') ,(8, 'action7_2') ,(9 ,'action7_3') ,(0,'None')       ,(0, 'None')      , (0, 'None')     , (0, 'None')      , (0, 'None')      ],  #<---STATE7
               [( 8,'action8_0' )  ,(1, 'action8_1') ,(2, 'action8_2') ,(3, 'action8_3' ),(4, 'action8_4' ),(5, 'action8_5' ), (6, 'action8_6' ),(7, 'action8_7' ), (9, 'action8_8') ],  #<---STATE8
               [( 9,'action9_0' )  ,(0, 'None')      ,(0, 'None')      ,(0, 'None')      ,(0, 'None')      ,(0, 'None')      , (0, 'None')     , (0, 'None')      , (0, 'None')      ]   #<---STATE9
               ])  



def name():
    return "Load_Prime"
#---------------  ACTIONS  --------------
def action0_0():
    settings.SM_TEXT_TO_DIAPLAY = "S0,E0 -> action0_0"         
    "  prepare for initialization"
    "  going to S0/E1"
    settings.next_E = 0

#--------------------------------------------
def action1_0():
    if (settings.PAUSE == True):
        settings.next_E = 3   
        settings.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0" "  goin to S1/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0" "  goin to S1/E4"
        return 
    
    settings.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0"         
    " -V1 to LinetoPump"
    " -V3 to TitrantLine"
    " -V5 to TitrantPort"
    " -V2 to LinetoPump"
    " -V4 to SampleLine"
    " -V7 to SamplePort"
    " -V8 to Air "
    " -V9 to Air"
    settings.next_E = 1


def action1_1():
    timeout = False
    Done = True #False
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1" "going to S1/E3"
        return 
    if (settings.ERROR == True or timeout == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1" "going to S1/E4"
        return 
   
    if (Done == False):
        settings.next_E = 2
        settings.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1" "  Waiting for valves to reach positions"
    else:
        settings.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1" "  Valves in Position" "going to S1/E2"
    settings.next_E = 2


def action1_2():
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S1,E2 -> action1_2" "going to S1/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S1,E2 -> action1_2" "going to S1/E4"
        return 
    
    settings.SM_TEXT_TO_DIAPLAY = "S1,E2 -> action1_2"  "  going to S2/E0"
    settings.next_E = 0


def action1_3():
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S1,E3 -> action1_3" "going to S1/E4"
        return 
    
    settings.SM_TEXT_TO_DIAPLAY = "S1,E3 -> action1_3"  "  going to PAUSE state"
    settings.next_E = 0
    settings.prev_S = 1
    
    
def action1_4():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY = "S1,E4 -> action1_4""  going to ERROR state"


#-------------------------------------------------------------------------------------------
def action2_0():
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S2,E0 -> action1_0" "going to S2/E4"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S2,E0 -> action1_0" "going to S2/E4"
        return 
    
    str1 = "  pump 1 pick up" "  pump 2 pickup"
    settings.SM_TEXT_TO_DIAPLAY ="S2,E0 -> action2_0" +str1
    settings.next_E = 1

def action2_1():
    timeout = False 
    bubble_sensor_3_triggered = True
    bubble_sensor_4_triggered = True
    if (settings.PAUSE == True):
        settings.next_E = 3           
        settings.SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1" "  goint to S2/E3"
        return 
    if (settings.ERROR == True or timeout==True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1" "  goint to S2/E4"
        return 
    
    if (bubble_sensor_3_triggered == True and bubble_sensor_4_triggered==True):        
        settings.SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1" "  bubble sensors both triggered" "  going to S2/E2"
        settings.next_E = 2
    else:
        settings.SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1" "  Waiting for bubble sensors to triggerer"
        settings.next_E = 1
    
            
def action2_2():
    if (settings.PAUSE == True):
        settings.next_E = 3           
        settings.SM_TEXT_TO_DIAPLAY = "S2,E2 -> action2_2" "  goint to S2/E3"
        return 
    if (settings.ERROR == True ):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S2,E2 -> action2_2" "  goint to S2/E4"
        return 
    
    settings.SM_TEXT_TO_DIAPLAY ="S2,E2 -> action2_2" "  go to S3/E0"
    settings.next_E = 0


def action2_3():
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S2,E3 -> action2_3" "Prepare to go to error State"
        return         

    settings.SM_TEXT_TO_DIAPLAY ="S2,E3 -> action2_3" " going to PAUSE state"
    settings.next_E = 0
    settings.prev_S = 2

def action2_4():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S2,E4 -> action2_4" "  goint to ERROR state"


#----------------------------------------------------------------
def action3_0():
    if (settings.PAUSE == True):
        settings.next_E = 3          
        settings.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0" "  goint to S2/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0" "  goint to S2/E4"
        return 

    str1 = "  V3 to Air" "  V4 to Air"
    settings.SM_TEXT_TO_DIAPLAY ="S3,E0 -> action3_0"+str1
    settings.next_E = 1


def action3_1():
    Done = True
    timeout = False
    if (settings.PAUSE == True):
        settings.next_E = 3        
        settings.SM_TEXT_TO_DIAPLAY = "S3,E1 -> action3_1" "  goint to S2/E3"
        return 
    if (settings.ERROR == True  and  timeout==True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S3,E1 -> action3_1" "  goint to S2/E4"
        return         
    
    if (Done == False):
        settings.SM_TEXT_TO_DIAPLAY ="S3,E1 -> action3_1""  wait for valves to reach position..."
        settings.next_E = 1
    else:    
        settings.SM_TEXT_TO_DIAPLAY ="S3,E1 -> action3_1" "  Valves in position" "go to S3/E2"
        settings.next_E = 2


def action3_2():
    if (settings.PAUSE == True):
        settings.next_E = 3        
        settings.SM_TEXT_TO_DIAPLAY = "S3,E2 -> action3_2" "  goint to S2/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S3,E2 -> action3_2" "  goint to S2/E4"
        return 
    
    settings.SM_TEXT_TO_DIAPLAY ="S3,E2 -> action3_2" " go to S4/E0"
    settings.next_E = 0


def action3_3():
    if (settings.ERROR == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S3,E3 -> action3_3" "  goint to S3/E4"
        return 
    
    settings.SM_TEXT_TO_DIAPLAY ="S3,E2 -> action3_2" "  go to S6/E0"
    settings.next_E = 0
    settings.prev_S = 3


def action3_4():
    settings.SM_TEXT_TO_DIAPLAY ="S3,E3 -> action3_3" " go to S7/E0"
    settings.next_E = 0
    settings.prev_S = 3
    

#---------------------------------------------------------------------------------------
def action4_0():
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S4,E0 -> action4_0" "goint to S4/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S4,E0 -> action4_0" "goint to S4/E4"
        return 

    str1 = "  pump 1 to dispense" 
    " pump 2 to dispense"
    settings.SM_TEXT_TO_DIAPLAY ="S4,E0 -> action4_0" + str1
    settings.next_E = 1


def action4_1():
    timeout = False 
    bubble_sensor_1_triggered = True
    bubble_sensor_2_triggered = True

    if (settings.PAUSE == True or timeout==True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1" "Pgoint to S4/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1" "goint to S4/E4"
        return 

    if (bubble_sensor_1_triggered == True  and  bubble_sensor_2_triggered==True):
        str1 = " bubble sensors 1&2 triggered" "  go to S4/E2"
        settings.SM_TEXT_TO_DIAPLAY ="S4,E1 -> action4_1"+ str1
        settings.next_E = 2
    else:
        settings.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1" "  waiting for bubble sensors 1&2 to trigger"
        settings.next_E = 1

def action4_2():
      
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S4,E2 -> action4_1" "goint to S4/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S4,E2 -> action4_1" "goint to S4/E4"
        return          
  
    str1 = "  prepare to go to S5" "  going to S5/E0"
    settings.SM_TEXT_TO_DIAPLAY ="S4,E2 -> action4_2" + str1
    settings.next_E = 0


def action4_3():
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S4,E3 -> action4_3" "goint to S4/E4"
        return         
    # print("S4,E3 -> action4_3")    
    settings.SM_TEXT_TO_DIAPLAY = "S4,E3 -> action4_3" "  going to PAUSE"
    settings.next_E = 0
    settings.prev_S = 4


def action4_4():    
    settings.SM_TEXT_TO_DIAPLAY ="S4,E4 -> action4_4" " going to ERROR state"
    settings.next_E = 0


#------------------------------------------------------------------------------------ 
def action5_0():
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S5,E0 -> action5_0" "  goint to S5/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S5,E0 -> action5_0" "  goint to S5/E4"
        return    

    str1 = "- V1 to LinetoPump"
    "- V3 to TitrantLine"
    "- V5 to TitrantCannula"
    "- V2 to LinetoGas"
    "- V4 to SampleLine"
    "- V7 to Cell"
    settings.SM_TEXT_TO_DIAPLAY ="S5,E0 -> action5_0" + str1
    settings.next_E = 1


def action5_1():
    Done = True
    timeout = False
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S5,E1 -> action5_1" "  goint to S5/E3"
        return 
    if (settings.ERROR == True  or timeout==True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S5,E1 -> action5_1" "  goint to S5/E4"
        return    
    
    if (Done == False):        
        settings.SM_TEXT_TO_DIAPLAY = "S5,E1 -> action5_1" "  Waiting for valve to go to positions..."
        settings.next_E = 1
    else:        
        settings.SM_TEXT_TO_DIAPLAY ="S5,E1 -> action5_1"  "  valves in position" "  going to S5/E2"
        settings.next_E = 2
    


def action5_2():
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S5,E2 -> action5_2" "  goint to S5/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S5,E2 -> action5_2" "  goint to S5/E4"
        return    
    
    settings.SM_TEXT_TO_DIAPLAY ="S5,E2 -> action5_2" "  going to S6/E0"
    settings.next_E = 0


def action5_3():
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S5,E5 -> action5_5" "   goint to S5/E4"
        return 
    
    settings.SM_TEXT_TO_DIAPLAY ="S5,E2 -> action5_2 ----> going to PAUSE state"
    settings.next_E = 0
    settings.prev_S = 5
    

def action5_4():
    settings.SM_TEXT_TO_DIAPLAY ="S5,E6 -> action5_4" " going to ERROR state"
    settings.next_E = 0


#-------------------------------------------------------------------------------
def action6_0():
    if (settings.PAUSE == True):
        settings.next_E = 5
        settings.SM_TEXT_TO_DIAPLAY = "S6,E0 -> action6_0" "goint to S6/E5"
        return 
    if (settings.ERROR == True):
        settings.next_E = 6
        settings.SM_TEXT_TO_DIAPLAY = "S6,E0 -> action6_0" "goint to S6/E6"
        return 

    str1 = "  pump 1 to dispense"
    "  pump 2 to dispense"
    settings.SM_TEXT_TO_DIAPLAY ="S6,E0 -> action6_0" + str1
    settings.next_E = 1


def action6_1():
    bubble_sensor_6_triggered = True    
    bubble_sensor_7_triggered = True    
    timeout = False
    if (settings.PAUSE == True or timeout==True):
        settings.next_E = 5
        settings.SM_TEXT_TO_DIAPLAY = "S6,E1 -> action6_1" "Pgoint to S6/E5"
        return 
    if (settings.ERROR == True):
        settings.next_E = 6
        settings.SM_TEXT_TO_DIAPLAY = "S6,E1 -> action6_1" "goint to S6/E6"
        return 

    if (bubble_sensor_6_triggered == True  and  bubble_sensor_7_triggered==True):        
        str1 = "  bubble sensors 6&7 triggered" "  go to S6/E2"
        settings.SM_TEXT_TO_DIAPLAY ="S6,E1 -> action6_1"+ str1
        settings.next_E = 2
    else:
        settings.SM_TEXT_TO_DIAPLAY = "S6,E1 -> action6_1" "  Waiting for valves to bubble sensor 6&7 to trig."
        settings.next_E = 1

def action6_2():      
    if (settings.PAUSE == True):
        settings.next_E = 5
        settings.SM_TEXT_TO_DIAPLAY = "S6,E2 -> action6_1" "goint to S6/E5"
        return 
    if (settings.ERROR == True):
        settings.next_E = 6
        settings.SM_TEXT_TO_DIAPLAY = "S6,E2 -> action6_1" "goint to S6/E6"
        return          
  
    str1 = "  pump 1 to position"  "  pump 2 to position"
    settings.SM_TEXT_TO_DIAPLAY ="S6,E2 -> action6_2" + str1
    settings.next_E = 3

def action6_3():      
    timeout = False
    Done = True
    if (settings.PAUSE == True):
        settings.next_E = 5
        settings.SM_TEXT_TO_DIAPLAY = "S6,E3 -> action6_3" "goint to S6/E5"
        return 
    if (settings.ERROR == True  or  timeout==True):
        settings.next_E = 6
        settings.SM_TEXT_TO_DIAPLAY = "S6,E3 -> action6_3" "goint to S6/E6"
        return          
  
    if (Done==True):
        str1 = "  pumps in position"
        settings.SM_TEXT_TO_DIAPLAY ="S6,E3 -> action6_3" + str1
        settings.next_E = 4
    else:
        str1 = "  waiting for pumps to get to position"
        settings.SM_TEXT_TO_DIAPLAY ="S6,E3 -> action6_3" + str1
        settings.next_E = 3

def action6_4():      
    if (settings.PAUSE == True):
        settings.next_E = 5
        settings.SM_TEXT_TO_DIAPLAY = "S6,E4 -> action6_4" "goint to S6/E5"
        return 
    if (settings.ERROR == True):
        settings.next_E = 6
        settings.SM_TEXT_TO_DIAPLAY = "S6,E4 -> action6_4" "goint to S6/E6"
        return          
  
    str1 = "  going to S7/E0"
    settings.SM_TEXT_TO_DIAPLAY ="S6,E2 -> action6_2" + str1
    settings.next_E = 0


def action6_5():
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S6,E5 -> action6_5" "goint to S6/E6"
        return         
    # print("S4,E3 -> action4_3")    
    settings.SM_TEXT_TO_DIAPLAY = "S6,E5 -> action6_5" "  going to PAUSE"
    settings.next_E = 0
    settings.prev_S = 6


def action6_6():    
    settings.SM_TEXT_TO_DIAPLAY ="S6,E6 -> action6_6" " going to ERROR state"
    settings.next_E = 0
    

#-----------------------------------------------------------------------------        

def action7_0():  
    if (settings.PAUSE == True):
        settings.next_E = 2
        settings.SM_TEXT_TO_DIAPLAY = "S7,E0 -> action7_0" "going to S7/E2"
        return 
    if (settings.ERROR == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S7,E0 -> action7_0" "going to S7/E3"
        return 
        
    str1 = "  perpare to trerminate SM" "  going to S7/E1"
    settings.SM_TEXT_TO_DIAPLAY = "S7,E0 -> action7_0" + str1
    settings.next_E = 1


def action7_1():
    
    if (settings.PAUSE == True):
        settings.next_E = 2
        settings.SM_TEXT_TO_DIAPLAY = "S7,E1 -> action7_1" "going to S7/E2"
        return 
    if (settings.ERROR == True ):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S7,E1 -> action7_1" "going to S7/E3"
        return 
    
    settings.SM_TEXT_TO_DIAPLAY = "S7,E1 -> action7_1" "  Terminating SM" 
    settings.next_E = 0
    settings.terminate_SM = True


def action7_2():
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S7,E2 -> action7_2" "going to S7/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S7,E2 -> action7_2" "going to S7/E4"
        return     
    
    settings.SM_TEXT_TO_DIAPLAY ="S7,E2 -> action7_2" "  go to PAUSE state"
    settings.next_E = 0

    
def action7_3():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY = "S7,E3 -> action7_3""  going to ERROR state"


#-----------------------------------------------------------------------------  


def action8_0():
    if (settings.ERROR == True):
        settings.next_E = 13
        settings.SM_TEXT_TO_DIAPLAY = "S8,E0 -> action8_0" "going to S8/E8"
        return    

    if (settings.PAUSE == True):
        settings.next_E = 0
    else:
        settings.next_E = settings.prev_S

    settings.SM_TEXT_TO_DIAPLAY ="S8,E0 -> action8_0"


def action8_1():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S8,E1 -> action8_1" "  going to S0/E0"

def action8_2():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S8,E2 -> action8_2" "  going to S1/E0"

def action8_3():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S8,E3 -> action8_3" "  going to S2/E0"

def action8_4():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S8,E4 -> action8_4" "  going to S3/E0"

def action8_5():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S8,E5 -> action8_5" "  going to S4/E0"

def action8_6():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S8,E6 -> action8_6"  "  going to S5/E0"
    
def action8_7():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S8,E7 -> action8_7"  "  going to S6/E0"

def action8_8():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S8,E8 -> action8_8"  "  going to S7/E0"

def action8_9():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S8,E9 -> action8_9"  "  going to S9/E0"



#--------------
def action9_0():
    print("S9,E0 -> action9_0")
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S9,E0 -> action9_0"


#-------------------------------------------------------------
#-------------- END OF ACTIONS -------------------------------
#-------------------------------------------------------------


