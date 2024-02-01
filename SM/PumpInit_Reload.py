import  numpy as np
import  general.global_vars as GV
import  HW
import  time
from    general.recipe import RECIPE


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
    return "PumpInit_Reload"

state_name = {0:"S0: Initialization", 1:"S1: Initialize Pumps", 2:"S2: Manual Purge1", 3:"S3: Manual Purge2",
              4:"S4: Load H2O1", 5:"S5: Load H2O2", 6:"S6: Expel Air1", 7:"S7: Expel Air2", 8:"S8: Get New Air Slugs1",
              9:"S8: retract Column 1", 10:"S10: retract Column 2", 11:"S11: PumpInit&Reload Complete", 12:"Pause", 13:"Error"}


def air_or_liquid( voltage):
    if voltage > HW.BS_THRESHOLD:
        return 'liquid'
    else:
        return 'air'
    
def NewAirSlugs(pump_address, valve_address):
    pump_speed = RECIPE["Func_NewAirSlugs"]["pump_speed"]
    air_slug_total_count = RECIPE["Func_NewAirSlugs"]["AirSlug_Total_count"]
    air_slug_volume = RECIPE["Func_NewAirSlugs"]["AirSlug_Volume"]
    LastAirSlug_Volume = RECIPE["Func_NewAirSlugs"]["LastAirSlug_Volume"]
    SC2_Volume = RECIPE["Func_NewAirSlugs"]["SC2_Volume"]
    WaterSlug_Volume = RECIPE["Func_NewAirSlugs"]["WaterSlug_Volume"]

    
    tot =0

    starting_pos = GV.pump1.get_plunger_position(pump_address)
    
    GV.pump1.set_speed(pump_address, pump_speed)
    time.sleep(1)

    airslug_count = 0
    next_pos =  starting_pos
    while (airslug_count < air_slug_total_count):        
        GV.pump1.set_multiwayvalve(valve_address,1)        #Valve to Air
        time.sleep(1)    
        next_pos +=  air_slug_volume
        GV.pump1.set_pos_absolute(pump_address, next_pos)
        pump_pos = 0
        while(pump_pos < next_pos):
            pump_pos = GV.pump1.get_plunger_position(pump_address)
            print("count:",airslug_count+1,"/",air_slug_total_count,"pump pos:",
                  pump_pos, '  target:', next_pos)
            time.sleep(1)
            
        GV.pump1.set_multiwayvalve(valve_address,2)        #Valve to water
        time.sleep(1)
        next_pos += air_slug_volume
        GV.pump1.set_pos_absolute(pump_address, next_pos)  #pump to position
        pump_pos = 0
        while(pump_pos < next_pos):
            pump_pos = GV.pump1.get_plunger_position(pump_address)
            print("\t\tpump pos:", pump_pos, '  target:', next_pos)
            time.sleep(1)
        airslug_count += 1


    GV.pump1.set_multiwayvalve(valve_address,1)        #Valve to Air
    time.sleep(1) 
    next_pos += LastAirSlug_Volume
    GV.pump1.set_pos_absolute(pump_address, next_pos)  #pump to position
    while(pump_pos < next_pos):
        pump_pos = GV.pump1.get_plunger_position(pump_address)
        print("pump pos:", pump_pos, '  target:', next_pos)
        time.sleep(1)     

#---------------  ACTIONS  --------------
def action0_0():
    if (GV.PAUSE == True):
        GV.next_E = 4       
        GV.SM_TEXT_TO_DIAPLAY = "S0,E0 -> action0_0\n" "Prepare to go to Pause State"
        return 
    if (GV.ERROR == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S0,E0 -> action0_0\n" "Prepare to go to error State"
        return     
    
    str1 = "  prepare for initialization\n" "  -V1 to LinetoPump\n" "  -V3 to TitrantLine\n"
    str1 = str1 +"  -V5 to Reservoirs\n" "  -V2 to LinetoPump\n" " - V4 to SampleLine\n" " - V7 to Reservoirs\n"
    str1 = str1 +" - V8 to Waste\n" " - V9 to Waste\n" "  going to S0/E1" 
    GV.SM_TEXT_TO_DIAPLAY = "S0,E0 -> action0_0\n" + str1
    GV.next_E = 1

    


def action0_1():
    if (GV.PAUSE == True):
        GV.next_E = 4       
        GV.SM_TEXT_TO_DIAPLAY = "S0,E1 -> action0_1\n" "Prepare to go to Pause State"
        return 
    if (GV.ERROR == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S0,E1 -> action0_1\n" "Prepare to go to error State"
        return 
    
    GV.pump1.set_valve(HW.TIRRANT_PUMP_ADDRESS, 'E')
    time.sleep(.5)
    GV.pump1.set_valve(HW.TITRANT_LOOP_ADDRESS, 'E')
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.TITRANT_PIPETTE_ADDRESS,3)
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.TITRANT_CLEANING_ADDRESS,1)        
    time.sleep(.5)
    GV.pump1.set_valve(HW.SAMPLE_PUMP_ADDRESS, 'E')
    time.sleep(.5)
    GV.pump1.set_valve(HW.SAMPLE_LOOP_ADDRESS, 'E')
    time.sleep(.5)
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
    


    str1 = "  prepare for initialization\n" "  -V1 to LinetoPump\n" "  -V3 to TitrantLine\n"
    str1 = str1 +"  -V5 to Reservoirs\n" "  -V2 to LinetoPump\n" " - V4 to SampleLine\n" " - V7 to Reservoirs\n"
    str1 = str1 +" - V8 to Waste\n" " - V9 to Waste\n" "  going to S0/E1"
    GV.SM_TEXT_TO_DIAPLAY = "S0,E1 -> action0_1\n" + str1
    
    GV.next_E = 2

def action0_2():
    timeout = False
    Done = True #False
    if (GV.PAUSE == True):
        GV.next_E = 4       
        GV.SM_TEXT_TO_DIAPLAY = "S0,E2 -> action0_2\n" "going to S0/E4"
        return 
    if (GV.ERROR == True or timeout == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S0,E2 -> action0_2\n" "going to S0/E5"
        return 
   
    if (Done == False):
        GV.next_E = 2
        GV.SM_TEXT_TO_DIAPLAY = "S0,E0 -> action0_2\n" "  Waiting for valves to reach positions"
    else:
        GV.SM_TEXT_TO_DIAPLAY = "S0,E0 -> action0_2\n" "  Valves in Position" "going to S0/E3"
    GV.next_E = 3


def action0_3():
    if (GV.PAUSE == True):
        GV.next_E = 4       
        GV.SM_TEXT_TO_DIAPLAY = "S0,E3 -> action0_3\n" "going to S0/E4"
        return 
    if (GV.ERROR == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S0,E3 -> action0_3\n" "going to S0/E5"
        return 
    
    str1 = "  Init. Titran Pump\n" "  Init. Sample Pump" 
    GV.SM_TEXT_TO_DIAPLAY = "S0,E3 -> action0_3\n"  + str1
     
    GV.next_E = 0


def action0_4():
    if (GV.ERROR == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S0,E4 -> action0_4\n" "going to S0/E5"
        return     
    GV.next_E = 0
    GV.prev_S = 0
    GV.SM_TEXT_TO_DIAPLAY ="S1,E2 -> action1_2\n\tgo to GV.PAUSE state"
    
    
def action0_5():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY = "S1,E3 -> action1_3\n\tgoing to ERROR state"


#-------------------------------------------------------------------------------------------
def action1_0():  
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0\n" "going to S1/E4"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0\n" "going to S1/E4"
        return 

    GV.pump1.pump_Zinit(HW.TIRRANT_PUMP_ADDRESS)
    # # print("\t\tPump1 initialized")
    time.sleep(3)
    GV.pump1.pump_Zinit(HW.SAMPLE_PUMP_ADDRESS)    
    # # print("\t\tPump2 initialized")
    time.sleep(3)


    str1 = "  Init. Titran Pump\n" "  Init. Sample Pump\n" "  going to S1/E1"
    GV.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0\n" + str1
    GV.next_E = 1


def action1_1():
    timeout = False
    Done = True #False
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" "going to S1/E3"
        return 
    if (GV.ERROR == True or timeout==True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" "going to S1/E4"
        return 
    
    if (Done == False):        
        GV.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" "  Waiting for Pumps to initialize"
        GV.next_E = 1
    else:
        GV.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" "  Pumps initialized" "going to S1/E2"
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
    

    str1 ="  Purge Sample and Titrant Lines"
    GV.SM_TEXT_TO_DIAPLAY ="S1,E2 -> action1_2\n" + str1
    GV.next_E = 0

def action1_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S1,E3 -> action1_3\n" "going to S1/E4"
        return     
    GV.SM_TEXT_TO_DIAPLAY ="S1,E2 -> action1_3\n\tgoing to PAUSE state"
    GV.next_E = 0
    GV.prev_S = 1
    
    
def action1_4():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY = "S1,E3 -> action1_3\n\tgoing to ERROR state"


#----------------------------------------------------------------   
def action2_0():
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S2,E0 -> action1_0\n" "going to S2/E4"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S2,E0 -> action1_0\n" "going to S2/E4"
        return 
    
    
    GV.pump1.set_valve(HW.TIRRANT_PUMP_ADDRESS, 'E')
    time.sleep(.5)
    GV.pump1.set_valve(HW.TITRANT_LOOP_ADDRESS, 'E')
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.TITRANT_PIPETTE_ADDRESS,3)
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.TITRANT_CLEANING_ADDRESS,1)        
    time.sleep(.5)
    GV.pump1.set_valve(HW.SAMPLE_PUMP_ADDRESS, 'E')
    time.sleep(.5)
    GV.pump1.set_valve(HW.SAMPLE_LOOP_ADDRESS, 'E')
    time.sleep(.5)
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


    GV.SM_TEXT_TO_DIAPLAY ="Purge Sample and Titrant Lines"
    GV.next_E = 1

def action2_1():
    timeout = False 
    Done = True
    if (GV.PAUSE == True):
        GV.next_E = 3           
        GV.SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1\n" "  goint to S2/E3"
        return 
    if (GV.ERROR == True or timeout==True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1\n" "  goint to S2/E4"
        return 
    
    if (Done == False):        
        GV.SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1\n" "  Waiting for valves to reach positions"
        GV.next_E = 1
    else:
        GV.SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1\n" "  Valves in position\n" "  going to S1/E2"
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
    
    GV.SM_TEXT_TO_DIAPLAY ="Please press NEXT button to continue..."
    GV.activate_NEXT_button = True
    GV.next_E = 0


def action2_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S2,E3 -> action2_3\n" "Prepare to go to error State"
        return         

    GV.next_E = 0
    GV.prev_S = 2
    GV.SM_TEXT_TO_DIAPLAY = "going to PAUSE state "

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


    while (GV.NEXT == False):        
        time.sleep(1)
        
    GV.NEXT = False
    GV.activate_NEXT_button = False
    print('next button is:', GV.NEXT)
    str1 = "  Purge Sample and Tritrandt Valves"
    GV.SM_TEXT_TO_DIAPLAY ="S3,E0 -> action3_0\n"+str1
    GV.next_E = 1


def action3_1():
    NEXT = True
    if (GV.PAUSE == True):
        GV.next_E = 3        
        GV.SM_TEXT_TO_DIAPLAY = "S3,E1 -> action3_1\n" "  goint to S2/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S3,E1 -> action3_1\n" "  goint to S2/E4"
        return         
    
    if (NEXT == False):
        GV.SM_TEXT_TO_DIAPLAY ="S3,E1 -> action3_1\n""\t  wait for NEXT button to be pressed..."
        GV.next_E = 1
    else:    
        GV.SM_TEXT_TO_DIAPLAY ="S3,E1 -> action3_1\n""\tgo to S3/E2"
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
    
    str1 = "  -V1 to PumptoLine\n" "  -V3 to PumptoLine\n""  -V5 to Reservoirs\n" "  -V9 to Water\n"
    str1 = str1 +"  -V6 to V7\n" "  -V2 to PumptoLine\n" "  -V4 to PumptoLine\n" "  -V7 to Reservoirs\n" "  -V8 to Water"
    GV.SM_TEXT_TO_DIAPLAY = str1
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

    GV.pump1.set_valve(HW.TIRRANT_PUMP_ADDRESS, 'I')
    time.sleep(.5)
    GV.pump1.set_valve(HW.TITRANT_LOOP_ADDRESS, 'I')
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.TITRANT_PIPETTE_ADDRESS,1)
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.TITRANT_CLEANING_ADDRESS,2)        
    time.sleep(.5)
    GV.pump1.set_valve(HW.SAMPLE_PUMP_ADDRESS, 'I')
    time.sleep(.5)
    GV.pump1.set_valve(HW.SAMPLE_LOOP_ADDRESS, 'I')
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.TITRANT_PORT_ADDRESS,2)
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.DEGASSER_ADDRESS,2)        
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.SAMPLE_CLEANING_ADDRESS,2)    
    time.sleep(.5)
    GV.next_E = 1
    GV.SM_TEXT_TO_DIAPLAY ="S4,E0 -> action4_0\n"  


def action4_1():
    Done = True
    timeout = False
    if (GV.PAUSE == True or timeout==True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1\n" "Pgoint to S4/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1\n" "goint to S4/E4"
        return 

    if (Done == False):        
        GV.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action2_1\n" "  Waiting for valves to reach positions"
        GV.next_E = 1
    else:        
        str1 = "  Valves reached position\n" "  go to S4/E2"
        GV.SM_TEXT_TO_DIAPLAY ="S4,E1 -> action4_1\n"+ str1
        GV.next_E = 2

def action4_2():
      
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S4,E2 -> action4_1\n" "goint to S4/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S4,E2 -> action4_1\n" "goint to S4/E4"
        return          
  
    str1 = "pump1: dispense until bubble sensor\n" "pump2: dispense until bubble sensor"
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
    GV.prev_S = 4


#------------------------------------------------------------------------------------ 
def action5_0():
    if (GV.PAUSE == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S5,E0 -> action5_0\n" "  goint to S5/E5"
        return 
    if (GV.ERROR == True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = "S5,E0 -> action5_0\n" "  goint to S5/E6"
        return    
    
    GV.SM_TEXT_TO_DIAPLAY ="S5,E0 -> action5_0\n" "  Pump 1 dispense\n" "  Pump 2 dispense"
    GV.next_E = 1


def action5_1():
    Done = True
    timeout = False
    if (GV.PAUSE == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S5,E1 -> action5_1\n" "  goint to S5/E5"
        return 
    if (GV.ERROR == True  or timeout==True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = "S5,E1 -> action5_1\n" "  goint to S5/E6"
        return    
    
    print('Dispense until bubble')
    GV.pump1.set_speed(HW.TIRRANT_PUMP_ADDRESS, HW.BUBBLE_DETECTION_PUMP_SPEED)
    time.sleep(1)        
    GV.pump1.set_speed(HW.SAMPLE_PUMP_ADDRESS, HW.BUBBLE_DETECTION_PUMP_SPEED)
    time.sleep(1)        
    GV.pump1.set_pos_absolute(HW.TIRRANT_PUMP_ADDRESS, 20000)
    time.sleep(1)
    GV.pump1.set_pos_absolute(HW.SAMPLE_PUMP_ADDRESS, 20000)
    time.sleep(1)
    input1 = GV.labjack.getAIN(0)
    input2 = GV.labjack.getAIN(1)
    #check if the bubble semsor detect air or liquid
    cur_state_1 = air_or_liquid(input1)
    cur_state_2 = air_or_liquid(input2)
    prev_state_1 = cur_state_1
    prev_state_2 = cur_state_2
    while (cur_state_1 == prev_state_1) or (cur_state_2 == prev_state_2) :        
        input1 = GV.labjack.getAIN(0)
        cur_state_1 = air_or_liquid(input1)
        pos1 =GV.pump1.get_plunger_position(HW.TIRRANT_PUMP_ADDRESS)
        time.sleep(.025)
        input2 = GV.labjack.getAIN(1)
        cur_state_2 = air_or_liquid(input2)
        pos2 =GV.pump1.get_plunger_position(HW.SAMPLE_PUMP_ADDRESS)
        print('        BS1:{:.2f} position:{},   BS2:{:.2f} position:{}'.format(input1,pos1,input2, pos2))
        time.sleep(.025)
        
    GV.pump1.stop(HW.TIRRANT_PUMP_ADDRESS)
    time.sleep(.5)
    GV.pump1.stop(HW.SAMPLE_PUMP_ADDRESS)
    print('\t\tBubble detection terminated')
    GV.pump1.set_speed(HW.TIRRANT_PUMP_ADDRESS,HW.DEFAULT_PUMP_SPEEED)
    time.sleep(.5)
    GV.pump1.set_speed(HW.SAMPLE_PUMP_ADDRESS,HW.DEFAULT_PUMP_SPEEED)


    if (Done == False):        
        GV.SM_TEXT_TO_DIAPLAY = "S5,E1 -> action5_1\n" "  Waiting for pumps to finish dispensing..."
        GV.next_E = 1
    else:        
        GV.SM_TEXT_TO_DIAPLAY ="pump 1 to position XX\n""pump 2 to position XX"
        GV.next_E = 2
    


def action5_2():
    if (GV.PAUSE == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S5,E2 -> action5_2\n" "  goint to S5/E5"
        return 
    if (GV.ERROR == True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = "S5,E2 -> action5_2\n" "  goint to S5/E6"
        return    
    
    fill_pos_titrant = RECIPE['PumpInit_Reload']['TitrantPumpt_syringe_fill_volume']
    fill_pos_sample = RECIPE['PumpInit_Reload']['SamplePumpt_syringe_fill_volume']

    
    
    GV.pump1.set_pos_absolute(HW.TIRRANT_PUMP_ADDRESS, fill_pos_titrant)
    time.sleep(1)
    GV.pump1.set_pos_absolute(HW.SAMPLE_PUMP_ADDRESS, fill_pos_sample)
    time.sleep(1)
    GV.SM_TEXT_TO_DIAPLAY ="S5,E2 -> action5_2\n" "  Pump 1 position xxx\n" "  Pump 2 to position xxx"
    GV.next_E = 3


def action5_3():
    Done = True
    timeout = False
    if (GV.PAUSE == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S5,E3 -> action5_3\n" "  goint to S5/E5"
        return 
    if (GV.ERROR == True  or timeout==True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = "S5,E3 -> action5_3\n" "  goint to S5/E6"
        return    
    
    if (Done == False):        
        GV.SM_TEXT_TO_DIAPLAY = "S5,E3 -> action5_3\n" "  Waiting for pumps to reach positions..."
        GV.next_E = 3
    else:        
        GV.SM_TEXT_TO_DIAPLAY ="S5,E3 -> action5_3\n"  "  pumps in position" "  going to S5/E4"
        GV.next_E = 4


def action5_4():
    if (GV.PAUSE == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S5,E4 -> action5_4\n" "  goint to S5/E5"
        return 
    if (GV.ERROR == True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = "S5,E4 -> action5_4\n" "  goint to S5/E6"
        return    
    
    GV.SM_TEXT_TO_DIAPLAY ="S5,E4 -> action5_4\n" "  -V1 to PumptoAir\n" "  -V2 to PumptoAir"
    GV.next_E = 0


def action5_5():
    if (GV.ERROR == True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = "S5,E5 -> action5_5\n" "   goint to S5/E6"
        return 
    
    GV.SM_TEXT_TO_DIAPLAY ="S5,E2 -> action5_2 \n----> going to PAUSE state"
    GV.next_E = 0
    GV.prev_S = 5
    

def action5_6():
    GV.SM_TEXT_TO_DIAPLAY ="S5,E6 -> action5_6\n"
    GV.next_E = 0
    GV.prev_S = 5


#-------------------------------------------------------------------------------
def action6_0():
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S6,E0 -> action6_0\n" "goint to S6/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S6,E0 -> action6_0\n" "goint to S6/E4"
        return 

    GV.pump1.set_valve(HW.TIRRANT_PUMP_ADDRESS, 'I')
    time.sleep(.5)
    GV.pump1.set_valve(HW.TITRANT_LOOP_ADDRESS, 'I')
    time.sleep(.5)

    str1 = "  -V1 to PumptoAir\n""  -V2 to PumptoAir"
    GV.SM_TEXT_TO_DIAPLAY ="S6,E0 -> action6_0\n" + str1
    GV.next_E = 1


def action6_1():
    Done = True
    timeout = False
    if (GV.PAUSE == True or timeout==True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S6,E1 -> action6_1\n" "Pgoint to S6/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S6,E1 -> action6_1\n" "goint to S6/E4"
        return 

    if (Done == False):        
        GV.SM_TEXT_TO_DIAPLAY = "S6,E1 -> action6_1\n" "  Waiting for valves to reach positions"
        GV.next_E = 1
    else:        
        str1 = "  Valves reached position\n" "  go to S6/E2"
        GV.SM_TEXT_TO_DIAPLAY ="S6,E1 -> action6_1\n"+ str1
        GV.next_E = 2

def action6_2():      
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S6,E2 -> action6_1\n" "goint to S6/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S6,E2 -> action6_1\n" "goint to S6/E4"
        return          
  
    
    str1 = "  pump 1 to position xxx\n""  pump 2 to position xxx"
    GV.SM_TEXT_TO_DIAPLAY ="S6,E2 -> action6_2\n" + str1
    GV.next_E = 0


def action6_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S6,E3 -> action6_3\n" "goint to S6/E4"
        return         
    # print("S4,E3 -> action4_3")    
    GV.SM_TEXT_TO_DIAPLAY = "S6,E3 -> action6_3\n" "  going to PAUSE"
    GV.next_E = 0
    GV.prev_S = 6


def action6_4():    
    GV.SM_TEXT_TO_DIAPLAY ="S6,E4 -> action6_4\n" " going to ERROR state"
    GV.next_E = 0
    GV.prev_S = 6

#-----------------------------------------------------------------------------        
def action7_0():
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S7,E0 -> action7_0\n" "goint to S7/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S7,E0 -> action7_0\n" "goint to S7/E4"
        return 

    fill_pos_titrant = RECIPE['PumpInit_Reload']['titrantpump_expelair_volume']
    fill_pos_sample = RECIPE['PumpInit_Reload']['samplepump_expelair_volume']
    
    GV.pump1.set_pos_absolute(HW.TIRRANT_PUMP_ADDRESS, fill_pos_titrant)
    time.sleep(1)
    GV.pump1.set_pos_absolute(HW.SAMPLE_PUMP_ADDRESS, fill_pos_sample)
    time.sleep(1)


    str1 = "  pump 1 to position xxx\n""  pump 2 to position xxx"
    GV.SM_TEXT_TO_DIAPLAY ="S7,E0 -> action7_0\n" + str1
    GV.next_E = 1


def action7_1():
    Done = True
    timeout = False
    if (GV.PAUSE == True or timeout==True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S7,E1 -> action7_1\n" "Pgoint to S7/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S7,E1 -> action7_1\n" "goint to S7/E4"
        return 

    if (Done == False):        
        GV.SM_TEXT_TO_DIAPLAY = "S7,E1 -> action6_1\n" "  Waiting for pumps to reach positions"
        GV.next_E = 1
    else:        
        str1 = "  pumps reached position\n" "  go to S7/E2"
        GV.SM_TEXT_TO_DIAPLAY ="S7,E1 -> action7_1\n"+ str1
        GV.next_E = 2


def action7_2():      
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S7,E2 -> action7_1\n" "goint to S7/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S7,E2 -> action7_1\n" "goint to S7/E4"
        return          
  
    str1 = "  sample pump:\n Run function NewAirSlugs\n"
    GV.SM_TEXT_TO_DIAPLAY ="S7,E2 -> action7_2\n" + str1
    GV.next_E = 0


def action7_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S7,E3 -> action7_3\n" "goint to S7/E4"
        return         
    # print("S4,E3 -> action4_3")    
    GV.SM_TEXT_TO_DIAPLAY = "S7,E3 -> action7_3\n" "  going to PAUSE"
    GV.next_E = 0
    GV.prev_S = 7


def action7_4():    
    GV.SM_TEXT_TO_DIAPLAY ="S7,E4 -> action7_4\n" " going to ERROR state"
    GV.next_E = 0
    GV.prev_S = 7

#-----------------------------------------------------------------------------      
def action8_0():
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S8,E0 -> action8_0\n" "goint to S8/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S8,E0 -> action8_0\n" "goint to S8/E4"
        return 


    pump_address = HW.SAMPLE_PUMP_ADDRESS
    valve_address = HW.DEGASSER_ADDRESS
    NewAirSlugs(pump_address, valve_address)


    str1 = "  titrant pump: run function NewAirSlugs"
    GV.SM_TEXT_TO_DIAPLAY ="S8,E0 -> action8_0\n" + str1
    GV.next_E = 1


def action8_1():
    Done = True
    timeout = False
    if (GV.PAUSE == True or timeout==True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S8,E1 -> action8_1\n" "Pgoint to S8/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S8,E1 -> action8_1\n" "goint to S8/E4"
        return 


    pump_address = HW.TIRRANT_PUMP_ADDRESS
    valve_address = HW.SAMPLE_CLEANING_ADDRESS
    NewAirSlugs(pump_address, valve_address)


    if (Done == False):        
        GV.SM_TEXT_TO_DIAPLAY = "S8,E1 -> action8_1\n" "  Waiting for pumps to finish functions"
        GV.next_E = 1
    else:        
        str1 = "  pumps completed functions\n" "  go to S8/E2"
        GV.SM_TEXT_TO_DIAPLAY ="S8,E1 -> action8_1\n"+ str1
        GV.next_E = 2


def action8_2():      
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S8,E2 -> action8_1\n" "goint to S8/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S8,E2 -> action8_1\n" "goint to S8/E4"
        return          
  
    str1 = "  V8 to Air\n" "  V9 to Air"
    GV.SM_TEXT_TO_DIAPLAY ="S9,E2 -> action9_2\n" + str1
    GV.next_E = 0


def action8_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S8,E3 -> action8_3\n" "goint to S8/E4"
        return         
    # print("S4,E3 -> action4_3")    
    GV.SM_TEXT_TO_DIAPLAY = "S8,E3 -> action8_3\n" "  going to PAUSE"
    GV.next_E = 0
    GV.prev_S = 8


def action8_4():    
    GV.SM_TEXT_TO_DIAPLAY ="S8,E4 -> action8_4\n" " going to ERROR state"
    GV.next_E = 0
    GV.prev_S = 8

#-----------------------------------------------------------------------------  

def action9_0():
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S9,E0 -> action9_0\n" "goint to S9/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S9,E0 -> action9_0\n" "goint to S9/E4"
        return 


    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.DEGASSER_ADDRESS,2)        
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.SAMPLE_CLEANING_ADDRESS,2)    
    time.sleep(.5)


    str1 = "  V8 to Air\n" "  V9 to Air"
    GV.SM_TEXT_TO_DIAPLAY ="S9,E0 -> action9_0\n" + str1
    GV.next_E = 1


def action9_1():
    Done = True
    timeout = False
    if (GV.PAUSE == True or timeout==True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S9,E1 -> action9_1\n" "Pgoint to S9/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S9,E1 -> action9_1\n" "goint to S9/E4"
        return 

    if (Done == False):        
        GV.SM_TEXT_TO_DIAPLAY = "S9,E1 -> action6_1\n" "  Waiting for valves to reach positions"
        GV.next_E = 1
    else:        
        str1 = "  valves reached position\n" "  go to S9/E2"
        GV.SM_TEXT_TO_DIAPLAY ="S9,E1 -> action9_1\n"+ str1
        GV.next_E = 2


def action9_2():      
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S9,E2 -> action9_1\n" "goint to S9/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S9,E2 -> action9_1\n" "goint to S9/E4"
        return          
  
    str1 = "  prepare to go to S10\n" "  going to S10/E0"
    GV.SM_TEXT_TO_DIAPLAY ="S9,E2 -> action9_2\n" + str1
    GV.next_E = 0


def action9_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S9,E3 -> action9_3\n" "goint to S9/E4"
        return         
    # print("S4,E3 -> action4_3")    
    GV.SM_TEXT_TO_DIAPLAY = "S9,E3 -> action9_3\n" "  going to PAUSE"
    GV.next_E = 0
    GV.prev_S = 9


def action9_4():    
    GV.SM_TEXT_TO_DIAPLAY ="S9,E4 -> action9_4\n" " going to ERROR state"
    GV.next_E = 0
    GV.prev_S = 9

#-----------------------------------------------------------------------------  

def action10_0():
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S10,E0 -> action10_0\n" "goint to S10/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S10,E0 -> action10_0\n" "goint to S10/E4"
        return 

    str1 = "  pump 1 pickup\n" "  pump 2 pickup"
    GV.SM_TEXT_TO_DIAPLAY ="S10,E0 -> action10_0\n" + str1
    GV.next_E = 1


def action10_1():
    Done = True
    timeout = False
    if (GV.PAUSE == True or timeout==True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S10,E1 -> action10_1\n" "Pgoint to S10/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S10,E1 -> action10_1\n" "goint to S10/E4"
        return 



    print('Pickup until bubble')
    GV.pump1.set_speed(HW.TIRRANT_PUMP_ADDRESS, HW.BUBBLE_DETECTION_PUMP_SPEED)
    time.sleep(1)        
    GV.pump1.set_speed(HW.SAMPLE_PUMP_ADDRESS, HW.BUBBLE_DETECTION_PUMP_SPEED)
    time.sleep(1)        
    GV.pump1.set_pos_absolute(HW.TIRRANT_PUMP_ADDRESS, 0)
    time.sleep(1)
    GV.pump1.set_pos_absolute(HW.SAMPLE_PUMP_ADDRESS, 0)
    time.sleep(1)
    input1 = GV.labjack.getAIN(0)
    input2 = GV.labjack.getAIN(1)
    #check if the bubble semsor detect air or liquid
    cur_state_1 = air_or_liquid(input1)
    cur_state_2 = air_or_liquid(input2)
    prev_state_1 = cur_state_1
    prev_state_2 = cur_state_2
    while (cur_state_1 == prev_state_1) or (cur_state_2 == prev_state_2) :        
        input1 = GV.labjack.getAIN(0)
        cur_state_1 = air_or_liquid(input1)
        pos1 =GV.pump1.get_plunger_position(HW.TIRRANT_PUMP_ADDRESS)
        time.sleep(.025)
        input2 = GV.labjack.getAIN(1)
        cur_state_2 = air_or_liquid(input2)
        pos2 =GV.pump1.get_plunger_position(HW.SAMPLE_PUMP_ADDRESS)
        print('        BS1:{:.2f} position:{},   BS2:{:.2f} position:{}'.format(input1,pos1,input2, pos2))
        time.sleep(.025)
        
    GV.pump1.stop(HW.TIRRANT_PUMP_ADDRESS)
    time.sleep(.5)
    GV.pump1.stop(HW.SAMPLE_PUMP_ADDRESS)
    print('\t\tBubble detection terminated')
    GV.pump1.set_speed(HW.TIRRANT_PUMP_ADDRESS,HW.DEFAULT_PUMP_SPEEED)
    time.sleep(.5)
    GV.pump1.set_speed(HW.SAMPLE_PUMP_ADDRESS,HW.DEFAULT_PUMP_SPEEED)







    if (Done == False):        
        GV.SM_TEXT_TO_DIAPLAY = "S10,E1 -> action6_1\n" "  Waiting for bubble sensor to be triggered"
        GV.next_E = 1
    else:        
        str1 = "  bubble sensor triggered" "  pumps stopped" "  go to S10/E2"
        GV.SM_TEXT_TO_DIAPLAY ="S10,E1 -> action10_1\n"+ str1
        GV.next_E = 2


def action10_2():      
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S10,E2 -> action10_1\n" "goint to S10/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S10,E2 -> action10_1\n" "goint to S10/E4"
        return          
  
    str1 = "  prepare to go to S11" "  going to S11/E0"
    GV.SM_TEXT_TO_DIAPLAY ="S10,E2 -> action10_2\n" + str1
    GV.next_E = 0


def action10_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S10,E3 -> action10_3\n" "goint to S10/E4"
        return         
    # print("S4,E3 -> action4_3")    
    GV.SM_TEXT_TO_DIAPLAY = "S10,E3 -> action10_3\n" "  going to PAUSE"
    GV.next_E = 0
    GV.prev_S = 10


def action10_4():    
    GV.SM_TEXT_TO_DIAPLAY ="S10,E4 -> action10_4\n" " going to ERROR state"
    GV.next_E = 0
    GV.prev_S = 10

#-------------------------------------------------------------------------------------------
def action11_0():  
    if (GV.PAUSE == True):
        GV.next_E = 2
        GV.SM_TEXT_TO_DIAPLAY = "S11,E0 -> action11_0\n" "going to S11/E2"
        return 
    if (GV.ERROR == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S11,E0 -> action11_0\n" "going to S11/E3"
        return 
        
    str1 = "  Pump init & reload completed" "  going to S11/E1"
    GV.SM_TEXT_TO_DIAPLAY = "S11,E0 -> action11_0\n" + str1
    GV.next_E = 1


def action11_1():
    
    if (GV.PAUSE == True):
        GV.next_E = 2
        GV.SM_TEXT_TO_DIAPLAY = "S11,E1 -> action11_1\n" "going to S11/E2"
        return 
    if (GV.ERROR == True ):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S11,E1 -> action11_1\n" "going to S11/E3"
        return 
    
    GV.SM_TEXT_TO_DIAPLAY = "Pump_Init_Reload SM terminated"
    GV.next_E = 0
    GV.terminate_SM = True


def action11_2():
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S11,E2 -> action11_2\n" "going to S11/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S11,E2 -> action11_2\n" "going to S11/E4"
        return     
    
    GV.SM_TEXT_TO_DIAPLAY ="S11,E2 -> action11_2\n" "  go to S2/E0 state"
    GV.next_E = 0

    
def action11_3():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY = "S11,E3 -> action11_3\n\tgoing to ERROR state"


#-----------------------------------------------------------------------------  


def action12_0():
    if (GV.ERROR == True):
        GV.next_E = 13
        GV.SM_TEXT_TO_DIAPLAY = "S12,E0 -> action12_0\n" "going to S12/E13"
        return    

    if (GV.PAUSE == True):
        GV.next_E = 0
    else:
        GV.next_E = GV.prev_S

    GV.SM_TEXT_TO_DIAPLAY ="S12,E0 -> action12_0\n"


def action12_1():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S12,E1 -> action12_1" "  going to S0/E0"

def action12_2():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S12,E2 -> action12_2" "  going to S1/E0"

def action12_3():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S12,E3 -> action12_3" "  going to S2/E0"

def action12_4():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S12,E4 -> action12_4" "  going to S3/E0"

def action12_5():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S12,E5 -> action12_5" "  going to S4/E0"

def action12_6():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S12,E6 -> action12_6"  "  going to S5/E0"
    
def action12_7():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S12,E7 -> action12_7"  "  going to S6/E0"

def action12_8():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S12,E8 -> action12_8"  "  going to S7/E0"

def action12_9():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S12,E9 -> action12_9"  "  going to S8/E0"

def action12_10():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S12,E10 -> action12_10"  "  going to S9/E0"

def action12_11():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S12,E11 -> action12_11"  "  going to S10/E0"
def action12_11():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S12,E11 -> action12_11"  "  going to S11/E0"


#--------------
def action13_0():
    print("S13,E0 -> action13_0")
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S13,E0 -> action13_0\n"


#-------------------------------------------------------------
#-------------- END OF ACTIONS -------------------------------
#-------------------------------------------------------------


