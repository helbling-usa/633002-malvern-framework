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
TT = np.array([[( 1, 'action0_0')  ,(0, 'None')       ,(0, 'None')       ,(1, 'None')       ,(12,'None')       ,(13, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')        , (0, 'None')      , (0, 'None')      , (0, 'None')      ,(0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')       , (0, 'None')       , (0, 'None')          ],  #<---STATE0
               [( 1, 'action1_0')  ,(1, 'action1_1')  ,(2, 'action1_2')  ,(23, 'action1_3') ,(24, 'action1_4') ,(0, 'None')       , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')        , (0, 'None')      , (0, 'None')      , (0, 'None')      ,(0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')       , (0, 'None')       , (0, 'None')          ],  #<---STATE1
               [( 2, 'action2_0')  ,(2, 'action2_1')  ,(2, 'action2_2')  ,(2,'action2_3')   ,(3,'action2_4')   ,(23, 'action2_5') , (24, 'action2_6'), (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')        , (0, 'None')      , (0, 'None')      , (0, 'None')      ,(0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')       , (0, 'None')       , (0, 'None')          ],  #<---STATE2
               [( 3, 'action3_0')  ,(3, 'action3_1')  ,(4, 'action3_2')  ,(23,'action3_3')  ,(24,'action3_4')  ,(0, 'None')       , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')        , (0, 'None')      , (0, 'None')      , (0, 'None')      ,(0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')       , (0, 'None')       , (0, 'None')          ],  #<---STATE3
               [( 4, 'action4_0')  ,(4, 'action4_1')  ,(5, 'action4_2')  ,(23,'action4_3')  ,(24,'action4_4')  ,(0, 'None')       , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')        , (0, 'None')      , (0, 'None')      , (0, 'None')      ,(0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')       , (0, 'None')       , (0, 'None')          ],  #<---STATE4
               [( 5, 'action5_0')  ,(5, 'action5_1')  ,(6, 'action5_2')  ,(23, 'action5_3') ,(24, 'action5_4') ,(0, 'None')       , (0,'None')       , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')        , (0, 'None')      , (0, 'None')      , (0, 'None')      ,(0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')       , (0, 'None')       , (0, 'None')          ],  #<---STATE5
               [( 6, 'action6_0')  ,(6, 'action6_1')  ,(7, 'action6_2')  ,(23,'action6_3')  ,(24,'action6_4')  ,(0, 'None')       , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')        , (0, 'None')      , (0, 'None')      , (0, 'None')      ,(0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')       , (0, 'None')       , (0, 'None')          ],  #<---STATE6
               [( 7, 'action7_0')  ,(7, 'action7_1')  ,(8, 'action7_2')  ,(23,'action7_3')  ,(24,'action7_4')  ,(0, 'None')       , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')        , (0, 'None')      , (0, 'None')      , (0, 'None')      ,(0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')       , (0, 'None')       , (0, 'None')          ],  #<---STATE7               
               [( 8, 'action8_0')  ,(8, 'action8_1')  ,(9, 'action8_2')  ,(23,'action8_3')  ,(24,'action8_4')  ,(0, 'None')       , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')        , (0, 'None')      , (0, 'None')      , (0, 'None')      ,(0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')       , (0, 'None')       , (0, 'None')          ],  #<---STATE8
               [( 9, 'action9_0')  ,(9, 'action9_1')  ,(9 ,'action9_2')  ,(9 ,'action9_3')  ,(10,'action9_4')  ,(23,'action9_5')  , (24,'action9_6') , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')        , (0, 'None')      , (0, 'None')      , (0, 'None')      ,(0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')       , (0, 'None')       , (0, 'None')          ],  #<---STATE9
               [( 10,'action10_0') ,(10,'action10_1') ,(10,'action10_2') ,(10,'action10_3') ,( 9,'action10_4') ,(11,'action10_5') , (23,'action10_6'), (24,'action10_7'), (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')        , (0, 'None')      , (0, 'None')      , (0, 'None')      ,(0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')       , (0, 'None')       , (0, 'None')          ],  #<---STATE10
               [( 11,'action11_0') ,(11,'action11_1') ,(8 ,'action11_2') ,(12,'action11_3') ,(23,'action11_4') ,(24,'action11_5') , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')        , (0, 'None')      , (0, 'None')      , (0, 'None')      ,(0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')       , (0, 'None')       , (0, 'None')          ],  #<---STATE11
               [( 12,'action12_0') ,(12,'action12_1') ,(13,'action12_2') ,(23,'action12_3') ,(24,'action12_4') ,(0, 'None')       , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')        , (0, 'None')      , (0, 'None')      , (0, 'None')      ,(0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')       , (0, 'None')       , (0, 'None')          ],  #<---STATE12
               [( 13,'action13_0') ,(13,'action13_1') ,(13,'action13_2') ,(13,'action13_3') ,(14,'action13_4') ,(23,'action13_5') , (24,'action13_6'), (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')        , (0, 'None')      , (0, 'None')      , (0, 'None')      ,(0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')       , (0, 'None')       , (0, 'None')          ],  #<---STATE13
               [( 14,'action14_0') ,(14,'action14_1') ,(4 ,'action14_2') ,(15,'action14_3') ,(23,'action14_4') ,(24,'action14_5') , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')        , (0, 'None')      , (0, 'None')      , (0, 'None')      ,(0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')       , (0, 'None')       , (0, 'None')          ],  #<---STATE14
               [( 15,'action15_0') ,(15,'action15_1') ,(16,'action15_2') ,(23,'action15_3') ,(24,'action15_4') ,(0 ,'None')       , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')        , (0, 'None')      , (0, 'None')      , (0, 'None')      ,(0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')       , (0, 'None')       , (0, 'None')          ],  #<---STATE15
               [( 16,'action16_0') ,(16,'action16_1') ,(17,'action16_2') ,(23,'action16_3') ,(24,'action16_4') ,(0 ,'None')       , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')        , (0, 'None')      , (0, 'None')      , (0, 'None')      ,(0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')       , (0, 'None')       , (0, 'None')          ],  #<---STATE16
               [( 17,'action17_0') ,(17,'action17_1') ,(18,'action17_2') ,(23,'action17_3') ,(24,'action17_4') ,(0 ,'None')       , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')        , (0, 'None')      , (0, 'None')      , (0, 'None')      ,(0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')       , (0, 'None')       , (0, 'None')          ],  #<---STATE17
               [( 18,'action18_0') ,(18,'action18_1') ,(19,'action18_2') ,(23,'action18_3') ,(24,'action18_4') ,(0 ,'None')       , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')        , (0, 'None')      , (0, 'None')      , (0, 'None')      ,(0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')       , (0, 'None')       , (0, 'None')          ],  #<---STATE18
               [( 19,'action19_0') ,(19,'action19_1') ,(20,'action19_2') ,(23,'action19_3') ,(24,'action19_4') ,(0 ,'None')       , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')        , (0, 'None')      , (0, 'None')      , (0, 'None')      ,(0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')       , (0, 'None')       , (0, 'None')          ],  #<---STATE19
               [( 20,'action20_0') ,(20,'action20_1') ,(18,'action20_2') ,(21,'action20_3') ,(23,'action20_4') ,(24,'action20_5') , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')        , (0, 'None')      , (0, 'None')      , (0, 'None')      ,(0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')       , (0, 'None')       , (0, 'None')          ],  #<---STATE20
               [( 21,'action21_0') ,(21,'action21_1') ,(22,'action21_2') ,(23,'action21_3') ,(24,'action21_4') ,(0 ,'None')       , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')        , (0, 'None')      , (0, 'None')      , (0, 'None')      ,(0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')       , (0, 'None')       , (0, 'None')          ],  #<---STATE21
               [( 22,'action22_0') ,(22,'action22_1') ,(23,'action22_2') ,(24,'action22_3') ,(0 ,'None')       ,(0 ,'None')       , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')        , (0, 'None')      , (0, 'None')      , (0, 'None')      ,(0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')       , (0, 'None')       , (0, 'None')          ],  #<---STATE22
               [( 23,'action23_0') ,(1 ,'action23_1') ,(2 ,'action23_2') ,(3 ,'action23_3') ,(4 ,'action23_4') ,(5 ,'action23_5') ,(6 ,'action23_6') , (7 ,'action23_7'), (8 ,'action23_8'), (9 ,'action23_9'), (10,'action23_10'), (11,'action23_11') , (12, 'action23_12'), (13, 'action23_13'),(14, 'action23_5'),(15,'action23_6') , (16,'action23_7'),(17,'action23_8'), (18,'action23_9'), (19,'action23_10'), (20,'action23_11'), (21,'action23_12'), (22,'action23_13')   ],  #<---STATE23
               [( 24,'action24_0') ,(0, 'None')       ,(0 , 'None')      ,(0 , 'None')      ,(0 , 'None')      ,(0 , 'None')      , (0 , 'None')     , (0 , 'None')     , (0, 'None')      , (0, 'None')      , (0, 'None')       , (0, 'None')        , (0, 'None')        , (0, 'None')        , (0, 'None')      , (0, 'None')      , (0, 'None')      , (0, 'None')     , (0, 'None')      , (0, 'None')       , (0, 'None')       , (0, 'None')       , (0, 'None')          ]   #<---STATE24
               ])  



def name():
    return "DegasClean"


state_name = {0:"S0: Initialization", 1:"S1: AdvancetoClean1", 2:"S2: AdvancetoClean2", 3:"S3: GetNewAirSlugs1",
              4:"S4: SwitchCleaningFluid", 5:"S5: LoadClean", 6:"S6: LoadAir1", 7:"S7: LoadAir2", 8:"S8: SwitchPort",
              9:"S9:  FillPort", 10:"S10:  EmptyPort", 11:"S11: GotoSwitchPort", 12:"S12: FluidtoWaste1", 13:"S13: FluidtoWaste2",
              14:"S14: GotoSwitchCleaningFluid", 15:"S15: PurgeAirSlugs", 16:"S16: GetNewAirSlugs2", 17:"S17: DegasDry1", 
              18:"S18: SwitchDryPort", 19:"S19: DegasDryWait", 20:"S20: GotoSwitchDryPort", 21:"S21: CloseGasLine", 
              22:"S22:  DegasCleanComplete", 23:"S23: Pause", 24:"S24: Error"}


    

#------ global variables used only in this statemachine
DegasCleanFluid = 0
DegasCleanPort = 0
DegasDryPort = 0





def air_or_liquid( voltage):
    if voltage > HW.BS_THRESHOLD:
        return 'liquid'
    else:
        return 'air'
  


def DiluteDetergent(pump_address, valve_address):
    if (pump_address == HW.TIRRANT_PUMP_ADDRESS):
        scale_factor = GV.PUMP_TITRANT_SCALING_FACTOR
        pump_speed = int(RECIPE["Func_DiluteDetergent"]["titrant_pump_speed"] * scale_factor)
    else:
        scale_factor = GV.PUMP_SAMPLE_SCALING_FACTOR
        pump_speed = int(RECIPE["Func_DiluteDetergent"]["sample_pump_speed"] * scale_factor)

    
    detergent_volume = RECIPE["Func_DiluteDetergent"]["detergent_volume"]
    water_volume = RECIPE["Func_DiluteDetergent"]["water_volume"]

    #Valve to detergent (3)
    GV.pump1.set_multiwayvalve(valve_address,3)         
    time.sleep(1)
    GV.pump1.set_speed(pump_address, pump_speed)
    time.sleep(1)   
    pump_pos = GV.pump1.get_plunger_position(pump_address)
    time.sleep(.5)
    next_pos = pump_pos + detergent_volume
    GV.pump1.set_pos_absolute(pump_address, next_pos)  #pump to position
    while( pump_pos != next_pos):
        time.sleep(.5)
        pump_pos = GV.pump1.get_plunger_position(pump_address)
        logger.info("pump pos: {}  target: {}".format(pump_pos, next_pos))
      
    #Valve to water 5
    GV.pump1.set_multiwayvalve(valve_address,5)         
    time.sleep(1)
    pump_pos = GV.pump1.get_plunger_position(pump_address)
    time.sleep(.5)
    next_pos = pump_pos + water_volume
    GV.pump1.set_pos_absolute(pump_address, next_pos)  #pump to position
    while( pump_pos != next_pos):
        time.sleep(.5)
        pump_pos = GV.pump1.get_plunger_position(pump_address)
        logger.info("pump pos: {}  ,  target: {}".format(pump_pos, next_pos))

    # time.sleep(.5)
    # GV.pump1.set_multiwayvalve(valve_address, 1) #valve  to air (1)



def NewAirSlugs(pump_address, valve_address):
    if (pump_address == HW.TIRRANT_PUMP_ADDRESS):
        scale_factor = GV.PUMP_TITRANT_SCALING_FACTOR
        pump_speed = int(RECIPE["Func_NewAirSlugs"]["titrant_pump_speed"] * scale_factor)
    else:
        scale_factor = GV.PUMP_SAMPLE_SCALING_FACTOR
        pump_speed = int(RECIPE["Func_NewAirSlugs"]["sample_pump_speed"] * scale_factor)
    
    air_slug_total_count = RECIPE["Func_NewAirSlugs"]["AirSlug_Total_count"]
    air_slug_volume = RECIPE["Func_NewAirSlugs"]["AirSlug_Volume"]
    LastAirSlug_Volume = RECIPE["Func_NewAirSlugs"]["LastAirSlug_Volume"]
    # SC2_Volume = RECIPE["Func_NewAirSlugs"]["SC2_Volume"]
    # WaterSlug_Volume = RECIPE["Func_NewAirSlugs"]["WaterSlug_Volume"]   
    
    tot =0
    starting_pos = GV.pump1.get_plunger_position(pump_address)
    time.sleep(.5)    
    GV.pump1.set_speed(pump_address, pump_speed)
    time.sleep(.5)
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
        GV.SM_TEXT_TO_DIAPLAY =  "Prepare to go to Pause State"
        return 
    if (GV.ERROR == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY =  "Prepare to go to error State"
        return     
    #seting the scale factor for converting volume to pump position units
    sample_pump_step = RECIPE["DegasClean"]["sample_pump_step"]
    titrant_pump_step = RECIPE["DegasClean"]["titrant_pump_step"]
    if sample_pump_step == "full step":
        str0 = 'pump 2: full step\n'
        GV.PUMP_SAMPLE_SCALING_FACTOR = HW.SAMPLE_PUMP_VOLUM_2_STEP
        GV.pump1.set_microstep_position(HW.SAMPLE_PUMP_ADDRESS,0)
    else:
        str0 = 'pump 2: micro step\n'
        GV.PUMP_SAMPLE_SCALING_FACTOR = HW.SAMPLE_PUMP_VOLUM_2_MICROSTEP
        GV.pump1.set_microstep_position(HW.SAMPLE_PUMP_ADDRESS,2)
    time.sleep(0.5)
    if titrant_pump_step == "full step":
        str1 = 'pump 2: full step\n'
        GV.PUMP_TITRANT_SCALING_FACTOR = HW.TITRANT_PUMP_VOLUM_2_STEP
        GV.pump1.set_microstep_position(HW.TIRRANT_PUMP_ADDRESS,0)
    else:
        str1 = 'pump 2: micro step\n'
        GV.PUMP_TITRANT_SCALING_FACTOR = HW.TITRANT_PUMP_VOLUM_2_MICROSTEP
        GV.pump1.set_microstep_position(HW.TIRRANT_PUMP_ADDRESS,2)


    logger.info("Sample pump scale facotr:{}".format(str0))
    logger.info("Titranst pump scale facotr:{}".format(str1))



    GV.VALVE_2 = "Line to Pump"
    GV.VALVE_4 = "Line to Pump"
    GV.VALVE_7 = "Reservoirs"
    GV.VALVE_8 = "Waste"
    GV.SM_TEXT_TO_DIAPLAY = "initialization\n" 
    GV.next_E = 0


#-------------------------------------------------------------------------------------------
def action1_0():
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "Prepare to go to Pause State"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "Prepare to go to error State"
        return   

    str1 =  "Waiting for valves to go to position\n" " -V2 to LinetoPump\n" 
    str1 = str1 + " - V4 to LinetoPump\n" " - V7 to Reservoirs\n" " - V8 to Waste\n"
    GV.SM_TEXT_TO_DIAPLAY = str1
    GV.next_E = 1


def action1_1():
    timeout = False
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to  pause state"
        return 
    if (GV.ERROR == True or timeout==True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY =  "going to error state"
        return 
    
    GV.pump1.set_valve(HW.SAMPLE_PUMP_ADDRESS, HW.VALVE2_P3)
    time.sleep(.5)
    GV.pump1.set_valve(HW.SAMPLE_LOOP_ADDRESS, HW.VALVE4_P2)
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.DEGASSER_ADDRESS,HW.VALVE7_P1)        
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.SAMPLE_CLEANING_ADDRESS,HW.VALVE8_P1)    
    time.sleep(.5)
        
    GV.SM_TEXT_TO_DIAPLAY = "Valves in position"
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
    
    GV.SM_TEXT_TO_DIAPLAY = "Going to State 2"
    GV.next_E = 0


def action1_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY =  "going to error state"
        return     
    GV.SM_TEXT_TO_DIAPLAY ="going to PAUSE state"
    GV.next_E = 0
    GV.prev_S = 1
    
    
def action1_4():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY = "going to ERROR state"


#----------------------------------------------------------------   
def action2_0():
    if (GV.PAUSE == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "going to pause state"
        return 
    if (GV.ERROR == True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY =  "going to error state"
        return 
    #turn off the pump active LED
    GV.pump2_sample_active_led     = True
    GV.SM_TEXT_TO_DIAPLAY ="pump 2 dispense \n waiting for transition in Bubble sensor 8"
    GV.next_E = 1


def action2_1():
    timeout_flag = False 
    if (GV.PAUSE == True):
        GV.next_E = 5           
        GV.SM_TEXT_TO_DIAPLAY = "going to pause state"
        return 
    if (GV.ERROR == True ):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = "going to error state"
        return 
    


    bubble_pickup_timeout = RECIPE["DegasClean"]["pump_move_timeout"]
    logger.info('Dispense until bubble')

    pump2_speed = int(HW.BUBBLE_DETECTION_PUMP_SPEED * GV.PUMP_SAMPLE_SCALING_FACTOR)
    print("===> pump 2 bubble sensor speed: ", pump2_speed)
    GV.pump1.set_speed(HW.SAMPLE_PUMP_ADDRESS, pump2_speed)
    time.sleep(1)        
    GV.pump1.set_pos_absolute(HW.SAMPLE_PUMP_ADDRESS, HW.DISPENSE_UNTIL_BUBBLE_TARGET)
    time.sleep(1)
    input2 = GV.labjack.getAIN(HW.BS8_IO_PORT)   #bubble sensor 2
    #check if the bubble semsor detect air or liquid
    cur_state_2 = air_or_liquid(input2)
    prev_state_2 = cur_state_2
    bubble_2_search = True    
    start_time = time.time()
    wait_time = 0
    while (bubble_2_search) :
        input2 = GV.labjack.getAIN(HW.BS8_IO_PORT)   #bubble sensor 2
        cur_state_2 = air_or_liquid(input2)
        pos2 =GV.pump1.get_plunger_position(HW.SAMPLE_PUMP_ADDRESS)
        if (cur_state_2 != prev_state_2):
            bubble_2_search = False
            GV.pump1.stop(HW.SAMPLE_PUMP_ADDRESS)
            time.sleep(0.5)
        time.sleep(.025)
        wait_time = time.time() - start_time
        logger.info('\t\tBS: {:.2f} position: {}'.format(input2, pos2))
        if (wait_time >  bubble_pickup_timeout):
            logger.error("\t\tpickup timeout. going to Pause state")
            timeout_flag = True
            break

    logger.info('\t\tBubble detection terminated')
    pump1_speed = int(RECIPE["DegasClean"]["titrant_pump_speed"] * GV.PUMP_TITRANT_SCALING_FACTOR)
    pump2_speed = int(RECIPE["DegasClean"]["sample_pump_speed"] * GV.PUMP_SAMPLE_SCALING_FACTOR)
    GV.pump1.set_speed(HW.TIRRANT_PUMP_ADDRESS,pump1_speed)
    time.sleep(1)
    GV.pump1.set_speed(HW.SAMPLE_PUMP_ADDRESS,pump2_speed)
    time.sleep(1)  

    if (timeout_flag == True):
        GV.SM_TEXT_TO_DIAPLAY ="Pickup timeout.\n going to Pause state"
        GV.PAUSE = True
        GV.next_E = 5
    else:
        GV.SM_TEXT_TO_DIAPLAY = "Transition in BS8 detected\n" 
        GV.next_E = 2
    
    
def action2_2():
    if (GV.PAUSE == True):
        GV.next_E = 5          
        GV.SM_TEXT_TO_DIAPLAY = "  goint to pause"
        return 
    if (GV.ERROR == True ):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY =  "  goint to error"
        return 

    S4 = RECIPE["DegasClean"]["s4_volume"]
    pump_address2 = HW.SAMPLE_PUMP_ADDRESS
    starting_pos2 = GV.pump1.get_plunger_position(pump_address2)
    time.sleep(.5)
    next_pos2 =  starting_pos2 - S4
    GV.pump1.set_pos_absolute(pump_address2, next_pos2)
    pump_pos2 = starting_pos2
    logger.info("\tPump 2 Dispense")
    while (pump_pos2 != next_pos2):
        time.sleep(0.5)
        pump_pos2 = GV.pump1.get_plunger_position(pump_address2)
        logger.info("\t\tpump2 pos: {}/{}".format(pump_pos2, next_pos2))

    time.sleep(5)
    #turn off the pump active LED
    GV.pump2_sample_active_led  = False
    GV.SM_TEXT_TO_DIAPLAY ="pump 2 to position variabl S4"    
    GV.next_E = 3

   
def action2_3():
    if (GV.PAUSE == True):
        GV.next_E = 5          
        GV.SM_TEXT_TO_DIAPLAY = "  goint to pause"
        return 
    if (GV.ERROR == True ):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY =  "  goint to error"
        return 

    GV.SM_TEXT_TO_DIAPLAY ="pump2 in position S4"    
    GV.next_E = 4


def action2_4():
    if (GV.PAUSE == True):
        GV.next_E = 5          
        GV.SM_TEXT_TO_DIAPLAY = "  goint to pause"
        return 
    if (GV.ERROR == True ):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY =  "  goint to error"
        return 
    
    GV.SM_TEXT_TO_DIAPLAY ="Get New Air Slugs1"    
    GV.next_E = 0


def action2_5():
    if (GV.ERROR == True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = "Prepare to go to error State"
        return         

    GV.next_E = 0
    GV.prev_S = 2
    GV.SM_TEXT_TO_DIAPLAY = "going to PAUSE state "

def action2_6():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="  goint to ERROR state"


#----------------------------------------------------------------
def action3_0():
    if (GV.PAUSE == True):
        GV.next_E = 3          
        GV.SM_TEXT_TO_DIAPLAY = "ging to pause state"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "going to error state"
        return 

    GV.SM_TEXT_TO_DIAPLAY ="Get New Air Slugs1" 
    GV.next_E = 1


def action3_1():
    if (GV.PAUSE == True):
        GV.next_E = 3        
        GV.SM_TEXT_TO_DIAPLAY = "S3,E1 -> action3_1\n" "  goint to S2/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S3,E1 -> action3_1\n" "  goint to S2/E4"
        return         
    
    pump_address = HW.SAMPLE_PUMP_ADDRESS
    valve_address = HW.DEGASSER_ADDRESS
    NewAirSlugs(pump_address, valve_address)
    
    GV.SM_TEXT_TO_DIAPLAY ="Get New Air Slug is done"
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
        
    GV.SM_TEXT_TO_DIAPLAY = "-V4 to PumptoLine\n" "-V7 to Reservoirs\n"  
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
    global DegasCleanFluid
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to pause state"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "going to error state"
        return 

    GV.VALVE_4 = "Pump to Line"
    GV.VALVE_7 = "Reservoirs"

    GV.pump1.set_multiwayvalve(HW.DEGASSER_ADDRESS, HW.VALVE7_P1)        
    time.sleep(.5)
    GV.pump1.set_valve(HW.SAMPLE_LOOP_ADDRESS, HW.VALVE4_P2)
    time.sleep(.5)

    if (DegasCleanFluid == 0):
        GV.pump1.set_multiwayvalve(HW.SAMPLE_CLEANING_ADDRESS, HW.VALVE8_P3)    
        GV.VALVE_8 = "Detergent"
    elif (DegasCleanFluid == 1):
        GV.pump1.set_multiwayvalve(HW.SAMPLE_CLEANING_ADDRESS, HW.VALVE8_P4)    
        GV.VALVE_8 = "DI Water"
    elif (DegasCleanFluid == 2):
        GV.pump1.set_multiwayvalve(HW.SAMPLE_CLEANING_ADDRESS, HW.VALVE8_P2)    
        GV.VALVE_8 = "MeOH"
    else:
        logger.error("Invalid DegasCleanFluid value")
    
    time.sleep(.5)
    GV.next_E = 1
    GV.SM_TEXT_TO_DIAPLAY ="Valves reached positions"  


def action4_1():
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to pause state"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "going to error state"
        return 

    GV.SM_TEXT_TO_DIAPLAY ="  Valves reached position\n"
    GV.next_E = 2


def action4_2():      
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to pause state"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "going to error state"
        return          
  
    GV.SM_TEXT_TO_DIAPLAY ="V8 to Air"
    GV.next_E = 0


def action4_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "going to error state"
        return         
    # print("S4,E3 -> action4_3")    
    GV.SM_TEXT_TO_DIAPLAY =   "  going to PAUSE"
    GV.next_E = 0
    GV.prev_S = 4


def action4_4():    
    GV.SM_TEXT_TO_DIAPLAY = " going to ERROR state"
    GV.next_E = 0
    GV.prev_S = 4


#------------------------------------------------------------------------------------ 
def action5_0():
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to pasue satte"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "going to Error state"
        return    
    
    pump_address = HW.SAMPLE_PUMP_ADDRESS
    if (DegasCleanFluid == 0):
        valve_address = HW.DEGASSER_ADDRESS    
        logger.info("\trunning DiluteDetergent")
        DiluteDetergent(pump_address, valve_address)
        GV.next_E = 2
    else:
        GV.next_E = 1
        logger.info("\tsending pump to position")
        degas_clean_volume = RECIPE["DegasClean"]["degascleanfluid_volume"]
        pump_pos = GV.pump1.get_plunger_position(pump_address)
        next_pos = pump_pos + degas_clean_volume
        time.sleep(.5)
        GV.pump1.set_pos_absolute(pump_address, next_pos)  #pump to position
        while(pump_pos != next_pos):
            time.sleep(1) 
            pump_pos = GV.pump1.get_plunger_position(pump_address)
            logger.info("pump pos: {},   target: {}".format( pump_pos, next_pos))
              
    GV.SM_TEXT_TO_DIAPLAY ="going to S5/E1"
    

def action5_1():
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "going to pasue satte"
        return 
    if (GV.ERROR == True ):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "going to Error state"
        return    
    
    GV.SM_TEXT_TO_DIAPLAY ="goint to S5/E0"
    GV.next_E = 2
    

def action5_2():
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY ="going to pasue satte"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "going to Error state"
        return    


    # GV.terminate_SM = True
    GV.SM_TEXT_TO_DIAPLAY ="going to S6/E0"
    GV.next_E = 0


def action5_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "   goint to S5/E4"
        return 
    
    GV.SM_TEXT_TO_DIAPLAY ="action5_3 \n----> going to PAUSE state"
    GV.next_E = 0
    GV.prev_S = 5
    

def action5_4():
    GV.SM_TEXT_TO_DIAPLAY ="action5_4\n"
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


    GV.VALVE_1 = "Pump to Air"
    GV.VALVE_2 = "Pump to Air"

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
    
    GV.pump1.set_multiwayvalve(HW.SAMPLE_CLEANING_ADDRESS, HW.VALVE8_P6)    
    time.sleep(.5)
    GV.VALVE_8 = "Air"
    GV.SM_TEXT_TO_DIAPLAY ="  Valves reached position\n"  
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

    GV.SM_TEXT_TO_DIAPLAY ="going to S7/E0" 
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

    GV.SM_TEXT_TO_DIAPLAY ="Pick up until bubble (BS4)"
    GV.next_E = 1


def action7_1():
    timeout_flag = False
    if (GV.PAUSE == True ):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S7,E1 -> action7_1\n" "Pgoint to S7/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S7,E1 -> action7_1\n" "goint to S7/E4"
        return 

    bubble_pickup_timeout = RECIPE["DegasClean"]["pump_move_timeout"]
    logger.info('Dispense until bubble (BS4)')
    pump2_speed = int(HW.BUBBLE_DETECTION_PUMP_SPEED * GV.PUMP_SAMPLE_SCALING_FACTOR)
    GV.pump1.set_speed(HW.SAMPLE_PUMP_ADDRESS, pump2_speed)
    time.sleep(1)        
    GV.pump1.set_pos_absolute(HW.SAMPLE_PUMP_ADDRESS, HW.DISPENSE_UNTIL_BUBBLE_TARGET)
    time.sleep(1)
    input2 = GV.labjack.getAIN(HW.BS4_IO_PORT)   #bubble sensor 2
    #check if the bubble semsor detect air or liquid
    cur_state_2 = air_or_liquid(input2)
    prev_state_2 = cur_state_2
    bubble_2_search = True    
    start_time = time.time()
    wait_time = 0
    while (bubble_2_search) :
        input2 = GV.labjack.getAIN(HW.BS4_IO_PORT)   #bubble sensor 2
        cur_state_2 = air_or_liquid(input2)
        pos2 =GV.pump1.get_plunger_position(HW.SAMPLE_PUMP_ADDRESS)
        if (cur_state_2 != prev_state_2):
            bubble_2_search = False
            GV.pump1.stop(HW.SAMPLE_PUMP_ADDRESS)
            time.sleep(0.5)
        time.sleep(.025)
        wait_time = time.time() - start_time
        logger.info('\t\tBS: {:.2f} position: {}'.format(input2, pos2))
        if (wait_time >  bubble_pickup_timeout):
            logger.error("\t\tpickup timeout. going to Pause state")
            timeout_flag = True
            break

    logger.info('\t\tBubble detection terminated')
    pump1_speed = int(RECIPE["DegasClean"]["titrant_pump_speed"] * GV.PUMP_TITRANT_SCALING_FACTOR)
    pump2_speed = int(RECIPE["DegasClean"]["sample_pump_speed"] * GV.PUMP_SAMPLE_SCALING_FACTOR)
    GV.pump1.set_speed(HW.TIRRANT_PUMP_ADDRESS,pump1_speed)
    time.sleep(1)
    GV.pump1.set_speed(HW.SAMPLE_PUMP_ADDRESS,pump2_speed)
    time.sleep(1)  

    if (timeout_flag == True):
        GV.SM_TEXT_TO_DIAPLAY ="Pickup timeout.\n going to Pause state"
        GV.PAUSE = True
        GV.next_E = 3
    else:
        GV.SM_TEXT_TO_DIAPLAY = "Transition in BS8 detected\n" 
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
  
    GV.pump1_titrant_active_led    = True
    GV.pump2_sample_active_led     = False
    GV.SM_TEXT_TO_DIAPLAY = "going to S8/E0"
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

    GV.pump1_titrant_active_led    = False
    GV.pump2_sample_active_led     = True
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


    GV.VALVE_8 = "Air"
    GV.VALVE_9 = "Air"


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

    GV.pump1_titrant_active_led    = True
    GV.pump2_sample_active_led     = True
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
    pump1_speed = int(HW.BUBBLE_DETECTION_PUMP_SPEED * GV.PUMP_TITRANT_SCALING_FACTOR)
    pump2_speed = int(HW.BUBBLE_DETECTION_PUMP_SPEED * GV.PUMP_SAMPLE_SCALING_FACTOR)
    GV.pump1.set_speed(HW.TIRRANT_PUMP_ADDRESS, pump1_speed)
    time.sleep(1)        
    GV.pump1.set_speed(HW.SAMPLE_PUMP_ADDRESS, pump2_speed)
    time.sleep(1)        
    GV.pump1.set_pos_absolute(HW.TIRRANT_PUMP_ADDRESS, HW.PICKUP_UNTIL_BUBBLE_TARGET)
    time.sleep(1)
    GV.pump1.set_pos_absolute(HW.SAMPLE_PUMP_ADDRESS, HW.PICKUP_UNTIL_BUBBLE_TARGET)
    time.sleep(1)
    input1 = GV.labjack.getAIN(0)
    input2 = GV.labjack.getAIN(1)
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
    pump1_speed = int(RECIPE["DegasClean"]["titrant_pump_speed"] * GV.PUMP_TITRANT_SCALING_FACTOR)
    pump2_speed = int(RECIPE["DegasClean"]["sample_pump_speed"] * GV.PUMP_SAMPLE_SCALING_FACTOR)
    GV.pump1.set_speed(HW.TIRRANT_PUMP_ADDRESS,pump1_speed)
    time.sleep(1)
    GV.pump1.set_speed(HW.SAMPLE_PUMP_ADDRESS,pump2_speed)
    time.sleep(1)  

    GV.pump1_titrant_active_led    = False
    GV.pump2_sample_active_led     = False

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


