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
#-------------   -------E0-------    ------E1-------  -------E2-------  -------E3-------  -------E4-------  -------E5------ -------E6------- -------E7-------  -------E8-------  -------E9-------   -------E10-------  -------E11-------      -------E12-------    -------E13-------
TT = np.array([[( 0, 'action0_0')  ,(0, 'action0_1') ,(0, 'action0_2') ,(1, 'action0_3') ,(12,'action0_4') ,(13, 'action0_5'), (0, 'None')     , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')         ],  #<---STATE0
               [( 1, 'action1_0')  ,(1, 'action1_1') ,(2, 'action1_2') ,(12, 'action1_3'),(13, 'action1_4'),(0, 'None')      , (0, 'None')     , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')         ],  #<---STATE1
               [( 2, 'action2_0')  ,(2, 'action2_1') ,(3, 'action2_2') ,(12,'action2_3') ,(13,'action2_4') ,(0, 'None')      , (0, 'None')     , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')         ],  #<---STATE2
               [( 3, 'action3_0')  ,(3, 'action3_1') ,(4, 'action3_2') ,(12,'action3_3') ,(12,'action3_4') ,(0, 'None')      , (0, 'None')     , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')         ],  #<---STATE3
               [( 4, 'action4_0')  ,(4, 'action4_1') ,(5, 'action4_2') ,(12,'action4_3') ,(13,'action4_4') ,(0, 'None')      , (0, 'None')     , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')         ],  #<---STATE4
               [( 5, 'action5_0')  ,(5, 'action5_1') ,(5, 'action5_2') ,(5, 'action5_3') ,(6, 'action5_4') ,(12, 'action5_5'), (13,'action5_6'),(0, 'None')       , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')         ],  #<---STATE5
               [( 6, 'action6_0')  ,(6, 'action6_1') ,(7, 'action6_2') ,(12,'action6_3') ,(13,'action6_4') ,(0, 'None')      , (0, 'None')     , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')         ],  #<---STATE6
               [( 7, 'action7_0')  ,(7, 'action7_1') ,(8, 'action7_2') ,(12,'action7_3') ,(13,'action7_4') ,(0, 'None')      , (0, 'None')     , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')         ],  #<---STATE7
               [( 8, 'action8_0')  ,(8, 'action8_1') ,(9, 'action8_2') ,(12,'action8_3') ,(13,'action8_4') ,(0, 'None')      , (0, 'None')     , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')         ],  #<---STATE8
               [( 9, 'action9_0')  ,(9, 'action9_1') ,(10,'action9_2') ,(12,'action9_3') ,(13,'action9_4') ,(0, 'None')      , (0, 'None')     , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')         ],  #<---STATE9
               [( 10,'action10_0') ,(10,'action10_1'),(11,'action10_2'),(12,'action10_3'),(13,'action10_4'),(0, 'None')      , (0, 'None')     , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')         ],  #<---STATE10
               [( 11,'action11_0') ,(11,'action11_1'),(12,'action11_2'),(13,'action11_3'),(0, 'None')      ,(0, 'None')      , (0, 'None')     , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')         ],  #<---STATE11
               [( 12,'action12_0') ,(0, 'action12_1'),(1, 'action12_2'),(2, 'action12_3'),(3, 'action12_4'),(4, 'action12_5'), (5, 'action12_6'),(6, 'action12_7'), (7, 'action12_8'), (8, 'action12_9'), (9, 'action12_10'), (10, 'action12_11'), (11, 'action12_12'), (0, 'None')         ],  #<---STATE12
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
    if pump_address == HW.TIRRANT_PUMP_ADDRESS:
        scale_factor = GV.PUMP_TITRANT_SCALING_FACTOR
        pump_speed = int( RECIPE["Func_NewAirSlugs"]["titrant_pump_speed"] * scale_factor)        
    elif pump_address== HW.SAMPLE_PUMP_ADDRESS:
        scale_factor = GV.PUMP_SAMPLE_SCALING_FACTOR
        pump_speed = int(RECIPE["Func_NewAirSlugs"]["sample_pump_speed"] * scale_factor)
    else:
        logger.info("Not a valid pump address")
        exit(1)

    air_slug_total_count = RECIPE["Func_NewAirSlugs"]["AirSlug_Total_count"]
    air_slug_volume = int(RECIPE["Func_NewAirSlugs"]["AirSlug_Volume"] * scale_factor)
    LastAirSlug_Volume = int( RECIPE["Func_NewAirSlugs"]["LastAirSlug_Volume"] * scale_factor)
    WaterSlug_Volume = int(RECIPE["Func_NewAirSlugs"]["WaterSlug_Volume"] * scale_factor)
    GV.pump1.set_speed(pump_address, pump_speed)
    time.sleep(.5)
    airslug_count = 0
    starting_pos = GV.pump1.get_plunger_position(pump_address)
    time.sleep(1)
    next_pos =  starting_pos
    while (airslug_count < air_slug_total_count):        
        logger.info(f"\t\tair slug:{airslug_count+1} / {air_slug_total_count}")
        # Air slug
        time.sleep(1)   
        GV.pump1.set_multiwayvalve(valve_address,HW.VALVE8_P1)        #Valve to Air
        time.sleep(2)   
        next_pos +=  air_slug_volume
        take_slug(pump_address, next_pos)            
        # Water slug
        time.sleep(1)  
        GV.pump1.set_multiwayvalve(valve_address,HW.VALVE8_P2)        #Valve to water
        time.sleep(2)        
        logger.info("water slug:{}".format(airslug_count+1)) 
        next_pos += WaterSlug_Volume
        take_slug(pump_address, next_pos)
        airslug_count += 1
    # valve to air    
    GV.pump1.set_multiwayvalve(valve_address,HW.VALVE8_P1)        #Valve to Air
    time.sleep(1) 
    #Last air slug
    next_pos += LastAirSlug_Volume
    logger.info("Last air slug:")
    take_slug(pump_address,next_pos)


def take_slug(pump_address, next_pos):
    time.sleep(1)
    GV.pump1.set_pos_absolute(pump_address, next_pos)
    time.sleep(1)
    pump_pos = 0
    while( abs (pump_pos - next_pos) > 10):
        time.sleep(1)
        pump_pos = GV.pump1.get_plunger_position(pump_address)
        logger.info(f"\t\tpump pos: {pump_pos}   target: { next_pos}")    
    time.sleep(5)



#---------------  ACTIONS  --------------
def action0_0():
    #seting the scale factor for converting volume to pump position units
    sample_pump_step = RECIPE["PumpInit_Reload"]["sample_pump_step"]
    titrant_pump_step = RECIPE["PumpInit_Reload"]["titrant_pump_step"]
    if sample_pump_step == "full step":
        str0 = 'pump 2: full step'
        GV.PUMP_SAMPLE_SCALING_FACTOR = HW.SAMPLE_PUMP_VOLUM_2_STEP
        GV.pump1.set_microstep_position(HW.SAMPLE_PUMP_ADDRESS,0)
    else:
        str0 = 'pump 2: micro step'
        GV.PUMP_SAMPLE_SCALING_FACTOR = HW.SAMPLE_PUMP_VOLUM_2_MICROSTEP
        GV.pump1.set_microstep_position(HW.SAMPLE_PUMP_ADDRESS,2)
    time.sleep(0.5)
    if titrant_pump_step == "full step":
        str1 = 'pump 1: full step'
        GV.PUMP_TITRANT_SCALING_FACTOR = HW.TITRANT_PUMP_VOLUM_2_STEP
        GV.pump1.set_microstep_position(HW.TIRRANT_PUMP_ADDRESS,0)
    else:
        str1 = 'pump 1: micro step'
        GV.PUMP_TITRANT_SCALING_FACTOR = HW.TITRANT_PUMP_VOLUM_2_MICROSTEP
        GV.pump1.set_microstep_position(HW.TIRRANT_PUMP_ADDRESS,2)

    logger.info("Sample pump scale facotr in {} is :{}".format(str0, GV.PUMP_SAMPLE_SCALING_FACTOR))
    logger.info("Titrant pump scale facotr in {} is :{}".format(str1, GV.PUMP_TITRANT_SCALING_FACTOR))

    GV.VALVE_1 = "Line to Pump"
    GV.VALVE_3 = "Line to Pump"    
    GV.VALVE_5 = "Reservoirs"
    GV.VALVE_2 = "Line to Pump"
    GV.VALVE_4 = "Line to Pump"
    GV.VALVE_7 = "Reservoirs"
    GV.VALVE_8 = "Waste"
    GV.VALVE_9 = "Waste"

    str2 = "  prepare for initialization\n" "  -V1 to LinetoPump\n" "  -V3 to Line to Pump\n"
    str2 = str2 +"  -V5 to Reservoirs\n" "  -V2 to LinetoPump\n" " - V4 to LinetoPump\n" " - V7 to Reservoirs\n"
    str2 = str2 +" - V8 to Waste\n" " - V9 to Waste\n" 

    if (GV.PAUSE == True):
        GV.next_E = 4       
        GV.SM_TEXT_TO_DIAPLAY =  "Prepare to go to Pause State"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY =  "Prepare to go to error State"
        return  
    else:    
        GV.SM_TEXT_TO_DIAPLAY =  str2 + str1 +'\n'+ str0
        GV.next_E = 1


def action0_1():
    GV.pump1.set_valve(HW.TIRRANT_PUMP_ADDRESS, HW.VALVE1_P2)
    time.sleep(.5)
    GV.pump1.set_valve(HW.TITRANT_LOOP_ADDRESS, HW.VALVE3_P3)
    time.sleep(.5)
    # GV.pump1.set_multiwayvalve(HW.TITRANT_PIPETTE_ADDRESS,HW.VALVE5_P3)
    GV.pump1.set_valve(HW.TITRANT_PIPETTE_ADDRESS,HW.VALVE5_P3)
    time.sleep(.5)
    GV.pump1.set_valve(HW.SAMPLE_PUMP_ADDRESS, HW.VALVE2_P3)
    time.sleep(.5)
    GV.pump1.set_valve(HW.SAMPLE_LOOP_ADDRESS, HW.VALVE4_P2)
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.DEGASSER_ADDRESS,HW.VALVE7_P1)        
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.SAMPLE_CLEANING_ADDRESS,HW.VALVE8_P1)    
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.TITRANT_CLEANING_ADDRESS,HW.VALVE9_P6)        
    time.sleep(.5)
    pump1_speed = int(RECIPE["PumpInit_Reload"]["titrant_pump_speed"] * GV.PUMP_TITRANT_SCALING_FACTOR)
    pump2_speed = int(RECIPE["PumpInit_Reload"]["sample_pump_speed"] * GV.PUMP_SAMPLE_SCALING_FACTOR)
    GV.pump1.set_speed(HW.TIRRANT_PUMP_ADDRESS, pump1_speed)
    time.sleep(1)
    GV.pump1.set_speed(HW.SAMPLE_PUMP_ADDRESS, pump2_speed)
    time.sleep(1)    
    if (GV.PAUSE == True):
        GV.next_E = 4       
        GV.SM_TEXT_TO_DIAPLAY = "Prepare to go to Pause State"
        return 
    if (GV.ERROR == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY =  "Prepare to go to error State"
        return 
    else:
        GV.SM_TEXT_TO_DIAPLAY =  "system initialized"    
        GV.next_E = 2


def action0_2():
    timeout = False
    Done = True #False
    if (GV.PAUSE == True):
        GV.next_E = 4       
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True or timeout == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "going to Error state"
        return 
    elif (Done == False):
        GV.next_E = 2
        GV.SM_TEXT_TO_DIAPLAY =  "  Waiting for valves to reach positions"
    else:
        GV.SM_TEXT_TO_DIAPLAY =  "  Valves in Position" 
        GV.next_E = 3


def action0_3():
    if (GV.PAUSE == True):
        GV.next_E = 4       
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return 
    else:
        GV.SM_TEXT_TO_DIAPLAY =  "  Init. Titran Pump\n" "  Init. Sample Pump"      
        GV.next_E = 0


def action0_4():
    if (GV.ERROR == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY =" going to ERROR state"
        return  
    else:   
        GV.next_E = 0
        GV.prev_S = 0
        GV.SM_TEXT_TO_DIAPLAY ="going to Pause state"
    
    
def action0_5():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY = "going to ERROR state"


#-------------------------------------------------------------------------------------------
def action1_0():  
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY =  "going to Error State"
        return 
    else:
        GV.SM_TEXT_TO_DIAPLAY =  "  Init. Titran Pump\n" "  Init. Sample Pump\n" "  Waiting for Pumps to initialize"
        GV.next_E = 1


def action1_1():
    timeout = False
    GV.pump1.set_pump_assignment(HW.TIRRANT_PUMP_ADDRESS)
    GV.pump1.pump_Zinit(HW.TIRRANT_PUMP_ADDRESS)
    time.sleep(3)
    GV.pump1.pump_Zinit(HW.SAMPLE_PUMP_ADDRESS)    
    time.sleep(3)
    #Turn on the home LEDs for both pumps
    GV.pump1_titrant_homed_led     = True    
    GV.pump2_sample_homed_led      = True
    GV.SM_TEXT_TO_DIAPLAY =  "Pumps initialized" 

    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY ="going to Pause state"
        return 
    elif (GV.ERROR == True or timeout==True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return 
    else:
        GV.next_E = 2


def action1_2():
    time.sleep(3)
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return     
    else:
        GV.next_E = 0


def action1_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return     
    else:
        GV.SM_TEXT_TO_DIAPLAY ="going to PAUSE state"
        GV.next_E = 0
        GV.prev_S = 1
        
    
def action1_4():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY = "going to ERROR state"


#----------------------------------------------------------------   
def action2_0():
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return 
    else:
        str1= "V2- GastoLine\n" "V4- LinetoGas\n" "V6- LinetoGas\n" "V7- Reservoirs\n" "V8- Waste\n"
        str1 = str1 + "V1- Gas to Line\n" "V3- Gas to Line\n" "V5- Reservoirs\n" "V9- Waste\n"
        GV.SM_TEXT_TO_DIAPLAY =str1
        GV.next_E = 1

def action2_1():
    timeout = False 
    GV.VALVE_2 = "GastoLine"
    GV.VALVE_4 = "LinetoGas"    
    GV.VALVE_6 = "LinetoGas"
    GV.VALVE_7 = "Reservoirs"
    GV.VALVE_8 = "Waste"
    GV.VALVE_1 = "Gas to Line"
    GV.VALVE_3 = "Gas to Line"
    GV.VALVE_5 = "Reservoirs"
    GV.VALVE_9 = "Waste"
    GV.pump1.set_valve(HW.TIRRANT_PUMP_ADDRESS, HW.VALVE1_P1)
    time.sleep(.5)
    GV.pump1.set_valve(HW.TITRANT_LOOP_ADDRESS, HW.VALVE3_P3)
    time.sleep(.5)
    # GV.pump1.set_multiwayvalve(HW.TITRANT_PIPETTE_ADDRESS,HW.VALVE5_P3)
    GV.pump1.set_valve(HW.TITRANT_PIPETTE_ADDRESS,HW.VALVE5_P3)
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.TITRANT_CLEANING_ADDRESS,HW.VALVE9_P6) 
    time.sleep(.5)
    GV.pump1.set_valve(HW.SAMPLE_PUMP_ADDRESS, HW.VALVE2_P4)
    time.sleep(.5)
    GV.pump1.set_valve(HW.SAMPLE_LOOP_ADDRESS, HW.VALVE4_P2)
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.DEGASSER_ADDRESS,HW.VALVE7_P1)        
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.SAMPLE_CLEANING_ADDRESS,HW.VALVE8_P1)    
    time.sleep(.5)

    if (GV.PAUSE == True):
        GV.next_E = 3           
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True or timeout==True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return 
    else:
        GV.SM_TEXT_TO_DIAPLAY = "  Valves in position\n" 
        GV.next_E = 2
        time.sleep(5)
        logger.debug("end of S2. going to S3")
    
def action2_2():
    if (GV.PAUSE == True):
        GV.next_E = 3           
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True ):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return   
    else:
        GV.next_E = 0


def action2_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY =  "Prepare to go to error State"
        return    
    else:     
        GV.next_E = 0
        GV.prev_S = 2
        GV.SM_TEXT_TO_DIAPLAY = "going to PAUSE state "
        logger.debug("cur. state: 2, going to pause state.  GV.prevS={}".format(GV.prev_S))

def action2_4():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY = "  goint to ERROR state"


#----------------------------------------------------------------
def action3_0():
    if (GV.PAUSE == True):
        GV.next_E = 3          
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return 
    else:
        GV.next_E = 1
        GV.SM_TEXT_TO_DIAPLAY ="Please press NEXT button to continue..."
        GV.activate_NEXT_button = True


def action3_1():
    if (GV.PAUSE == True):
        GV.next_E = 3        
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return         
    elif (GV.NEXT == False):
        GV.SM_TEXT_TO_DIAPLAY ="wait for NEXT button to be pressed..."
        GV.next_E = 1
    else:    
        GV.SM_TEXT_TO_DIAPLAY ="Next button pressed"
        GV.NEXT = False
        GV.activate_NEXT_button = False
        GV.next_E = 2


def action3_2():
    if (GV.PAUSE == True):
        GV.next_E = 3        
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return 
    else:
        # str1 = "  -V1 to PumptoLine\n" "  -V3 to PumptoLine\n""  -V5 to Reservoirs\n" "  -V9 to Water\n"
        # str1 = str1 +"  -V6 to V7\n" "  -V2 to PumptoLine\n" "  -V4 to PumptoLine\n" "  -V7 to Reservoirs\n" "  -V8 to Water"
        # GV.SM_TEXT_TO_DIAPLAY = str1
        GV.next_E = 0


def action3_3():
    if (GV.ERROR == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return 
    else:
        GV.SM_TEXT_TO_DIAPLAY ="going to Pause state"
        GV.next_E = 0
        GV.prev_S = 3
        logger.debug("cur. state: 3, going to pause state.  GV.prevS={}".format(GV.prev_S))


def action3_4():
    GV.SM_TEXT_TO_DIAPLAY =" going to ERROR state"
    GV.next_E = 0
    GV.prev_S = 3
    

#---------------------------------------------------------------------------------------
def action4_0():
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return 
    else:
        str1 = "  -V1 to PumptoLine\n" "  -V3 to PumptoLine\n""  -V5 to Reservoirs\n" "  -V9 to Water\n"
        str1 = str1 +"  -V6 to V7\n" "  -V2 to PumptoLine\n" "  -V4 to PumptoLine\n" "  -V7 to Reservoirs\n" "  -V8 to Water"
        GV.SM_TEXT_TO_DIAPLAY = str1
        GV.next_E = 1


def action4_1():
    GV.VALVE_1 = "Pump to Line"
    GV.VALVE_3 = "Pump to LIne"
    GV.VALVE_5 = "Reservoirs"
    GV.VALVE_9 = "Water"
    GV.VALVE_6 = "V7"
    GV.VALVE_2 = "Pump to Line"
    GV.VALVE_4 = "Pump to Line"
    GV.VALVE_7 = "Reservoirs"
    GV.VALVE_8 = "Water"
    GV.pump1.set_valve(HW.TIRRANT_PUMP_ADDRESS, HW.VALVE1_P2)
    time.sleep(.5)
    GV.pump1.set_valve(HW.TITRANT_LOOP_ADDRESS, HW.VALVE3_P3)
    time.sleep(.5)
    # GV.pump1.set_multiwayvalve(HW.TITRANT_PIPETTE_ADDRESS,HW.VALVE5_P3)
    GV.pump1.set_valve(HW.TITRANT_PIPETTE_ADDRESS,HW.VALVE5_P3)
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.TITRANT_CLEANING_ADDRESS,HW.VALVE9_P3)        
    time.sleep(.5)
    GV.pump1.set_valve(HW.SAMPLE_PUMP_ADDRESS, HW.VALVE2_P3)
    time.sleep(.5)
    GV.pump1.set_valve(HW.SAMPLE_LOOP_ADDRESS, HW.VALVE4_P2)
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.DEGASSER_ADDRESS,HW.VALVE7_P1)        
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.SAMPLE_CLEANING_ADDRESS, HW.VALVE8_P4)    
    time.sleep(.5)     

    if (GV.PAUSE == True ):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return 
    else:
        GV.next_E = 2        
        GV.SM_TEXT_TO_DIAPLAY ="  Valves reached position\n"
        time.sleep(5)

def action4_2():      
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return          
    else:
        GV.SM_TEXT_TO_DIAPLAY ="going to S5/E0"
        GV.next_E = 0


def action4_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return         
    else:
        logger.info("S4,E3 -> action4_3")    
        GV.SM_TEXT_TO_DIAPLAY =  "going to PAUSE"
        GV.next_E = 0
        GV.prev_S = 4
        logger.debug("cur. state: 4, going to pause state.  GV.prevS={}".format(GV.prev_S))


def action4_4():    
    GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
    GV.next_E = 0
    GV.prev_S = 4


#------------------------------------------------------------------------------------ 
def action5_0():
    if (GV.PAUSE == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return    
    else:
        #Turn on the pump active LEDs    
        GV.pump1_titrant_active_led    = True
        GV.pump2_sample_active_led     = True
        GV.SM_TEXT_TO_DIAPLAY = "Pump 1 pickup\n" "Pump 2 pickup"
        GV.next_E = 1


def action5_1():
    timeout_flag = False
    bubble_pickup_timeout = RECIPE["PumpInit_Reload"]["pump_move_timeout"]
    logger.info('Pickup until bubble')
    GV.pump1.set_speed(HW.TIRRANT_PUMP_ADDRESS, HW.BUBBLE_DETECTION_PUMP_SPEED)
    time.sleep(1)        
    GV.pump1.set_speed(HW.SAMPLE_PUMP_ADDRESS, HW.BUBBLE_DETECTION_PUMP_SPEED)
    time.sleep(1)        
    GV.pump1.set_pos_absolute(HW.TIRRANT_PUMP_ADDRESS, HW.PICKUP_UNTIL_BUBBLE_TARGET_TITRANT)
    time.sleep(1)
    GV.pump1.set_pos_absolute(HW.SAMPLE_PUMP_ADDRESS, HW.PICKUP_UNTIL_BUBBLE_TARGET_SAMPLE)
    time.sleep(1)
    input1 = GV.labjack.getAIN(HW.BS1_IO_PORT)      #bubble sensor 1
    input2 = GV.labjack.getAIN(HW.BS2_IO_PORT)      #bubble sensor 2
    #check if the bubble semsor detect air or liquid
    cur_state_1 = air_or_liquid(input1)
    cur_state_2 = air_or_liquid(input2)
    prev_state_1 = cur_state_1
    prev_state_2 = cur_state_2
    bubble_1_search = True
    bubble_2_search = True    
    start_time = time.time()
    wait_time = 0
    while (bubble_1_search  or bubble_2_search)  :
        #bubble sensor 1 & Pump 1
        input1 = GV.labjack.getAIN(HW.BS1_IO_PORT)      
        cur_state_1 = air_or_liquid(input1)
        if (cur_state_1 != prev_state_1):
            bubble_1_search = False
            #Stop  pump1
            time.sleep(.5)
            GV.pump1.stop(HW.TIRRANT_PUMP_ADDRESS)
        time.sleep(.025)
        pos1 =GV.pump1.get_plunger_position(HW.TIRRANT_PUMP_ADDRESS)
        #bubble sensor 2 and Pump 2
        input2 = GV.labjack.getAIN(HW.BS2_IO_PORT)
        cur_state_2 = air_or_liquid(input2)        
        if (cur_state_2 != prev_state_2):
            bubble_2_search = False
            time.sleep(.5)
            GV.pump1.stop(HW.SAMPLE_PUMP_ADDRESS)
        time.sleep(.025)
        pos2 =GV.pump1.get_plunger_position(HW.SAMPLE_PUMP_ADDRESS)
        logger.info('\t\tBS1:{:.2f}  position:{},   BS2:{:.2f}  position:{}'.format(input1,pos1,input2, pos2))
        wait_time = time.time() - start_time
        if (wait_time >  bubble_pickup_timeout):
            logger.error("\t\tpickup timeout. going to Pause state")
            timeout_flag = True
            break

    #Stop both pumps
    # GV.pump1.stop(HW.TIRRANT_PUMP_ADDRESS)
    # time.sleep(.5)
    # GV.pump1.stop(HW.SAMPLE_PUMP_ADDRESS)
    logger.info('\t\tBubble detection terminated')
    #set pumps speeds to their defaults
    pump1_speed = int(RECIPE["PumpInit_Reload"]["titrant_pump_speed"] * GV.PUMP_TITRANT_SCALING_FACTOR)
    pump2_speed = int( RECIPE["PumpInit_Reload"]["sample_pump_speed"] * GV.PUMP_SAMPLE_SCALING_FACTOR)
    time.sleep(0.5)
    GV.pump1.set_speed(HW.TIRRANT_PUMP_ADDRESS, pump1_speed)
    time.sleep(0.5)
    GV.pump1.set_speed(HW.SAMPLE_PUMP_ADDRESS, pump2_speed)
    time.sleep(0.5)

    if (GV.PAUSE == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True ):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return    
    elif (timeout_flag == True):
        GV.SM_TEXT_TO_DIAPLAY ="Pickup timeout.\n going to Pause state"
        GV.PAUSE = True
        GV.next_E = 5
    else:
        GV.SM_TEXT_TO_DIAPLAY ="pump 1 to position XX\n""pump 2 to position XX"
        GV.next_E = 2
    

def action5_2():   
    #Send pumps to positions
    titrant_target_raw =RECIPE['PumpInit_Reload']['TitrantPumpt_syringe_fill_volume']
    sample_target_raw = RECIPE['PumpInit_Reload']['SamplePumpt_syringe_fill_volume']    
    fill_pos_titrant = int(titrant_target_raw * GV.PUMP_TITRANT_SCALING_FACTOR )
    fill_pos_sample = int( sample_target_raw * GV.PUMP_SAMPLE_SCALING_FACTOR )
    logger.info("Target Titrant pump pos.   before scaling: {}, after scaling {}".format(titrant_target_raw,
                                                                                        fill_pos_titrant) )
    logger.info("Target Sample pump pos.   before scaling: {}, after scaling {}".format(sample_target_raw,
                                                                                        fill_pos_sample) )
    starting_pos_titrant = GV.pump1.get_plunger_position(HW.TIRRANT_PUMP_ADDRESS)  
    time.sleep(0.5)
    starting_pos_sample = GV.pump1.get_plunger_position(HW.SAMPLE_PUMP_ADDRESS)  
    time.sleep(0.5)
    target_pos_titrant = starting_pos_titrant + fill_pos_titrant
    target_pos_sample = starting_pos_sample + fill_pos_sample
    GV.pump1.set_pos_absolute(HW.TIRRANT_PUMP_ADDRESS, target_pos_titrant)
    time.sleep(.5)
    GV.pump1.set_pos_absolute(HW.SAMPLE_PUMP_ADDRESS, target_pos_sample)
    time.sleep(.5)               
    # Wait until pumps reach targets
    cur_pump_pos1 = 0
    cur_pump_pos2 = 0
    pump1_away_from_target = True
    pump2_away_from_target = True
    while(  pump1_away_from_target or pump2_away_from_target ):
        cur_pump_pos1 = GV.pump1.get_plunger_position(HW.TIRRANT_PUMP_ADDRESS)
        pump1_away_from_target = (abs (cur_pump_pos1 - target_pos_titrant) > 5)
        time.sleep(.5)
        cur_pump_pos2 = GV.pump1.get_plunger_position(HW.SAMPLE_PUMP_ADDRESS)
        pump2_away_from_target = (abs (cur_pump_pos2 - target_pos_sample) > 5)
        time.sleep(.5)
        logger.info("\t\tPump1 cur pos: {}, target: {},   pump2 cur pos: {},  target: {}".format(cur_pump_pos1,target_pos_titrant,
                                                                                 cur_pump_pos2, target_pos_sample))
    # Pumps are now in positions                                      
        
    if (GV.PAUSE == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return 
    else:
        GV.SM_TEXT_TO_DIAPLAY = "Pump 1 position \n" "Pump 2 to position\n ""  Waiting for pumps to reach positions..."
        GV.next_E = 3


def action5_3():
    timeout = False
    if (GV.PAUSE == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True  or timeout==True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return    
    else:
        GV.SM_TEXT_TO_DIAPLAY = "pumps in position"
        GV.next_E = 4


def action5_4():
    if (GV.PAUSE == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY =" going to ERROR state"
        return    
    else:
        # Turn of pumps active LEDs
        GV.pump1_titrant_active_led    = False
        GV.pump2_sample_active_led     = False
        GV.SM_TEXT_TO_DIAPLAY = "-V1 to PumptoAir\n" "-V2 to PumptoAir"
        GV.next_E = 0


def action5_5():
    if (GV.ERROR == True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = "S5,E5 -> action5_5\n" "   goint to S5/E6"
        return     
    else:
        GV.SM_TEXT_TO_DIAPLAY ="S5,E2 -> action5_2 \n----> going to PAUSE state"
        GV.next_E = 0
        GV.prev_S = 5
        logger.debug("cur. state: 5, going to pause state.  GV.prevS={}".format(GV.prev_S))
    

def action5_6():
    GV.SM_TEXT_TO_DIAPLAY ="S5,E6 -> action5_6\n"
    GV.next_E = 0
    GV.prev_S = 5


#-------------------------------------------------------------------------------
def action6_0():
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return 
    else:
        GV.SM_TEXT_TO_DIAPLAY = "-V1 to PumptoAir\n""-V2 to PumptoAir"
        GV.next_E = 1


def action6_1():
    timeout = False
    GV.pump1.set_valve(HW.TIRRANT_PUMP_ADDRESS, HW.VALVE1_P3)
    time.sleep(.5)
    GV.pump1.set_valve(HW.SAMPLE_PUMP_ADDRESS, HW.VALVE2_P2)
    time.sleep(.5)
    GV.VALVE_1 = "Pump to Air"
    GV.VALVE_2 = "Pump to Air"
    GV.SM_TEXT_TO_DIAPLAY ="  Valves reached position\n" "  go to S6/E2"

    if (GV.PAUSE == True or timeout==True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return 
    else:
        GV.next_E = 2


def action6_2():      
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return  
    else:
        GV.SM_TEXT_TO_DIAPLAY = "pump 1 to position \n""pump 2 to position "
        GV.next_E = 0


def action6_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY ="going to Pause state"
        return         
    else:
        # logger.info("S4,E3 -> action4_3")    
        GV.SM_TEXT_TO_DIAPLAY = "  going to PAUSE"
        GV.next_E = 0
        GV.prev_S = 6


def action6_4():    
    GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
    GV.next_E = 0
    GV.prev_S = 6


#-----------------------------------------------------------------------------        
def action7_0():
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY ="going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY =" going to ERROR state"
        return 
    else:
        GV.pump1_titrant_active_led    = True
        GV.pump2_sample_active_led     = True
        GV.SM_TEXT_TO_DIAPLAY ="  pump 1 to position \n""  pump 2 to position "
        GV.next_E = 1


def action7_1():
    Done = True
    timeout = False
    # Pumps to positions
    fill_pos_titrant =int( RECIPE['PumpInit_Reload']['TitrantPumpt_syringe_fill_volume'] * GV.PUMP_TITRANT_SCALING_FACTOR )
    fill_pos_sample =int( RECIPE['PumpInit_Reload']['SamplePumpt_syringe_fill_volume'] * GV.PUMP_SAMPLE_SCALING_FACTOR )
    starting_pos_titrant = GV.pump1.get_plunger_position(HW.TIRRANT_PUMP_ADDRESS)  
    starting_pos_sample = GV.pump1.get_plunger_position(HW.SAMPLE_PUMP_ADDRESS)  
    target_pos_titrant = starting_pos_titrant - fill_pos_titrant
    target_pos_sample = starting_pos_sample - fill_pos_sample
    GV.pump1.set_pos_absolute(HW.TIRRANT_PUMP_ADDRESS, target_pos_titrant)
    time.sleep(.5)
    GV.pump1.set_pos_absolute(HW.SAMPLE_PUMP_ADDRESS, target_pos_sample)
    time.sleep(.5)
    # Wait until pumps fimish their move
    cur_pump_pos1 = 0
    cur_pump_pos2 = 0
    pump1_away_from_target = True
    pump2_away_from_target = True
    while(  pump1_away_from_target or pump2_away_from_target ):
        cur_pump_pos1 = GV.pump1.get_plunger_position(HW.TIRRANT_PUMP_ADDRESS)
        pump1_away_from_target = (abs (cur_pump_pos1 - target_pos_titrant) > 5)
        time.sleep(.5)
        cur_pump_pos2 = GV.pump1.get_plunger_position(HW.SAMPLE_PUMP_ADDRESS)
        pump2_away_from_target = (abs (cur_pump_pos2 - target_pos_sample) > 5)
        time.sleep(.5)
        logger.info("\t\tPump1 cur pos: {}, target: {},   pump2 cur pos: {},  target: {}".format(cur_pump_pos1,target_pos_titrant,
                                                                                 cur_pump_pos2, target_pos_sample))
    # Pumps are in positin now. Turn off the pumps active LEDs
    GV.pump1_titrant_active_led    = False
    GV.pump2_sample_active_led     = False

    if (GV.PAUSE == True or timeout==True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return     
    elif (Done == False):        
        GV.SM_TEXT_TO_DIAPLAY = "  Waiting for pumps to reach positions"
        GV.next_E = 1
    else:        
        GV.SM_TEXT_TO_DIAPLAY ="  pumps reached position\n" 
        GV.next_E = 2


def action7_2():      
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return  
    else:
        GV.pump1_titrant_active_led    = False
        GV.pump2_sample_active_led     = True    
        GV.SM_TEXT_TO_DIAPLAY ="Sample pump:\n Run function NewAirSlugs\n"
        GV.next_E = 0


def action7_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return         
    else:
        # logger.info("S4,E3 -> action4_3")    
        GV.SM_TEXT_TO_DIAPLAY =  "  going to PAUSE"
        GV.next_E = 0
        GV.prev_S = 7


def action7_4():    
    GV.SM_TEXT_TO_DIAPLAY =" going to ERROR state"
    GV.next_E = 0
    GV.prev_S = 7


#-----------------------------------------------------------------------------      
def action8_0():
    # Run new air slug
    pump_address = HW.SAMPLE_PUMP_ADDRESS
    valve_address = HW.SAMPLE_CLEANING_ADDRESS
    NewAirSlugs(pump_address, valve_address)
    GV.pump1_titrant_active_led    = True
    GV.pump2_sample_active_led     = False    
    GV.SM_TEXT_TO_DIAPLAY ="titrant pump: run function NewAirSlugs\n""  Waiting for pumps to finish functions"
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return 
    else:
        GV.next_E = 1


def action8_1():
    timeout = False
    # Run new air slug
    pump_address = HW.TIRRANT_PUMP_ADDRESS
    valve_address = HW.TITRANT_CLEANING_ADDRESS
    NewAirSlugs(pump_address, valve_address)
    GV.pump1_titrant_active_led    = False
    GV.pump2_sample_active_led     = False   
    GV.SM_TEXT_TO_DIAPLAY = "Pumps completed functions\n" 
    if (GV.PAUSE == True or timeout==True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return 
    else:
        GV.next_E = 2


def action8_2():      
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return          
    else:
        GV.SM_TEXT_TO_DIAPLAY = "  V8 to Air\n" "  V9 to Air"
        GV.next_E = 0


def action8_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return
    else:
        # logger.info("S4,E3 -> action4_3")    
        GV.SM_TEXT_TO_DIAPLAY = "  going to PAUSE"
        GV.next_E = 0
        GV.prev_S = 8


def action8_4():    
    GV.SM_TEXT_TO_DIAPLAY =" going to ERROR state"
    GV.next_E = 0
    GV.prev_S = 8

#-----------------------------------------------------------------------------  
def action9_0():
    GV.VALVE_8 = "Air"
    GV.VALVE_9 = "Air"
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.SAMPLE_CLEANING_ADDRESS, HW.VALVE8_P6)        
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.TITRANT_CLEANING_ADDRESS, HW.VALVE9_P2)    
    time.sleep(.5)
    GV.SM_TEXT_TO_DIAPLAY ="  Waiting for valves to reach positions"
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY ="going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return 
    else:
        GV.next_E = 1


def action9_1():
    timeout = False
    if (GV.PAUSE == True or timeout==True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return 
    else:
        GV.SM_TEXT_TO_DIAPLAY =  "  valves reached position\n"  
        GV.next_E = 2


def action9_2():      
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return  
    else:
        str1 = "  prepare to go to S10\n" 
        GV.SM_TEXT_TO_DIAPLAY =str1
        GV.next_E = 0


def action9_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return         
    else:
        # logger.info("S4,E3 -> action4_3")    
        GV.SM_TEXT_TO_DIAPLAY =   "  going to PAUSE"
        GV.next_E = 0
        GV.prev_S = 9


def action9_4():    
    GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
    GV.next_E = 0
    GV.prev_S = 9

#-----------------------------------------------------------------------------  

def action10_0():
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return 
    else:
        GV.pump1_titrant_active_led    = True
        GV.pump2_sample_active_led     = True
        GV.SM_TEXT_TO_DIAPLAY = "  pump 1 pickup\n" "  pump 2 pickup"
        # print(GV.SM_TEXT_TO_DIAPLAY)
        GV.next_E = 1


def action10_1():
    timeout_flag = False    
    bubble_pickup_timeout = RECIPE["PumpInit_Reload"]["pump_move_timeout"]    
    logger.info('Pickup until bubble')
    GV.pump1.set_speed(HW.TIRRANT_PUMP_ADDRESS, HW.BUBBLE_DETECTION_PUMP_SPEED)
    time.sleep(1)        
    GV.pump1.set_speed(HW.SAMPLE_PUMP_ADDRESS, HW.BUBBLE_DETECTION_PUMP_SPEED)
    time.sleep(1)        
    GV.pump1.set_pos_absolute(HW.TIRRANT_PUMP_ADDRESS, HW.PICKUP_UNTIL_BUBBLE_TARGET_TITRANT)
    time.sleep(1)
    GV.pump1.set_pos_absolute(HW.SAMPLE_PUMP_ADDRESS, HW.PICKUP_UNTIL_BUBBLE_TARGET_SAMPLE)
    time.sleep(1)
    input1 = GV.labjack.getAIN(HW.BS3_IO_PORT)   #bubble sensor 3
    input2 = GV.labjack.getAIN(HW.BS4_IO_PORT)   #bubble sensor 4
    #check if the bubble sensors detect transitions from air or liquid
    cur_state_1 = air_or_liquid(input1)
    cur_state_2 = air_or_liquid(input2)
    prev_state_1 = cur_state_1
    prev_state_2 = cur_state_2
    bubble_1_search = True
    bubble_2_search = True
    start_time = time.time()
    wait_time = 0    
    while (bubble_1_search  or bubble_2_search) :
        # check bs3
        input1 = GV.labjack.getAIN(HW.BS3_IO_PORT)   #bubble sensor 3
        cur_state_1 = air_or_liquid(input1)
        pos1 =GV.pump1.get_plunger_position(HW.TIRRANT_PUMP_ADDRESS)
        if (cur_state_1 != prev_state_1):
            bubble_1_search = False
            GV.pump1.stop(HW.TIRRANT_PUMP_ADDRESS)
            time.sleep(.5)
        time.sleep(.025)
        #check bs 4
        input2 = GV.labjack.getAIN(HW.BS4_IO_PORT)   #bubble sensor 4
        cur_state_2 = air_or_liquid(input2)
        pos2 =GV.pump1.get_plunger_position(HW.SAMPLE_PUMP_ADDRESS)
        if (cur_state_2 != prev_state_2):
            bubble_2_search = False
            GV.pump1.stop(HW.SAMPLE_PUMP_ADDRESS)
            time.sleep(.5)
        time.sleep(.025)
        logger.info('        BS3:{:.2f}  position:{},   BS4:{:.2f}  position:{}'.format(input1,pos1,input2, pos2))
        wait_time = time.time() - start_time
        if (wait_time >  bubble_pickup_timeout):
            logger.error("\t\tpickup timeout. going to Pause state")
            timeout_flag = True
            break

    # # Stop pumps
    # GV.pump1.stop(HW.TIRRANT_PUMP_ADDRESS)
    # time.sleep(.5)
    # GV.pump1.stop(HW.SAMPLE_PUMP_ADDRESS)
    logger.info('\t\tBubble detection terminated')
    pump1_speed = int(RECIPE["PumpInit_Reload"]["titrant_pump_speed"] * GV.PUMP_TITRANT_SCALING_FACTOR)
    pump2_speed = int(RECIPE["PumpInit_Reload"]["sample_pump_speed"] * GV.PUMP_SAMPLE_SCALING_FACTOR)
    GV.pump1.set_speed(HW.TIRRANT_PUMP_ADDRESS, pump1_speed)
    time.sleep(1)
    GV.pump1.set_speed(HW.SAMPLE_PUMP_ADDRESS, pump2_speed)
    time.sleep(1)
    #Turn off pumps LEDs
    GV.pump1_titrant_active_led    = False
    GV.pump2_sample_active_led     = False
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return     
    elif (timeout_flag == True):
        GV.SM_TEXT_TO_DIAPLAY ="Pickup timeout.\n going to Pause state"
        GV.PAUSE = True
        GV.next_E = 3
    else:    
        GV.SM_TEXT_TO_DIAPLAY ="  bubble sensor triggered" "  pumps stopped" 
        GV.next_E = 2
        print(GV.SM_TEXT_TO_DIAPLAY)


def action10_2():      
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return  
    else:
        GV.SM_TEXT_TO_DIAPLAY ="  prepare to go to S11"  
        # print(GV.SM_TEXT_TO_DIAPLAY)
        GV.next_E = 0


def action10_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
        return 
    else:        
        GV.SM_TEXT_TO_DIAPLAY = "  going to PAUSE"
        # print(GV.SM_TEXT_TO_DIAPLAY)
        GV.next_E = 0
        GV.prev_S = 10


def action10_4():    
    GV.SM_TEXT_TO_DIAPLAY =" going to ERROR state"
    # print(GV.SM_TEXT_TO_DIAPLAY)
    GV.next_E = 0
    GV.prev_S = 10

#-------------------------------------------------------------------------------------------
def action11_0():  
    if (GV.PAUSE == True):
        GV.next_E = 2
        GV.SM_TEXT_TO_DIAPLAY ="going to Pause state"
        return 
    elif (GV.ERROR == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to error state"
        return         
    else:
        GV.SM_TEXT_TO_DIAPLAY =  "Pump init & reload completed"
        GV.next_E = 1


def action11_1():    
    if (GV.PAUSE == True):
        GV.next_E = 2
        GV.SM_TEXT_TO_DIAPLAY ="going to Pause state"
        return 
    elif (GV.ERROR == True ):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to error state"
        return     
    else:
        GV.SM_TEXT_TO_DIAPLAY = "Pump_Init_Reload SM terminated"
        GV.next_E = 0
        GV.terminate_SM = True


def action11_2():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "going to error state"
        return  
    else:   
        GV.SM_TEXT_TO_DIAPLAY = "going to Pause state"
        GV.next_E = 0

    
def action11_3():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="going to ERROR state"


#-----------------------------------------------------------------------------  


def action12_0():
    if (GV.ERROR == True):
        GV.next_E = 13
        GV.SM_TEXT_TO_DIAPLAY = "System Paused"
        return    

    if (GV.PAUSE == True):
        GV.next_E = 0
    else:
        GV.next_E = GV.prev_S + 1

    str1 = "Press Resume to return to state {}".format(GV.prev_S)
    GV.SM_TEXT_TO_DIAPLAY ="Pause state (S12,E0 -> action12_0)\n" + str1



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
def action12_12():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S12,E11 -> action12_11"  "  going to S11/E0"


#--------------
def action13_0():    
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="System in Error state"


#-------------------------------------------------------------
#-------------- END OF ACTIONS -------------------------------
#-------------------------------------------------------------


