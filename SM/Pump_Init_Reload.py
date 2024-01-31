import numpy as np
import settings


##-----------------   ("next STATE","FUCNCTION") --------------------------------------------------
#-------------   -------E0-------    ------E1-------  -------E2-------  -------E3-------  -------E4-------  -------E5------ -------E6------- -------E7-------  -------E8-------  -------E9-------   -------E10-------  -------E11-------      -------E12-------    -------E13-------
TT = np.array([[( 0, 'action0_0')  ,(0, 'action0_1') ,(0, 'action0_2') ,(1, 'action0_3') ,(12,'action0_4') ,(13, 'action0_5'), (0, 'None')     , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')         ],  #<---STATE0
               [( 1, 'action1_0')  ,(1, 'action1_1') ,(2, 'action1_2') ,(12, 'action1_3'),(13, 'action1_4'),(0, 'None')      , (0, 'None')     , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')         ],  #<---STATE1
               [( 2, 'action2_0')  ,(2, 'action2_1') ,(3, 'action2_2') ,(12,'action2_3') ,(12,'action2_4') ,(0, 'None')      , (0, 'None')     , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')         ],  #<---STATE2
               [( 3, 'action3_0')  ,(3, 'action3_1') ,(4, 'action3_2') ,(12,'action3_3') ,(12,'action3_4') ,(0, 'None')      , (0, 'None')     , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')         ],  #<---STATE3
               [( 4, 'action4_0')  ,(4, 'action4_1') ,(5, 'action4_2') ,(12,'action4_3') ,(13,'action4_4') ,(0, 'None')      , (0, 'None')     , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')         ],  #<---STATE4
               [( 5, 'action5_0')  ,(5, 'action5_1') ,(5, 'action5_2') ,(5, 'action5_3') ,(6, 'action5_4') ,(12, 'action5_5'), (13,'action5_6'),(0, 'None')       , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')         ],  #<---STATE5
               [( 6, 'action6_0')  ,(6, 'action6_1') ,(7, 'action6_2') ,(12,'action6_3') ,(13,'action6_4') ,(0, 'None')      , (0, 'None')     , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')         ],  #<---STATE6
               [( 7, 'action7_0')  ,(7, 'action7_1') ,(8, 'action7_2') ,(12,'action7_3') ,(13,'action7_4') ,(0, 'None')      , (0, 'None')     , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')         ],  #<---STATE7
               [( 8, 'action8_0')  ,(8, 'action8_1') ,(9, 'action8_2') ,(12,'action8_3') ,(13,'action8_4') ,(0, 'None')      , (0, 'None')     , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')         ],  #<---STATE8
               [( 9, 'action9_0')  ,(9, 'action9_1') ,(10,'action9_2') ,(12,'action9_3') ,(13,'action9_4') ,(0, 'None')      , (0, 'None')     , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')         ],  #<---STATE9
               [( 10,'action10_0') ,(10,'action10_1'),(11,'action10_2'),(12,'action10_3'),(13,'action10_4'),(0, 'None')      , (0, 'None')     , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')         ],  #<---STATE10
               [( 11,'action11_0') ,(11,'action11_1'),(12,'action11_2'),(13,'action11_3'),(0, 'None')      ,(0, 'None')      , (0, 'None')     , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')         ],  #<---STATE11
               [( 12,'action12_0') ,(0, 'action12_1'),(1, 'action12_2'),(2, 'action12_3'),(3, 'action12_4'),(4, 'action12_5'),(5, 'action12_6'), (6, 'action12_7'), (7, 'action12_8'), (8, 'action12_9'), (9, 'action12_10'), (10, 'action12_11'), (11, 'action12_12'), (13, 'action12_13') ],  #<---STATE12
               [( 13,'action13_0') ,(0, 'None')      ,(0, 'None')      ,(0, 'None')      ,(0, 'None')      ,(0, 'None')      , (0, 'None')     , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')         ]   #<---STATE13
               ])  



def name():
    return "Pump_Init_Reload"
#---------------  ACTIONS  --------------
def action0_0():
    if (settings.PAUSE == True):
        settings.next_E = 4       
        settings.SM_TEXT_TO_DIAPLAY = "S0,E0 -> action0_0\n" "Prepare to go to Pause State"
        return 
    if (settings.ERROR == True):
        settings.next_E = 5
        settings.SM_TEXT_TO_DIAPLAY = "S0,E0 -> action0_0\n" "Prepare to go to error State"
        return     
    settings.SM_TEXT_TO_DIAPLAY = "S0,E0 -> action0_0\n"         
    "  prepare for initialization"
    "  going to S0/E1"
    settings.next_E = 1

def action0_1():
    if (settings.PAUSE == True):
        settings.next_E = 4       
        settings.SM_TEXT_TO_DIAPLAY = "S0,E1 -> action0_1\n" "Prepare to go to Pause State"
        return 
    if (settings.ERROR == True):
        settings.next_E = 5
        settings.SM_TEXT_TO_DIAPLAY = "S0,E1 -> action0_1\n" "Prepare to go to error State"
        return 
    settings.SM_TEXT_TO_DIAPLAY = "S0,E1 -> action0_1\n"         
    "  -V1 to LinetoPump"
    "  -V1 to LinetoPump"
    "  -V3 to TitrantLine"
    "  -V5 to Reservoirs"
    "  -V2 to LinetoPump"
    " - V4 to SampleLine"
    " - V7 to Reservoirs"
    " - V8 to Waste"
    " - V9 to Waste"
    "  goint to S0/E2"
    settings.next_E = 2

def action0_2():
    timeout = False
    Done = True #False
    if (settings.PAUSE == True):
        settings.next_E = 4       
        settings.SM_TEXT_TO_DIAPLAY = "S0,E2 -> action0_2\n" "going to S0/E4"
        return 
    if (settings.ERROR == True or timeout == True):
        settings.next_E = 5
        settings.SM_TEXT_TO_DIAPLAY = "S0,E2 -> action0_2\n" "going to S0/E5"
        return 
   
    if (Done == False):
        settings.next_E = 2
        settings.SM_TEXT_TO_DIAPLAY = "S0,E0 -> action0_2\n" "  Waiting for valves to reach positions"
    else:
        settings.SM_TEXT_TO_DIAPLAY = "S0,E0 -> action0_2\n" "  Valves in Position" "going to S0/E3"
    settings.next_E = 3


def action0_3():
    if (settings.PAUSE == True):
        settings.next_E = 4       
        settings.SM_TEXT_TO_DIAPLAY = "S0,E3 -> action0_3\n" "going to S0/E4"
        return 
    if (settings.ERROR == True):
        settings.next_E = 5
        settings.SM_TEXT_TO_DIAPLAY = "S0,E3 -> action0_3\n" "going to S0/E5"
        return 
    
    settings.SM_TEXT_TO_DIAPLAY = "S0,E3 -> action0_3\n"  "  going to S1/E0"
    settings.next_E = 0


def action0_4():
    if (settings.ERROR == True):
        settings.next_E = 5
        settings.SM_TEXT_TO_DIAPLAY = "S0,E4 -> action0_4\n" "going to S0/E5"
        return     
    settings.next_E = 0
    settings.prev_S = 0
    settings.SM_TEXT_TO_DIAPLAY ="S1,E2 -> action1_2\n\tgo to settings.PAUSE state"
    
    
def action0_5():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY = "S1,E3 -> action1_3\n\tgoing to ERROR state"


#-------------------------------------------------------------------------------------------
def action1_0():  
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0\n" "going to S1/E4"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0\n" "going to S1/E4"
        return 
        
    str1 = "  Init. Titran Pump" "  Init. Sample Pump" "  going to S1/E1"
    settings.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0\n" + str1
    settings.next_E = 1


def action1_1():
    timeout = False
    Done = True #False
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" "going to S1/E3"
        return 
    if (settings.ERROR == True or timeout==True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" "going to S1/E4"
        return 
    
    if (Done == False):        
        settings.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" "  Waiting for Pumps to initialize"
        settings.next_E = 1
    else:
        settings.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" "  Pumps initialized" "going to S1/E2"
        settings.next_E = 2


def action1_2():
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S1,E2 -> action1_2\n" "going to S1/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S1,E2 -> action1_2\n" "going to S1/E4"
        return     
    
    settings.SM_TEXT_TO_DIAPLAY ="S1,E2 -> action1_2\n" "  go to S2/E0 state"
    settings.next_E = 0

def action1_3():
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S1,E3 -> action1_3\n" "going to S1/E4"
        return     
    settings.SM_TEXT_TO_DIAPLAY ="S1,E2 -> action1_3\n\tgoing to PAUSE state"
    settings.next_E = 0
    settings.prev_S = 1
    
    
def action1_4():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY = "S1,E3 -> action1_3\n\tgoing to ERROR state"


#----------------------------------------------------------------   
def action2_0():
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S2,E0 -> action1_0\n" "going to S2/E4"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S2,E0 -> action1_0\n" "going to S2/E4"
        return 
    
    str1 = "  -V2 to P2 GastoLine"
    "  -V4 to P2 LinetoGas"
    "  -V6 to P2 V7"
    "  -V7 to P5 Reservoirs"
    "  -V8 to P5 Waste"
    "  -V1 to P3 Gas to Line"
    "  -V3 to P1 Gas to Line"
    "  -V5 to P2 Reservoirs"
    "  -V9 to P5 Waste"
    "  go to S2/E1"
    settings.SM_TEXT_TO_DIAPLAY ="S2,E0 -> action2_0\n" +str1
    settings.next_E = 1

def action2_1():
    timeout = False 
    Done = True
    if (settings.PAUSE == True):
        settings.next_E = 3           
        settings.SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1\n" "  goint to S2/E3"
        return 
    if (settings.ERROR == True or timeout==True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1\n" "  goint to S2/E4"
        return 
    
    if (Done == False):        
        settings.SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1\n" "  Waiting for valves to reach positions"
        settings.next_E = 1
    else:
        settings.SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1\n" "  Valves in position" "  going to S1/E2"
        settings.next_E = 2

    
def action2_2():
    if (settings.PAUSE == True):
        settings.next_E = 3           
        settings.SM_TEXT_TO_DIAPLAY = "S2,E2 -> action2_2\n" "  goint to S2/E3"
        return 
    if (settings.ERROR == True ):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S2,E2 -> action2_2\n" "  goint to S2/E4"
        return 
    
    settings.SM_TEXT_TO_DIAPLAY ="S2,E2 -> action2_2\n" "  go to S3/E0"
    settings.next_E = 0


def action2_3():
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S2,E3 -> action2_3\n" "Prepare to go to error State"
        return         

    settings.next_E = 0
    settings.prev_S = 2
    settings.SM_TEXT_TO_DIAPLAY ="S2,E3 -> action2_3\n" " going to PAUSE state"

def action2_4():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S2,E4 -> action2_4\n" "  goint to ERROR state"


#----------------------------------------------------------------
def action3_0():
    if (settings.PAUSE == True):
        settings.next_E = 3          
        settings.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0\n" "  goint to S2/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0\n" "  goint to S2/E4"
        return 

    str1 = "  Purge Sample and Tritrandt Valves"
    settings.SM_TEXT_TO_DIAPLAY ="S3,E0 -> action3_0\n"+str1
    settings.next_E = 1


def action3_1():
    NEXT = True
    if (settings.PAUSE == True):
        settings.next_E = 3        
        settings.SM_TEXT_TO_DIAPLAY = "S3,E1 -> action3_1\n" "  goint to S2/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S3,E1 -> action3_1\n" "  goint to S2/E4"
        return         
    
    if (NEXT == False):
        settings.SM_TEXT_TO_DIAPLAY ="S3,E1 -> action3_1\n""\t  wait for NEXT button to be pressed..."
        settings.next_E = 1
    else:    
        settings.SM_TEXT_TO_DIAPLAY ="S3,E1 -> action3_1\n""\tgo to S3/E2"
        settings.next_E = 2


def action3_2():
    if (settings.PAUSE == True):
        settings.next_E = 3        
        settings.SM_TEXT_TO_DIAPLAY = "S3,E2 -> action3_2\n" "  goint to S2/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S3,E2 -> action3_2\n" "  goint to S2/E4"
        return 
    
    settings.SM_TEXT_TO_DIAPLAY ="S3,E2 -> action3_2\n" " go to S4/E0"
    settings.next_E = 0


def action3_3():
    if (settings.ERROR == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S3,E3 -> action3_3\n" "  goint to S3/E4"
        return 
    
    settings.SM_TEXT_TO_DIAPLAY ="S3,E2 -> action3_2\n" "  go to S6/E0"
    settings.next_E = 0
    settings.prev_S = 3


def action3_4():
    settings.SM_TEXT_TO_DIAPLAY ="S3,E3 -> action3_3\n" " go to S7/E0"
    settings.next_E = 0
    settings.prev_S = 3
    

#---------------------------------------------------------------------------------------
def action4_0():
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S4,E0 -> action4_0\n" "goint to S4/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S4,E0 -> action4_0\n" "goint to S4/E4"
        return 

    str1 = "  -V1 to PumptoLine"
    "  -V3 to PumptoLine"
    "  -V5 to Reservoirs"
    "  -V9 to Water"
    "  -V6 to V7"
    "  -V2 to PumptoLine"
    "  -V4 to PumptoLine"
    "  -V7 to Reservoirs"
    "  -V8 to Water"
    settings.SM_TEXT_TO_DIAPLAY ="S4,E0 -> action4_0\n" + str1
    settings.next_E = 1


def action4_1():
    Done = True
    timeout = False
    if (settings.PAUSE == True or timeout==True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1\n" "Pgoint to S4/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1\n" "goint to S4/E4"
        return 

    if (Done == False):        
        settings.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action2_1\n" "  Waiting for valves to reach positions"
        settings.next_E = 1
    else:        
        str1 = "  Valves reached position" "  go to S4/E2"
        settings.SM_TEXT_TO_DIAPLAY ="S4,E1 -> action4_1\n"+ str1
        settings.next_E = 2

def action4_2():
      
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S4,E2 -> action4_1\n" "goint to S4/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S4,E2 -> action4_1\n" "goint to S4/E4"
        return          
  
    str1 = "  prepare to go to S5" "  going to S5/E0"
    settings.SM_TEXT_TO_DIAPLAY ="S4,E2 -> action4_2\n" + str1
    settings.next_E = 0


def action4_3():
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S4,E3 -> action4_3\n" "goint to S4/E4"
        return         
    # print("S4,E3 -> action4_3")    
    settings.SM_TEXT_TO_DIAPLAY = "S4,E3 -> action4_3\n" "  going to PAUSE"
    settings.next_E = 0
    settings.prev_S = 4


def action4_4():    
    settings.SM_TEXT_TO_DIAPLAY ="S4,E4 -> action4_4\n" " going to ERROR state"
    settings.next_E = 0
    settings.prev_S = 4


#------------------------------------------------------------------------------------ 
def action5_0():
    if (settings.PAUSE == True):
        settings.next_E = 5
        settings.SM_TEXT_TO_DIAPLAY = "S5,E0 -> action5_0\n" "  goint to S5/E5"
        return 
    if (settings.ERROR == True):
        settings.next_E = 6
        settings.SM_TEXT_TO_DIAPLAY = "S5,E0 -> action5_0\n" "  goint to S5/E6"
        return    
    
    settings.SM_TEXT_TO_DIAPLAY ="S5,E0 -> action5_0\n" "  Pump 1 dispense" "  Pump 2 dispense"
    settings.next_E = 1


def action5_1():
    Done = True
    timeout = False
    if (settings.PAUSE == True):
        settings.next_E = 5
        settings.SM_TEXT_TO_DIAPLAY = "S5,E1 -> action5_1\n" "  goint to S5/E5"
        return 
    if (settings.ERROR == True  or timeout==True):
        settings.next_E = 6
        settings.SM_TEXT_TO_DIAPLAY = "S5,E1 -> action5_1\n" "  goint to S5/E6"
        return    
    
    if (Done == False):        
        settings.SM_TEXT_TO_DIAPLAY = "S5,E1 -> action5_1\n" "  Waiting for pumps to finish dispensing..."
        settings.next_E = 1
    else:        
        settings.SM_TEXT_TO_DIAPLAY ="S5,E1 -> action5_1\n"  "  dispensing complete" "  going to S5/E2"
        settings.next_E = 2
    


def action5_2():
    if (settings.PAUSE == True):
        settings.next_E = 5
        settings.SM_TEXT_TO_DIAPLAY = "S5,E2 -> action5_2\n" "  goint to S5/E5"
        return 
    if (settings.ERROR == True):
        settings.next_E = 6
        settings.SM_TEXT_TO_DIAPLAY = "S5,E2 -> action5_2\n" "  goint to S5/E6"
        return    
    
    settings.SM_TEXT_TO_DIAPLAY ="S5,E2 -> action5_2\n" "  Pump 1 position xxx" "  Pump 2 to position xxx"
    settings.next_E = 3


def action5_3():
    Done = True
    timeout = False
    if (settings.PAUSE == True):
        settings.next_E = 5
        settings.SM_TEXT_TO_DIAPLAY = "S5,E3 -> action5_3\n" "  goint to S5/E5"
        return 
    if (settings.ERROR == True  or timeout==True):
        settings.next_E = 6
        settings.SM_TEXT_TO_DIAPLAY = "S5,E3 -> action5_3\n" "  goint to S5/E6"
        return    
    
    if (Done == False):        
        settings.SM_TEXT_TO_DIAPLAY = "S5,E3 -> action5_3\n" "  Waiting for pumps to reach positions..."
        settings.next_E = 3
    else:        
        settings.SM_TEXT_TO_DIAPLAY ="S5,E3 -> action5_3\n"  "  pumps in position" "  going to S5/E4"
        settings.next_E = 4


def action5_4():
    if (settings.PAUSE == True):
        settings.next_E = 5
        settings.SM_TEXT_TO_DIAPLAY = "S5,E4 -> action5_4\n" "  goint to S5/E5"
        return 
    if (settings.ERROR == True):
        settings.next_E = 6
        settings.SM_TEXT_TO_DIAPLAY = "S5,E4 -> action5_4\n" "  goint to S5/E6"
        return    
    
    settings.SM_TEXT_TO_DIAPLAY ="S5,E4 -> action5_4\n" "  going to S6/E0"
    settings.next_E = 0


def action5_5():
    if (settings.ERROR == True):
        settings.next_E = 6
        settings.SM_TEXT_TO_DIAPLAY = "S5,E5 -> action5_5\n" "   goint to S5/E6"
        return 
    
    settings.SM_TEXT_TO_DIAPLAY ="S5,E2 -> action5_2 \n----> going to PAUSE state"
    settings.next_E = 0
    settings.prev_S = 5
    

def action5_6():
    settings.SM_TEXT_TO_DIAPLAY ="S5,E6 -> action5_6\n"
    settings.next_E = 0
    settings.prev_S = 5


#-------------------------------------------------------------------------------
def action6_0():
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S6,E0 -> action6_0\n" "goint to S6/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S6,E0 -> action6_0\n" "goint to S6/E4"
        return 

    str1 = "  -V1 to PumptoAir"
    "  -V2 to PumptoAir"
    settings.SM_TEXT_TO_DIAPLAY ="S6,E0 -> action6_0\n" + str1
    settings.next_E = 1


def action6_1():
    Done = True
    timeout = False
    if (settings.PAUSE == True or timeout==True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S6,E1 -> action6_1\n" "Pgoint to S6/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S6,E1 -> action6_1\n" "goint to S6/E4"
        return 

    if (Done == False):        
        settings.SM_TEXT_TO_DIAPLAY = "S6,E1 -> action6_1\n" "  Waiting for valves to reach positions"
        settings.next_E = 1
    else:        
        str1 = "  Valves reached position" "  go to S6/E2"
        settings.SM_TEXT_TO_DIAPLAY ="S6,E1 -> action6_1\n"+ str1
        settings.next_E = 2

def action6_2():      
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S6,E2 -> action6_1\n" "goint to S6/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S6,E2 -> action6_1\n" "goint to S6/E4"
        return          
  
    str1 = "  prepare to go to S7" "  going to S7/E0"
    settings.SM_TEXT_TO_DIAPLAY ="S6,E2 -> action6_2\n" + str1
    settings.next_E = 0


def action6_3():
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S6,E3 -> action6_3\n" "goint to S6/E4"
        return         
    # print("S4,E3 -> action4_3")    
    settings.SM_TEXT_TO_DIAPLAY = "S6,E3 -> action6_3\n" "  going to PAUSE"
    settings.next_E = 0
    settings.prev_S = 6


def action6_4():    
    settings.SM_TEXT_TO_DIAPLAY ="S6,E4 -> action6_4\n" " going to ERROR state"
    settings.next_E = 0
    settings.prev_S = 6

#-----------------------------------------------------------------------------        
def action7_0():
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S7,E0 -> action7_0\n" "goint to S7/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S7,E0 -> action7_0\n" "goint to S7/E4"
        return 

    str1 = "  pump 1 to position xxx"
    "  pump 2 to position xxx"
    settings.SM_TEXT_TO_DIAPLAY ="S7,E0 -> action7_0\n" + str1
    settings.next_E = 1


def action7_1():
    Done = True
    timeout = False
    if (settings.PAUSE == True or timeout==True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S7,E1 -> action7_1\n" "Pgoint to S7/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S7,E1 -> action7_1\n" "goint to S7/E4"
        return 

    if (Done == False):        
        settings.SM_TEXT_TO_DIAPLAY = "S7,E1 -> action6_1\n" "  Waiting for pumps to reach positions"
        settings.next_E = 1
    else:        
        str1 = "  pumps reached position" "  go to S7/E2"
        settings.SM_TEXT_TO_DIAPLAY ="S7,E1 -> action7_1\n"+ str1
        settings.next_E = 2


def action7_2():      
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S7,E2 -> action7_1\n" "goint to S7/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S7,E2 -> action7_1\n" "goint to S7/E4"
        return          
  
    str1 = "  prepare to go to S8" "  going to S8/E0"
    settings.SM_TEXT_TO_DIAPLAY ="S7,E2 -> action7_2\n" + str1
    settings.next_E = 0


def action7_3():
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S7,E3 -> action7_3\n" "goint to S7/E4"
        return         
    # print("S4,E3 -> action4_3")    
    settings.SM_TEXT_TO_DIAPLAY = "S7,E3 -> action7_3\n" "  going to PAUSE"
    settings.next_E = 0
    settings.prev_S = 7


def action7_4():    
    settings.SM_TEXT_TO_DIAPLAY ="S7,E4 -> action7_4\n" " going to ERROR state"
    settings.next_E = 0
    settings.prev_S = 7

#-----------------------------------------------------------------------------      
def action8_0():
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S8,E0 -> action8_0\n" "goint to S8/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S8,E0 -> action8_0\n" "goint to S8/E4"
        return 

    str1 = "  sample pump: Run function NewAirSlugs"
    "  titrant pump: run function NewAirSlugs"
    settings.SM_TEXT_TO_DIAPLAY ="S8,E0 -> action8_0\n" + str1
    settings.next_E = 1


def action8_1():
    Done = True
    timeout = False
    if (settings.PAUSE == True or timeout==True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S8,E1 -> action8_1\n" "Pgoint to S8/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S8,E1 -> action8_1\n" "goint to S8/E4"
        return 

    if (Done == False):        
        settings.SM_TEXT_TO_DIAPLAY = "S8,E1 -> action8_1\n" "  Waiting for pumps to finish functions"
        settings.next_E = 1
    else:        
        str1 = "  pumps completed functions" "  go to S8/E2"
        settings.SM_TEXT_TO_DIAPLAY ="S8,E1 -> action8_1\n"+ str1
        settings.next_E = 2


def action8_2():      
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S8,E2 -> action8_1\n" "goint to S8/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S8,E2 -> action8_1\n" "goint to S8/E4"
        return          
  
    str1 = "  prepare to go to S9" "  going to S9/E0"
    settings.SM_TEXT_TO_DIAPLAY ="S9,E2 -> action9_2\n" + str1
    settings.next_E = 0


def action8_3():
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S8,E3 -> action8_3\n" "goint to S8/E4"
        return         
    # print("S4,E3 -> action4_3")    
    settings.SM_TEXT_TO_DIAPLAY = "S8,E3 -> action8_3\n" "  going to PAUSE"
    settings.next_E = 0
    settings.prev_S = 8


def action8_4():    
    settings.SM_TEXT_TO_DIAPLAY ="S8,E4 -> action8_4\n" " going to ERROR state"
    settings.next_E = 0
    settings.prev_S = 8

#-----------------------------------------------------------------------------  

def action9_0():
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S9,E0 -> action9_0\n" "goint to S9/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S9,E0 -> action9_0\n" "goint to S9/E4"
        return 

    str1 = "  V8 to Air"
    "  V9 to Air"
    settings.SM_TEXT_TO_DIAPLAY ="S9,E0 -> action9_0\n" + str1
    settings.next_E = 1


def action9_1():
    Done = True
    timeout = False
    if (settings.PAUSE == True or timeout==True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S9,E1 -> action9_1\n" "Pgoint to S9/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S9,E1 -> action9_1\n" "goint to S9/E4"
        return 

    if (Done == False):        
        settings.SM_TEXT_TO_DIAPLAY = "S9,E1 -> action6_1\n" "  Waiting for valves to reach positions"
        settings.next_E = 1
    else:        
        str1 = "  valves reached position" "  go to S9/E2"
        settings.SM_TEXT_TO_DIAPLAY ="S9,E1 -> action9_1\n"+ str1
        settings.next_E = 2


def action9_2():      
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S9,E2 -> action9_1\n" "goint to S9/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S9,E2 -> action9_1\n" "goint to S9/E4"
        return          
  
    str1 = "  prepare to go to S10" "  going to S10/E0"
    settings.SM_TEXT_TO_DIAPLAY ="S9,E2 -> action9_2\n" + str1
    settings.next_E = 0


def action9_3():
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S9,E3 -> action9_3\n" "goint to S9/E4"
        return         
    # print("S4,E3 -> action4_3")    
    settings.SM_TEXT_TO_DIAPLAY = "S9,E3 -> action9_3\n" "  going to PAUSE"
    settings.next_E = 0
    settings.prev_S = 9


def action9_4():    
    settings.SM_TEXT_TO_DIAPLAY ="S9,E4 -> action9_4\n" " going to ERROR state"
    settings.next_E = 0
    settings.prev_S = 9

#-----------------------------------------------------------------------------  

def action10_0():
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S10,E0 -> action10_0\n" "goint to S10/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S10,E0 -> action10_0\n" "goint to S10/E4"
        return 

    str1 = "  pump 1 pickup"
    "  pump 2 pickup"
    settings.SM_TEXT_TO_DIAPLAY ="S10,E0 -> action10_0\n" + str1
    settings.next_E = 1


def action10_1():
    Done = True
    timeout = False
    if (settings.PAUSE == True or timeout==True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S10,E1 -> action10_1\n" "Pgoint to S10/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S10,E1 -> action10_1\n" "goint to S10/E4"
        return 

    if (Done == False):        
        settings.SM_TEXT_TO_DIAPLAY = "S10,E1 -> action6_1\n" "  Waiting for bubble sensor to be triggered"
        settings.next_E = 1
    else:        
        str1 = "  bubble sensor triggered" "  pumps stopped" "  go to S10/E2"
        settings.SM_TEXT_TO_DIAPLAY ="S10,E1 -> action10_1\n"+ str1
        settings.next_E = 2


def action10_2():      
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S10,E2 -> action10_1\n" "goint to S10/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S10,E2 -> action10_1\n" "goint to S10/E4"
        return          
  
    str1 = "  prepare to go to S11" "  going to S11/E0"
    settings.SM_TEXT_TO_DIAPLAY ="S10,E2 -> action10_2\n" + str1
    settings.next_E = 0


def action10_3():
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S10,E3 -> action10_3\n" "goint to S10/E4"
        return         
    # print("S4,E3 -> action4_3")    
    settings.SM_TEXT_TO_DIAPLAY = "S10,E3 -> action10_3\n" "  going to PAUSE"
    settings.next_E = 0
    settings.prev_S = 10


def action10_4():    
    settings.SM_TEXT_TO_DIAPLAY ="S10,E4 -> action10_4\n" " going to ERROR state"
    settings.next_E = 0
    settings.prev_S = 10

#-------------------------------------------------------------------------------------------
def action11_0():  
    if (settings.PAUSE == True):
        settings.next_E = 2
        settings.SM_TEXT_TO_DIAPLAY = "S11,E0 -> action11_0\n" "going to S11/E2"
        return 
    if (settings.ERROR == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S11,E0 -> action11_0\n" "going to S11/E3"
        return 
        
    str1 = "  Pump init & reload completed" "  going to S11/E1"
    settings.SM_TEXT_TO_DIAPLAY = "S11,E0 -> action11_0\n" + str1
    settings.next_E = 1


def action11_1():
    
    if (settings.PAUSE == True):
        settings.next_E = 2
        settings.SM_TEXT_TO_DIAPLAY = "S11,E1 -> action11_1\n" "going to S11/E2"
        return 
    if (settings.ERROR == True ):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S11,E1 -> action11_1\n" "going to S11/E3"
        return 
    
    settings.SM_TEXT_TO_DIAPLAY = "S11,E1 -> action11_1\n" "  Pumps initialized" "going to S11/E2"
    settings.next_E = 0
    settings.terminate_SM = True


def action11_2():
    if (settings.PAUSE == True):
        settings.next_E = 3
        settings.SM_TEXT_TO_DIAPLAY = "S11,E2 -> action11_2\n" "going to S11/E3"
        return 
    if (settings.ERROR == True):
        settings.next_E = 4
        settings.SM_TEXT_TO_DIAPLAY = "S11,E2 -> action11_2\n" "going to S11/E4"
        return     
    
    settings.SM_TEXT_TO_DIAPLAY ="S11,E2 -> action11_2\n" "  go to S2/E0 state"
    settings.next_E = 0

    
def action11_3():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY = "S11,E3 -> action11_3\n\tgoing to ERROR state"


#-----------------------------------------------------------------------------  


def action12_0():
    if (settings.ERROR == True):
        settings.next_E = 13
        settings.SM_TEXT_TO_DIAPLAY = "S12,E0 -> action12_0\n" "going to S12/E13"
        return    

    if (settings.PAUSE == True):
        settings.next_E = 0
    else:
        settings.next_E = settings.prev_S

    settings.SM_TEXT_TO_DIAPLAY ="S12,E0 -> action12_0\n"


def action12_1():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S12,E1 -> action12_1" "  going to S0/E0"

def action12_2():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S12,E2 -> action12_2" "  going to S1/E0"

def action12_3():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S12,E3 -> action12_3" "  going to S2/E0"

def action12_4():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S12,E4 -> action12_4" "  going to S3/E0"

def action12_5():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S12,E5 -> action12_5" "  going to S4/E0"

def action12_6():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S12,E6 -> action12_6"  "  going to S5/E0"
    
def action12_7():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S12,E7 -> action12_7"  "  going to S6/E0"

def action12_8():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S12,E8 -> action12_8"  "  going to S7/E0"

def action12_9():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S12,E9 -> action12_9"  "  going to S8/E0"

def action12_10():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S12,E10 -> action12_10"  "  going to S9/E0"

def action12_11():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S12,E11 -> action12_11"  "  going to S10/E0"
def action12_11():
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S12,E11 -> action12_11"  "  going to S11/E0"


#--------------
def action13_0():
    print("S13,E0 -> action13_0")
    settings.next_E = 0
    settings.SM_TEXT_TO_DIAPLAY ="S13,E0 -> action13_0\n"


#-------------------------------------------------------------
#-------------- END OF ACTIONS -------------------------------
#-------------------------------------------------------------


