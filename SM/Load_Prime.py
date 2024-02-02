import numpy as np
import  general.global_vars as GV
import  hardware.config as HW
import  time
from    general.recipe import RECIPE

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

state_name = {0:"S0:  Initialization", 1:"S1: Load1", 2:"S2: Load2", 3:"S3: PurgeAir1", 4:"S4: PurgeAir1", 
              5:"S5: Fill1", 6:"S6: Fill2", 7:"S7: Load Prime Complete", 8:"Pause", 9:"Error"}


def air_or_liquid( voltage):
    if voltage > HW.BS_THRESHOLD:
        return 'liquid'
    else:
        return 'air'
    


#---------------  ACTIONS  --------------
def action0_0():
    str1 = " -V1 to LinetoPump\n" " -V3 to TitrantLine\n" " -V5 to TitrantPort\n" " -V2 to LinetoPump\n"
    str1 = str1 + " -V4 to SampleLine\n" " -V7 to SamplePort\n"" -V8 to Air\n" " -V9 to Air\n"
    GV.SM_TEXT_TO_DIAPLAY = str1

    GV.next_E = 0

#--------------------------------------------
def action1_0():
    if (GV.PAUSE == True):
        GV.next_E = 3   
        GV.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0" "  goin to S1/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0" "  goin to S1/E4"
        return 


    GV.pump1.set_valve(HW.TIRRANT_PUMP_ADDRESS, 'E')
    time.sleep(.5)
    GV.pump1.set_valve(HW.TITRANT_LOOP_ADDRESS, 'E')
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.TITRANT_CLEANING_ADDRESS,1)        
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.TITRANT_PIPETTE_ADDRESS,3)
    time.sleep(.5)    
    GV.pump1.set_valve(HW.SAMPLE_PUMP_ADDRESS, 'E')
    time.sleep(.5)
    # GV.pump1.set_valve(HW.SAMPLE_LOOP_ADDRESS, 'E')
    # time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.TITRANT_PORT_ADDRESS,3)
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.DEGASSER_ADDRESS,1)        
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.SAMPLE_CLEANING_ADDRESS,1)    
    time.sleep(.5)

    GV.pump1.set_speed(HW.TIRRANT_PUMP_ADDRESS,RECIPE["PumpInit_Reload"]["pump_speed"])
    time.sleep(1)
    GV.pump1.set_speed(HW.SAMPLE_PUMP_ADDRESS,RECIPE["PumpInit_Reload"]["pump_speed"])
    time.sleep(1)
    



    str1 = " -V1 to LinetoPump\n" " -V3 to TitrantLine\n" " -V5 to TitrantPort\n" " -V2 to LinetoPump\n"
    str1 = str1 + " -V4 to SampleLine\n" " -V7 to SamplePort\n"" -V8 to Air\n" " -V9 to Air\n"    
    GV.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0\n" + str1

    GV.next_E = 1


def action1_1():
    timeout = False
    Done = True #False
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" "going to S1/E3"
        return 
    if (GV.ERROR == True or timeout == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" "going to S1/E4"
        return 
   
    if (Done == False):
        GV.next_E = 2
        GV.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" "  Waiting for valves to reach positions"
    else:
        GV.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" "  Valves in Position\n" "going to S1/E2"
    GV.next_E = 2


def action1_2():
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S1,E2 -> action1_2\n" "going to S1/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S1,E2 -> action1_2\n" "going to S1/E4"
        return 
    
    GV.SM_TEXT_TO_DIAPLAY = "S1,E2 -> action1_2\n"  "  going to S2/E0"
    GV.next_E = 0


def action1_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S1,E3 -> action1_3\n" "going to S1/E4"
        return 
    
    GV.SM_TEXT_TO_DIAPLAY = "S1,E3 -> action1_3\n"  "  going to PAUSE state"
    GV.next_E = 0
    GV.prev_S = 1
    
    
def action1_4():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY = "S1,E4 -> action1_4\n""  going to ERROR state"


#-------------------------------------------------------------------------------------------
def action2_0():
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S2,E0 -> action1_0\n" "going to S2/E4"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S2,E0 -> action1_0\n" "going to S2/E4"
        return 
    
    str1 = "  pump 1 pick up\n" "  pump 2 pickup"
    GV.SM_TEXT_TO_DIAPLAY ="S2,E0 -> action2_0" +str1
    GV.next_E = 1

def action2_1():
    timeout = False 
    bubble_sensor_3_triggered = True
    bubble_sensor_4_triggered = True
    if (GV.PAUSE == True):
        GV.next_E = 3           
        GV.SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1" "  goint to S2/E3"
        return 
    if (GV.ERROR == True or timeout==True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1" "  goint to S2/E4"
        return 
    

    print('Pickup until bubble')
    GV.pump1.set_speed(HW.TIRRANT_PUMP_ADDRESS, HW.BUBBLE_DETECTION_PUMP_SPEED)
    time.sleep(1)        
    GV.pump1.set_speed(HW.SAMPLE_PUMP_ADDRESS, HW.BUBBLE_DETECTION_PUMP_SPEED)
    time.sleep(1)        
    GV.pump1.set_pos_absolute(HW.TIRRANT_PUMP_ADDRESS, HW.PICKUP_UNTIL_BUBBLE_TARGET)
    time.sleep(1)
    GV.pump1.set_pos_absolute(HW.SAMPLE_PUMP_ADDRESS, HW.PICKUP_UNTIL_BUBBLE_TARGET)
    time.sleep(1)
    input1 = GV.labjack.getAIN(2)  #bubble sensor 3
    input2 = GV.labjack.getAIN(3)   #bubble snesor 4
    #check if the bubble semsor detect air or liquid
    cur_state_1 = air_or_liquid(input1)
    cur_state_2 = air_or_liquid(input2)
    prev_state_1 = cur_state_1
    prev_state_2 = cur_state_2    
    bubble_1_search = True
    bubble_2_search = True
    
    while (bubble_1_search  or bubble_2_search) :
        input1 = GV.labjack.getAIN(0)
        cur_state_1 = air_or_liquid(input1)
        pos1 =GV.pump1.get_plunger_position(HW.TIRRANT_PUMP_ADDRESS)
        if (cur_state_1 != prev_state_1):
            bubble_1_search = False

        time.sleep(.025)
        input2 = GV.labjack.getAIN(1)
        cur_state_2 = air_or_liquid(input2)
        pos2 =GV.pump1.get_plunger_position(HW.SAMPLE_PUMP_ADDRESS)
        print('        BS1:{:.2f} position:{},   BS2:{:.2f} position:{}'.format(input1,pos1,input2, pos2))
        if (cur_state_2 != prev_state_2):
            bubble_2_search = False
        time.sleep(.025)
        
    GV.pump1.stop(HW.TIRRANT_PUMP_ADDRESS)
    time.sleep(.5)
    GV.pump1.stop(HW.SAMPLE_PUMP_ADDRESS)
    print('\t\tBubble detection terminated')
    GV.pump1.set_speed(HW.TIRRANT_PUMP_ADDRESS,HW.DEFAULT_PUMP_SPEEED)
    time.sleep(.5)
    GV.pump1.set_speed(HW.SAMPLE_PUMP_ADDRESS,HW.DEFAULT_PUMP_SPEEED)


    GV.SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1\n" "  bubble sensors both triggered\n" "  going to S2/E2\n"
    GV.next_E = 2
            
def action2_2():
    if (GV.PAUSE == True):
        GV.next_E = 3           
        GV.SM_TEXT_TO_DIAPLAY = "S2,E2 -> action2_2\n" "  goint to S2/E3"
        return 
    if (GV.ERROR == True ):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S2,E2 -> action2_2\n" "  goint to S2/E4"
        return 
    
    GV.SM_TEXT_TO_DIAPLAY ="S2,E2 -> action2_2\n" "  go to S3/E0"
    GV.next_E = 0


def action2_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S2,E3 -> action2_3\n" "Prepare to go to error State"
        return         

    GV.SM_TEXT_TO_DIAPLAY ="S2,E3 -> action2_3\n" " going to PAUSE state"
    GV.next_E = 0
    GV.prev_S = 2

def action2_4():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S2,E4 -> action2_4\n" "  goint to ERROR state"


#----------------------------------------------------------------
def action3_0():
    if (GV.PAUSE == True):
        GV.next_E = 3          
        GV.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0\n" "  goint to S2/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0\n" "  goint to S2/E4"
        return 

    str1 = "  V3 to Air\n" "  V4 to Air\n""  wait for valves to reach position..."
    GV.SM_TEXT_TO_DIAPLAY ="S3,E0 -> action3_0"+str1
    GV.next_E = 1


def action3_1():
    Done = True
    timeout = False
    if (GV.PAUSE == True):
        GV.next_E = 3        
        GV.SM_TEXT_TO_DIAPLAY = "S3,E1 -> action3_1\n" "  goint to S2/E3"
        return 
    if (GV.ERROR == True  and  timeout==True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S3,E1 -> action3_1\n" "  goint to S2/E4"
        return         

    GV.pump1.set_multiwayvalve(HW.TITRANT_CLEANING_ADDRESS,1)        
    time.sleep(.5)    
    GV.pump1.set_multiwayvalve(HW.TITRANT_PIPETTE_ADDRESS,3)
    time.sleep(.5)



    if (Done == False):
        GV.SM_TEXT_TO_DIAPLAY ="S3,E1 -> action3_1\n"
        GV.next_E = 1
    else:    
        GV.SM_TEXT_TO_DIAPLAY ="S3,E1 -> action3_1\n" "  Valves in position" "go to S3/E2"
        GV.next_E = 2


def action3_2():
    if (GV.PAUSE == True):
        GV.next_E = 3        
        GV.SM_TEXT_TO_DIAPLAY = "S3,E2 -> action3_2\n" "  goint to S2/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S3,E2 -> action3_2\n" "  goint to S2/E4"
        return 
    
    GV.SM_TEXT_TO_DIAPLAY ="S3,E2 -> action3_2\n" " go to S4/E0"
    GV.next_E = 0


def action3_3():
    if (GV.ERROR == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S3,E3 -> action3_3\n" "  goint to S3/E4"
        return 
    
    GV.SM_TEXT_TO_DIAPLAY ="S3,E2 -> action3_2\n" "  go to S6/E0"
    GV.next_E = 0
    GV.prev_S = 3


def action3_4():
    GV.SM_TEXT_TO_DIAPLAY ="S3,E3 -> action3_3\n" " go to S7/E0"
    GV.next_E = 0
    GV.prev_S = 3
    

#---------------------------------------------------------------------------------------
def action4_0():
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S4,E0 -> action4_0\n" "goint to S4/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S4,E0 -> action4_0\n" "goint to S4/E4"
        return 

    str1 = "  pump 1 to dispense\n"  " pump 2 to dispense"
    GV.SM_TEXT_TO_DIAPLAY ="S4,E0 -> action4_0\n" + str1
    GV.next_E = 1


def action4_1():
    timeout = False 
    bubble_sensor_1_triggered = True
    bubble_sensor_2_triggered = True

    if (GV.PAUSE == True or timeout==True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1" "Pgoint to S4/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1" "goint to S4/E4"
        return 


    print('Dispense until bubble')
    GV.pump1.set_speed(HW.TIRRANT_PUMP_ADDRESS, HW.BUBBLE_DETECTION_PUMP_SPEED)
    time.sleep(1)        
    GV.pump1.set_speed(HW.SAMPLE_PUMP_ADDRESS, HW.BUBBLE_DETECTION_PUMP_SPEED)
    time.sleep(1)        
    GV.pump1.set_pos_absolute(HW.TIRRANT_PUMP_ADDRESS, HW.DISPENSE_UNTIL_BUBBLE_TARGET)
    time.sleep(1)
    GV.pump1.set_pos_absolute(HW.SAMPLE_PUMP_ADDRESS, HW.DISPENSE_UNTIL_BUBBLE_TARGET)
    time.sleep(1)
    input1 = GV.labjack.getAIN(0)   #bubble sensor 1
    input2 = GV.labjack.getAIN(1)   #bubble sensor 2
    #check if the bubble semsor detect air or liquid
    cur_state_1 = air_or_liquid(input1)
    cur_state_2 = air_or_liquid(input2)
    prev_state_1 = cur_state_1
    prev_state_2 = cur_state_2
    bubble_1_search = True
    bubble_2_search = True
    
    while (bubble_1_search  or bubble_2_search) :
        input1 = GV.labjack.getAIN(0)
        cur_state_1 = air_or_liquid(input1)
        pos1 =GV.pump1.get_plunger_position(HW.TIRRANT_PUMP_ADDRESS)
        if (cur_state_1 != prev_state_1):
            bubble_1_search = False

        time.sleep(.025)
        input2 = GV.labjack.getAIN(1)
        cur_state_2 = air_or_liquid(input2)
        pos2 =GV.pump1.get_plunger_position(HW.SAMPLE_PUMP_ADDRESS)
        print('        BS1:{:.2f} position:{},   BS2:{:.2f} position:{}'.format(input1,pos1,input2, pos2))
        if (cur_state_2 != prev_state_2):
            bubble_2_search = False
        time.sleep(.025)

        
    GV.pump1.stop(HW.TIRRANT_PUMP_ADDRESS)
    time.sleep(.5)
    GV.pump1.stop(HW.SAMPLE_PUMP_ADDRESS)
    print('\t\tBubble detection terminated')
    GV.pump1.set_speed(HW.TIRRANT_PUMP_ADDRESS,HW.DEFAULT_PUMP_SPEEED)
    time.sleep(.5)
    GV.pump1.set_speed(HW.SAMPLE_PUMP_ADDRESS,HW.DEFAULT_PUMP_SPEEED)



    str1 = " bubble sensors 1&2 triggered\n" "  go to S4/E2"
    GV.SM_TEXT_TO_DIAPLAY ="S4,E1 -> action4_1\n"+ str1
    GV.next_E = 2

def action4_2():
      
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S4,E2 -> action4_1" "goint to S4/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S4,E2 -> action4_1" "goint to S4/E4"
        return          
  
    str1 = "  prepare to go to S5\n" "  going to S5/E0"
    GV.SM_TEXT_TO_DIAPLAY ="S4,E2 -> action4_2\n" + str1
    GV.next_E = 0


def action4_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S4,E3 -> action4_3\n" "goint to S4/E4"
        return         
    # print("S4,E3 -> action4_3")    
    GV.SM_TEXT_TO_DIAPLAY = "S4,E3 -> action4_3\n" "  going to PAUSE"
    GV.next_E = 0
    GV.prev_S = 4


def action4_4():    
    GV.SM_TEXT_TO_DIAPLAY ="S4,E4 -> action4_4\n" " going to ERROR state"
    GV.next_E = 0


#------------------------------------------------------------------------------------ 
def action5_0():
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S5,E0 -> action5_0" "  goint to S5/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S5,E0 -> action5_0" "  goint to S5/E4"
        return    

    str1 = "- V1 to LinetoPump\n""- V3 to TitrantLine\n""- V5 to TitrantCannula\n"
    str1 = str1 + "- V2 to LinetoGas\n""- V4 to SampleLine\n""- V7 to Cell\n""  Waiting for valve to go to positions..."
    GV.SM_TEXT_TO_DIAPLAY ="S5,E0 -> action5_0" + str1
    GV.next_E = 1


def action5_1():
    Done = True
    timeout = False
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S5,E1 -> action5_1" "  goint to S5/E3"
        return 
    if (GV.ERROR == True  or timeout==True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S5,E1 -> action5_1" "  goint to S5/E4"
        return    
    

    GV.pump1.set_valve(HW.TIRRANT_PUMP_ADDRESS, 'I')
    time.sleep(.5)
    GV.pump1.set_valve(HW.TITRANT_LOOP_ADDRESS, 'I')
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.TITRANT_CLEANING_ADDRESS,2)        
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.TITRANT_PIPETTE_ADDRESS,1)
    time.sleep(.5)
    GV.pump1.set_valve(HW.SAMPLE_PUMP_ADDRESS, 'I')
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.TITRANT_PORT_ADDRESS,2)
    time.sleep(.5)




    if (Done == False):        
        GV.SM_TEXT_TO_DIAPLAY = "S5,E1 -> action5_1\n" "  Waiting for valve to go to positions..."
        GV.next_E = 1
    else:        
        GV.SM_TEXT_TO_DIAPLAY ="S5,E1 -> action5_1\n"  "  valves in position\n" "  going to S5/E2"
        GV.next_E = 2
    


def action5_2():
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S5,E2 -> action5_2" "  goint to S5/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S5,E2 -> action5_2" "  goint to S5/E4"
        return    
    
    GV.SM_TEXT_TO_DIAPLAY ="S5,E2 -> action5_2" "  going to S6/E0"
    GV.next_E = 0


def action5_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S5,E5 -> action5_5" "   goint to S5/E4"
        return 
    
    GV.SM_TEXT_TO_DIAPLAY ="S5,E2 -> action5_2 ----> going to PAUSE state"
    GV.next_E = 0
    GV.prev_S = 5
    

def action5_4():
    GV.SM_TEXT_TO_DIAPLAY ="S5,E6 -> action5_4" " going to ERROR state"
    GV.next_E = 0


#-------------------------------------------------------------------------------
def action6_0():
    if (GV.PAUSE == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S6,E0 -> action6_0" "goint to S6/E5"
        return 
    if (GV.ERROR == True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = "S6,E0 -> action6_0" "goint to S6/E6"
        return 

    str1 = "  pump 1 to dispense\n"    "  pump 2 to dispense"
    GV.SM_TEXT_TO_DIAPLAY ="S6,E0 -> action6_0\n" + str1
    GV.next_E = 1


def action6_1():
    bubble_sensor_6_triggered = True    
    bubble_sensor_7_triggered = True    
    timeout = False
    if (GV.PAUSE == True or timeout==True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S6,E1 -> action6_1" "Pgoint to S6/E5"
        return 
    if (GV.ERROR == True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = "S6,E1 -> action6_1" "goint to S6/E6"
        return 

    print('Dispense until bubble')
    GV.pump1.set_speed(HW.TIRRANT_PUMP_ADDRESS, HW.BUBBLE_DETECTION_PUMP_SPEED)
    time.sleep(1)        
    GV.pump1.set_speed(HW.SAMPLE_PUMP_ADDRESS, HW.BUBBLE_DETECTION_PUMP_SPEED)
    time.sleep(1)        
    GV.pump1.set_pos_absolute(HW.TIRRANT_PUMP_ADDRESS, HW.DISPENSE_UNTIL_BUBBLE_TARGET)
    time.sleep(1)
    GV.pump1.set_pos_absolute(HW.SAMPLE_PUMP_ADDRESS, HW.DISPENSE_UNTIL_BUBBLE_TARGET)
    time.sleep(1)
    input1 = GV.labjack.getAIN(5)   #bubble sensor 6
    input2 = GV.labjack.getAIN(6)   #bubble sensor 7
    #check if the bubble semsor detect air or liquid
    cur_state_1 = air_or_liquid(input1)
    cur_state_2 = air_or_liquid(input2)
    prev_state_1 = cur_state_1
    prev_state_2 = cur_state_2
    bubble_1_search = True
    bubble_2_search = True
    
    while (bubble_1_search  or bubble_2_search) :
        input1 = GV.labjack.getAIN(0)
        cur_state_1 = air_or_liquid(input1)
        pos1 =GV.pump1.get_plunger_position(HW.TIRRANT_PUMP_ADDRESS)
        if (cur_state_1 != prev_state_1):
            bubble_1_search = False

        time.sleep(.025)
        input2 = GV.labjack.getAIN(1)
        cur_state_2 = air_or_liquid(input2)
        pos2 =GV.pump1.get_plunger_position(HW.SAMPLE_PUMP_ADDRESS)
        print('        BS1:{:.2f} position:{},   BS2:{:.2f} position:{}'.format(input1,pos1,input2, pos2))
        if (cur_state_2 != prev_state_2):
            bubble_2_search = False
        time.sleep(.025)

        
    GV.pump1.stop(HW.TIRRANT_PUMP_ADDRESS)
    time.sleep(.5)
    GV.pump1.stop(HW.SAMPLE_PUMP_ADDRESS)
    print('\t\tBubble detection terminated')
    GV.pump1.set_speed(HW.TIRRANT_PUMP_ADDRESS,HW.DEFAULT_PUMP_SPEEED)
    time.sleep(.5)
    GV.pump1.set_speed(HW.SAMPLE_PUMP_ADDRESS,HW.DEFAULT_PUMP_SPEEED)


    str1 = "  bubble sensors 6&7 triggered\n" "  go to S6/E2\n"
    str1 = str1 +"  pump 1 to position\n"  "  pump 2 to position"
    GV.SM_TEXT_TO_DIAPLAY ="S6,E1 -> action6_1\n"+ str1
    GV.next_E = 2


def action6_2():      
    if (GV.PAUSE == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S6,E2 -> action6_1" "goint to S6/E5"
        return 
    if (GV.ERROR == True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = "S6,E2 -> action6_1" "goint to S6/E6"
        return          
  
    TC2_pos = RECIPE['Load_Prime']['TC2_Volume']
    SC2_pos = RECIPE['Load_Prime']['SC2_Volume']

    pump1_pos = GV.pump1.get_plunger_position(HW.TIRRANT_PUMP_ADDRESS)
    time.sleep(.5)
    target_pos_1 = pump1_pos + TC2_pos
    GV.pump1.set_pos_absolute(HW.TIRRANT_PUMP_ADDRESS, target_pos_1)
    time.sleep(.5)

    pump2_pos = GV.pump1.get_plunger_position(HW.TIRRANT_PUMP_ADDRESS)
    time.sleep(.5)
    target_pos_2 = pump2_pos + SC2_pos
    GV.pump1.set_pos_absolute(HW.TIRRANT_PUMP_ADDRESS, target_pos_2)
    time.sleep(.5)

    str1 = "  pump 1 to position\n"  "  pump 2 to position"
    GV.SM_TEXT_TO_DIAPLAY ="S6,E2 -> action6_2\n" + str1
    GV.next_E = 3

def action6_3():      
    timeout = False
    Done = True
    if (GV.PAUSE == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S6,E3 -> action6_3\n" "goint to S6/E5"
        return 
    if (GV.ERROR == True  or  timeout==True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = "S6,E3 -> action6_3\n" "goint to S6/E6"
        return          
  
    if (Done==True):
        str1 = "  pumps in position"
        GV.SM_TEXT_TO_DIAPLAY ="S6,E3 -> action6_3\n" + str1
        GV.next_E = 4
    else:
        str1 = "  waiting for pumps to get to position"
        GV.SM_TEXT_TO_DIAPLAY ="S6,E3 -> action6_3\n" + str1
        GV.next_E = 3

def action6_4():      
    if (GV.PAUSE == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S6,E4 -> action6_4\n" "goint to S6/E5"
        return 
    if (GV.ERROR == True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = "S6,E4 -> action6_4\n" "goint to S6/E6"
        return          
  
    str1 = "  going to S7/E0"
    GV.SM_TEXT_TO_DIAPLAY ="S6,E2 -> action6_2\n" + str1
    GV.next_E = 0


def action6_5():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S6,E5 -> action6_5\n" "goint to S6/E6"
        return         
    # print("S4,E3 -> action4_3")    
    GV.SM_TEXT_TO_DIAPLAY = "S6,E5 -> action6_5\n" "  going to PAUSE"
    GV.next_E = 0
    GV.prev_S = 6


def action6_6():    
    GV.SM_TEXT_TO_DIAPLAY ="S6,E6 -> action6_6\n" " going to ERROR state"
    GV.next_E = 0
    

#-----------------------------------------------------------------------------        

def action7_0():  
    if (GV.PAUSE == True):
        GV.next_E = 2
        GV.SM_TEXT_TO_DIAPLAY = "S7,E0 -> action7_0\n" "going to S7/E2"
        return 
    if (GV.ERROR == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S7,E0 -> action7_0\n" "going to S7/E3"
        return 
        
    str1 = "  perpare to trerminate SM\n" "  going to S7/E1"
    GV.SM_TEXT_TO_DIAPLAY = "S7,E0 -> action7_0\n" + str1
    GV.next_E = 1


def action7_1():
    
    if (GV.PAUSE == True):
        GV.next_E = 2
        GV.SM_TEXT_TO_DIAPLAY = "S7,E1 -> action7_1\n" "going to S7/E2"
        return 
    if (GV.ERROR == True ):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S7,E1 -> action7_1\n" "going to S7/E3"
        return 
    
    GV.SM_TEXT_TO_DIAPLAY = "S7,E1 -> action7_1\n" "  Terminating SM" 
    GV.next_E = 0
    GV.terminate_SM = True


def action7_2():
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S7,E2 -> action7_2\n" "going to S7/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S7,E2 -> action7_2\n" "going to S7/E4"
        return     
    
    GV.SM_TEXT_TO_DIAPLAY ="S7,E2 -> action7_2\n" "  go to PAUSE state"
    GV.next_E = 0

    
def action7_3():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY = "S7,E3 -> action7_3\n""  going to ERROR state"


#-----------------------------------------------------------------------------  


def action8_0():
    if (GV.ERROR == True):
        GV.next_E = 13
        GV.SM_TEXT_TO_DIAPLAY = "S8,E0 -> action8_0\n" "going to S8/E8"
        return    

    if (GV.PAUSE == True):
        GV.next_E = 0
    else:
        GV.next_E = GV.prev_S

    GV.SM_TEXT_TO_DIAPLAY ="S8,E0 -> action8_0"


def action8_1():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S8,E1 -> action8_1\n" "  going to S0/E0"

def action8_2():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S8,E2 -> action8_2\n" "  going to S1/E0"

def action8_3():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S8,E3 -> action8_3\n" "  going to S2/E0"

def action8_4():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S8,E4 -> action8_4\n" "  going to S3/E0"

def action8_5():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S8,E5 -> action8_5\n" "  going to S4/E0"

def action8_6():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S8,E6 -> action8_6\n"  "  going to S5/E0"
    
def action8_7():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S8,E7 -> action8_7\n"  "  going to S6/E0"

def action8_8():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S8,E8 -> action8_8\n"  "  going to S7/E0"

def action8_9():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S8,E9 -> action8_9\n"  "  going to S9/E0"



#--------------
def action9_0():
    print("S9,E0 -> action9_0")
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S9,E0 -> action9_0"


#-------------------------------------------------------------
#-------------- END OF ACTIONS -------------------------------
#-------------------------------------------------------------


