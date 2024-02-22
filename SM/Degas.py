import  numpy as npfile_handler
import  general.global_vars as GV
import  hardware.config as HW
import  time
from    general.recipe import RECIPE
import  logging
import  numpy as np

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(levelname)s:%(message)s')
file_handler = logging.FileHandler('./logs/error.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
# logger.addHandler(file_handler)
# logger.addHandler(stream_handler)


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


state_name = {0:"S0: Initialization", 1:"S1: DegasValvePos", 2:"S2: StartTEC", 3:"S3: AspirateIN",
              4:"S4: DispenseOUT", 5:"S5: DegasComplete", 6:"Pause", 7:"Error"}

heating_wait_time = 0 #to hold how much time is passed since the TEC controller is turned on until now
settle_wait_start_time  = 0     # keeps track of temperature the settle time
current_Aspiration_count = 0    #keeps track of aspiratin number 

#---------------  ACTIONS  --------------
def action0_0():
    global current_Aspiration_count
    #seting the scale factor for converting volume to pump position units
    sample_pump_step = RECIPE["Degas"]["sample_pump_step"]
    titrant_pump_step = RECIPE["Degas"]["titrant_pump_step"]
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

    str2 = "-V1 to LinetoPump\n" "-V3 to TitrantLine\n" "-V5 to TitrantPort\n" "-V2 to LinetoGas\n"
    str2 = str1 + "-V4 to SampleLine\n"  "-V7 to SamplePort"
    GV.SM_TEXT_TO_DIAPLAY = str2 + str1 + str0
    current_Aspiration_count = 0
    # GV.current_Aspiration_count = 0
    GV.next_E = 0    


#--------------
def action1_0():
    if (GV.PAUSE == True):
        GV.next_E = 3          
        GV.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0\n" "Prepare to go to Pause State"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0\n" "Prepare to go to error State"
        return 
    # move the valves to positions
    GV.pump1.set_valve(HW.TIRRANT_PUMP_ADDRESS, HW.VALVE1_P2)
    time.sleep(.5)
    GV.pump1.set_valve(HW.TITRANT_LOOP_ADDRESS, HW.VALVE3_P3)
    time.sleep(.5)
    # GV.pump1.set_multiwayvalve(HW.TITRANT_PIPETTE_ADDRESS,HW.VALVE5_P2)
    GV.pump1.set_valve(HW.TITRANT_PIPETTE_ADDRESS,HW.VALVE5_P2)
    time.sleep(.5)
    # GV.pump1.set_multiwayvalve(HW.TITRANT_PORT_ADDRESS,2)
    GV.pump1.set_valve(HW.TITRANT_PORT_ADDRESS, HW.VALVE6_P2)
    time.sleep(.5)
    GV.pump1.set_valve(HW.SAMPLE_PUMP_ADDRESS,  HW.VALVE2_P3)
    time.sleep(.5)
    GV.pump1.set_valve(HW.SAMPLE_LOOP_ADDRESS, HW.VALVE4_P2)
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.DEGASSER_ADDRESS, HW.VALVE7_P3)
    time.sleep(.5)
    # GV.pump1.set_speed(HW.TIRRANT_PUMP_ADDRESS,RECIPE["Degas"]["titrant_pump_speed"])
    # time.sleep(1)
    # GV.pump1.set_speed(HW.SAMPLE_PUMP_ADDRESS,RECIPE["Degas"]["sample_pump_speed"])
    # time.sleep(1)
    pump1_speed = int(RECIPE["Degas"]["titrant_pump_speed"] * GV.PUMP_TITRANT_SCALING_FACTOR)
    pump2_speed = int(RECIPE["Degas"]["sample_pump_speed"] * GV.PUMP_SAMPLE_SCALING_FACTOR)
    GV.pump1.set_speed(HW.TIRRANT_PUMP_ADDRESS, pump1_speed)
    time.sleep(1)
    GV.pump1.set_speed(HW.SAMPLE_PUMP_ADDRESS, pump2_speed)
    time.sleep(1) 

    GV.VALVE_1 = "Line to Pump"    
    GV.VALVE_3 = "Titrant Line"    
    GV.VALVE_5 = "Titrant Port"
    GV.VALVE_2 = "Line to Gas"
    GV.VALVE_4 = "Sample Line"
    GV.VALVE_7 = "Sample Port"
    str1 =  "-V1 to LinetoPump\n" "-V3 to TitrantLine\n" "-V5 to TitrantPort\n" 
    str1 = str1 + "-V2 to LinetoGas\n" "-V4 to SampleLine\n"  "-V7 to SamplePort"
    GV.SM_TEXT_TO_DIAPLAY = str1
    GV.next_E = 1


def action1_1():
    timeout = False
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" "go to S1/E3"
        return 
    if (GV.ERROR == True or timeout==True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" "go to S1/E4"
        return     
    str1 = "  Valves in position\n"  "  go to S1/E2"
    GV.SM_TEXT_TO_DIAPLAY = str1
    GV.next_E = 2


def action1_2():
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S1,E2 -> action1_2\n" "go to S1/E3"
        return     
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S1,E2 -> action1_2\n" "go to S1/E4"
        return     
    GV.SM_TEXT_TO_DIAPLAY = "  go to S2/E0 state"
    GV.next_E = 0


def action1_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S1,E3 -> action1_3\n" "  go to S1/E4"
        return     
    GV.SM_TEXT_TO_DIAPLAY ="S1,E2 -> action1_2\n"  "  go to PAUSE state"
    GV.next_E = 0
    GV. prev_S = 1
    
    
def action1_4():
    GV.SM_TEXT_TO_DIAPLAY = "S1,E4 -> action1_4\n" "  go to ERROR state"
    GV.next_E = 0


#------------------------------------------------------------------------------------------------
def action2_0():
    global current_Aspiration_count
    if (GV.PAUSE == True):
        GV.next_E = 4        
        GV.SM_TEXT_TO_DIAPLAY = "S2,E0 -> action2_1\n" "  going to S2/E4"
        return 
    if (GV.ERROR == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S2,E0 -> action2_1\n" "  going to S2/E5"
        return 
    
    temp = RECIPE['Degas']['degas_temp']
    logger.info("\t\t set temperature: {}".format(temp))
    GV.tec.set_temp(float(temp))
    time.sleep(1)
    # turn on the TEC controller
    GV.tec.enable()
    time.sleep(1)
    tec_dic =  GV.tec.get_data()
    obj_temp = round(tec_dic['object temperature'][0], 1)
    target_temp = round(tec_dic['target object temperature'][0], 1)
    TEC_cur_status = tec_dic['loop status'][0]        
    logger.info('\t\tobj temp:{} , target temp:{}    status:{}'.format(obj_temp,  target_temp,TEC_cur_status))  
    GV.TEC_IS_ON = True
    GV.TEC_TARGET = target_temp
    GV.TEC_ACTUAL = obj_temp
    total_asipiration_number = RECIPE["Degas"]["total_asipiration_number"]    
    str0 = "\nCurrent Aspiration: {}\nTotal Aspirations: {}".format(current_Aspiration_count+1,
                                                                    total_asipiration_number)
    str1 = "  set TEC to temp\n" "  going to S2/E1"
    GV.SM_TEXT_TO_DIAPLAY =str1 + str0
    GV.next_E = 1


def action2_1():
    global heating_wait_time
    global settle_wait_start_time    
    if (GV.PAUSE == True):
        GV.next_E = 4        
        GV.SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1\n" "  going to S2/E4"
        return 
    if (GV.ERROR == True):
        GV.next_E = 5
        # GV.SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1\n" "  going to S2/E5"
        return     
    heating_timeout = RECIPE["Degas"]["temperature_settledown_timeout"]
    if (heating_wait_time > heating_timeout):
        GV.ERROR = True
        GV.SM_TEXT_TO_DIAPLAY = "ERROR: heating timout error\n Going to error state"

    heating_wait_time += 1
    tec_dic =  GV.tec.get_data()    
    time.sleep(1)
    obj_temp = round(tec_dic['object temperature'][0], 1)
    target_temp = round(tec_dic['target object temperature'][0], 1)
    # TEC_cur_status = tec_dic['loop status'][0]    
    GV.TEC_ACTUAL = obj_temp
    if (heating_wait_time % 10 == 0):
        logger.info('\t\telapsed time: {} sec. ,   obj temp:{} '.format(heating_wait_time,obj_temp))
    if ( abs (obj_temp - target_temp) > HW.TEC_ACCEPTABLE_TEMP_DIFF):
        GV.next_E = 1
        str1= f"elapsed time: {heating_wait_time}"
        GV.SM_TEXT_TO_DIAPLAY="Waiting to reach target temperature\n" + str1
    else:
        settle_wait_start_time = time.time()  #start the settle time timer
        GV.next_E = 2
        heating_wait_time = 0 #set the waiting time to zero for next repeatition
    

def action2_2():
    global settle_wait_start_time
    global current_Aspiration_count
    timeout = False
    # passed_time = 10 # measure the  heating time
    if (GV.PAUSE == True):
        GV.next_E = 4        
        # GV.SM_TEXT_TO_DIAPLAY = "S2,E2 -> action2_2\n" "  going to S2/E4"
        return 
    if (GV.ERROR == True  or  timeout==True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S2,E2 -> action2_2\n" "  going to S2/E5"
        return
    
    # update the current temperature on GUI 
    tec_dic =  GV.tec.get_data()
    obj_temp = round(tec_dic['object temperature'][0], 1)
    GV.TEC_ACTUAL = obj_temp
    #check if obj temp is less than 1 degree below/above target
    target_temp = RECIPE['Degas']['degas_temp']
    if ( abs ( target_temp - obj_temp) > 1):
        GV.PAUSE = True
        GV.SM_TEXT_TO_DIAPLAY = "ATTENTION: The temperature difference is above threshold\n""going to PAUSE state"
        logger.error(GV.SM_TEXT_TO_DIAPLAY)

    # check for the elapsed time
    heat_time = RECIPE["Degas"]["heat_time"]
    time_passed = time.time() - settle_wait_start_time
    time.sleep(1)
    if (time_passed % 10 == 0):
        logger.info('\t\telapsed time: {}/ ,  settle time:{} '.format(heating_wait_time, heat_time))        
    #decide to reapted or go to next event
    if (time_passed < heat_time):
        GV.next_E = 2
        total_asipiration_number = RECIPE["Degas"]["total_asipiration_number"]    
        str0 = "\nCurrent Aspiration:{}\nTotal Aspirations:{}".format(current_Aspiration_count+1, 
                                                                      total_asipiration_number)    
        str1= f"elapsed time: {int(time_passed)}\n" + str0
        GV.SM_TEXT_TO_DIAPLAY="Settle time in progress\n" + str1
    else:
        GV.SM_TEXT_TO_DIAPLAY ="going to S3/E0"
        GV.next_E = 3


def action2_3():
    global current_Aspiration_count
    if (GV.PAUSE == True):
        GV.next_E = 4        
        GV.SM_TEXT_TO_DIAPLAY = "S2,E3 -> action2_3\n" "  going to S2/E4"
        return 
    if (GV.ERROR == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S2,E3 -> action2_3\n" "  going to S2/E5"
        return
    GV.pump1_titrant_active_led     = True   
    GV.pump2_sample_active_led      = True
    total_asipiration_number = RECIPE["Degas"]["total_asipiration_number"]    
    str0 = "\nCurrent Aspiration:{}\nTotal Aspirations:{}".format(current_Aspiration_count+1, 
                                                                  total_asipiration_number)    
    str1 ="pump 1 pickup Var.: Tit. Vol. +Asp. Overshoot\n""pump 2 pickup Var.: Sample Vol. +Asp. Overshoot"
    GV.SM_TEXT_TO_DIAPLAY = str1 + str0
    GV.next_E = 0


def action2_4():
    if (GV.ERROR == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S2,E4 -> action2_4\n" "  going to S2/E5"
        return         
    
    # GV.SM_TEXT_TO_DIAPLAY ="S2,E4 -> action2_4"
    GV.next_E = 0
    GV. prev_S = 2


def action2_5():
    GV.SM_TEXT_TO_DIAPLAY ="S2,E5 -> action2_5"
    GV.next_E = 0

#--------------------------------------------------------------------------------------------
def action3_0():
    if (GV.PAUSE == True):
        GV.next_E = 3          
        GV.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0\n" "  going to S3/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0\n" "  going to S3/E4"
        return 
    # experiment_temp = RECIPE["Degas"]["experiment_temp"]
    # total_asipiration_number = RECIPE["Degas"]["total_asipiration_number"]
    # pump_address = HW.SAMPLE_PUMP_ADDRESS
    # valve_address = HW.DEGASSER_ADDRESS
    # pump_speed = RECIPE["Degas"]["pump_speed"] 

    # GV.pump1.set_speed(HW.TIRRANT_PUMP_ADDRESS,RECIPE["Degas"]["titrant_pump_speed"])
    # time.sleep(1)
    # GV.pump1.set_speed(HW.SAMPLE_PUMP_ADDRESS,RECIPE["Degas"]["sample_pump_speed"])
    # time.sleep(1)          
    pump1_speed = int(RECIPE["Degas"]["titrant_pump_speed"] * GV.PUMP_TITRANT_SCALING_FACTOR)
    pump2_speed = int(RECIPE["Degas"]["sample_pump_speed"] * GV.PUMP_SAMPLE_SCALING_FACTOR)
    GV.pump1.set_speed(HW.TIRRANT_PUMP_ADDRESS, pump1_speed)
    time.sleep(1)
    GV.pump1.set_speed(HW.SAMPLE_PUMP_ADDRESS, pump2_speed)
    time.sleep(1) 


    # AspirationVolume_Overshoot = RECIPE["Degas"]["AspirationVolume_Overshoot"]
    # AspirationVolume_Overshoot = int(RECIPE["Degas"]["AspirationVolume_Overshoot"]* GV.PUMP_TITRANT_SCALING_FACTOR )

    AspVol_Overshoot_titrant = int(RECIPE["Degas"]["AspirationVolume_Overshoot"]* GV.PUMP_TITRANT_SCALING_FACTOR )
    AspVol_Overshoot_sample = int(RECIPE["Degas"]["AspirationVolume_Overshoot"]* GV.PUMP_SAMPLE_SCALING_FACTOR )

    pump_address1 = HW.TIRRANT_PUMP_ADDRESS
    pump_address2 = HW.SAMPLE_PUMP_ADDRESS
    starting_pos1 = GV.pump1.get_plunger_position(pump_address1)
    time.sleep(1)
    # GV.pump1.set_speed(pump_address1, pump_speed)
    # time.sleep(.5)
    next_pos1 =  starting_pos1 + AspVol_Overshoot_titrant
    GV.pump1.set_pos_absolute(pump_address1, next_pos1)
    time.sleep(1)
    starting_pos2 = GV.pump1.get_plunger_position(pump_address2)
    time.sleep(1)
    # GV.pump1.set_speed(pump_address2, pump_speed)
    # time.sleep(1)
    next_pos2 =  starting_pos2 + AspVol_Overshoot_sample
    GV.pump1.set_pos_absolute(pump_address2, next_pos2)
    # wait untl pumps reach positions
    pump_pos1 = starting_pos1
    pump_pos2 = starting_pos2
    logger.info("\tAspiration IN")
    logger.info("\t\tpump1 pos: {}, Asp. vol 1: {},  pump2 pos: {}, Asp. vol 2: {}".format(pump_pos1,
                                                                                           AspVol_Overshoot_titrant,
                                                                                           pump_pos2,
                                                                                           AspVol_Overshoot_sample))
        
    while (pump_pos1 != next_pos1  or   pump_pos2 != next_pos2):    
        pump_pos1 = GV.pump1.get_plunger_position(pump_address1)        
        time.sleep(0.5)
        pump_pos2 = GV.pump1.get_plunger_position(pump_address2)
        logger.info("\t\tpump1 pos:{} /{}\tpump2 pos:{}/{}".format(pump_pos1, next_pos1, pump_pos2, next_pos2))
        time.sleep(0.5)
    time.sleep(5)

    GV.pump1_titrant_active_led     = False   
    GV.pump2_sample_active_led      = False
    #check if dose signal is receved 
    GV.next_E = 1
    str1 = "pump 1 pickup Var.:Tit. Vol. +Asp. Overshoot\n""pump 2 pickup Var.: Sample Vol. +Asp. Overshoot"
    GV.SM_TEXT_TO_DIAPLAY = str1


def action3_1():
    timeout = False
    if (GV.PAUSE == True):
        GV.next_E = 3        
        GV.SM_TEXT_TO_DIAPLAY = "S3,E1 -> action3_1\n" "  going to S3/E3"
        return 
    if (GV.ERROR == True or timeout==True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S3,E1 -> action3_1\n" "  going to S3/E4"
        return    
         
    GV.pump1_titrant_homed_led     = False
    GV.pump2_sample_homed_led      = False
    GV.next_E = 2
    GV.SM_TEXT_TO_DIAPLAY ="  go to S3/E2"


def action3_2():
    global current_Aspiration_count
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0" "  going to S3/E4"
        return 
    GV.pump1_titrant_active_led     = True   
    GV.pump2_sample_active_led      = True
    total_asipiration_number = RECIPE["Degas"]["total_asipiration_number"]    
    str0 = "\nCurrent Aspiration:{}\nTotal Aspirations:{}".format(current_Aspiration_count+1,
                                                                  total_asipiration_number)    
    str1 =  "pump 1 dispense Var.: Tit. Vol. +Asp. Overshoot\n""pump 2 dispense Var.: Sample Vol. +Asp. Overshoot"
    GV.SM_TEXT_TO_DIAPLAY =str1 + str0
    GV.next_E = 0

def action3_3():
    if (GV.ERROR == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0" "  going to S3/E3"
        return 
    
    GV.SM_TEXT_TO_DIAPLAY ="S3,E2 -> action3_2" "  go to PAUSE state"
    GV. prev_S = 3
    GV.next_E = 0

def action3_4():
    # logger.info("S3,E3 -> action3_3")
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S3,E3 -> action3_3" " go to ERROR state"

#----------------------------------------------------------------------------------------------
def action4_0():
    if (GV.PAUSE == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S4,E0 -> action4_0" "  going to S4/E5"
        return 
    if (GV.ERROR == True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = "S4,E0 -> action4_0" " going to S4/E6"
        return 
    # # pump_speed = RECIPE["Degas"]["pump_speed"]    
    # GV.pump1.set_speed(HW.TIRRANT_PUMP_ADDRESS,RECIPE["Degas"]["titrant_pump_speed"])
    # time.sleep(1)
    # GV.pump1.set_speed(HW.SAMPLE_PUMP_ADDRESS,RECIPE["Degas"]["sample_pump_speed"])
    # time.sleep(1)
    pump1_speed = int(RECIPE["Degas"]["titrant_pump_speed"] * GV.PUMP_TITRANT_SCALING_FACTOR)
    pump2_speed = int(RECIPE["Degas"]["sample_pump_speed"] * GV.PUMP_SAMPLE_SCALING_FACTOR)
    GV.pump1.set_speed(HW.TIRRANT_PUMP_ADDRESS, pump1_speed)
    time.sleep(1)
    GV.pump1.set_speed(HW.SAMPLE_PUMP_ADDRESS, pump2_speed)
    time.sleep(1) 


    # AspirationVolume_Overshoot = RECIPE["Degas"]["AspirationVolume_Overshoot"]
    AspVol_Overshoot_titrant = int(RECIPE["Degas"]["AspirationVolume_Overshoot"]* GV.PUMP_TITRANT_SCALING_FACTOR )
    AspVol_Overshoot_sample = int(RECIPE["Degas"]["AspirationVolume_Overshoot"]* GV.PUMP_SAMPLE_SCALING_FACTOR )
    pump_address1 = HW.TIRRANT_PUMP_ADDRESS
    pump_address2 = HW.SAMPLE_PUMP_ADDRESS
    starting_pos1 = GV.pump1.get_plunger_position(pump_address1)
    time.sleep(.5)
    next_pos1 =  starting_pos1 - AspVol_Overshoot_titrant
    GV.pump1.set_pos_absolute(pump_address1, next_pos1)
    time.sleep(1)
    starting_pos2 = GV.pump1.get_plunger_position(pump_address2)
    time.sleep(.5)
    next_pos2 =  starting_pos2 - AspVol_Overshoot_sample
    GV.pump1.set_pos_absolute(pump_address2, next_pos2)
    pump_pos1 = starting_pos1
    pump_pos2 = starting_pos2
    # print("Pump1 pos:", pump)
    # print('starting the despiration loop')
    logger.info("\tDispense OUT")
    logger.info("\t\tpump1 pos: {}, Asp. vol 1: {},  pump2 pos: {}, Asp. vol 2: {}".format(pump_pos1,
                                                                                           AspVol_Overshoot_titrant,
                                                                                           pump_pos2,
                                                                                           AspVol_Overshoot_sample))
    # while ( abs( pump_pos1 - next_pos1)> 5   or   abs( pump_pos2 - next_pos2)>5):
    while (pump_pos1 != next_pos1  or   pump_pos2 != next_pos2):
        pump_pos1 = GV.pump1.get_plunger_position(pump_address1)        
        time.sleep(0.5)
        pump_pos2 = GV.pump1.get_plunger_position(pump_address2)
        logger.info("\t\tpump1 pos:  {}/{}  \tpump2 pos: {}/{}".format(pump_pos1, next_pos1, pump_pos2, next_pos2))
        time.sleep(0.5)
    # print('ending the despiration loop')
    time.sleep(5)
    #turn off the pump active LED
    GV.pump1_titrant_active_led     = False   
    GV.pump2_sample_active_led      = False
    str1 =  "pump 1 dispense Var.: Tit. Vol. +Asp. Overshoot\n""pump 2 dispense Var.: Sample Vol. +Asp. Overshoot"
    GV.SM_TEXT_TO_DIAPLAY = str1
    GV.next_E = 1


def action4_1():
    timeout = False
    if (GV.PAUSE == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1\n" " going to S4/E5"
        return 
    if (GV.ERROR == True or timeout==True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1\n" " going to S4/E6"
        return 
    
    GV.SM_TEXT_TO_DIAPLAY = "  pumps in  position...\n" 
    GV.next_E = 2


def action4_2():    
    global current_Aspiration_count
    if (GV.PAUSE == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S4,E2 -> action4_2\n" " going to S4/E5"
        return 
    if (GV.ERROR == True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = "S4,E2 -> action4_2\n" " going to S4/E6"
        return          

    current_Aspiration_count += 1
    total_asipiration_number = RECIPE["Degas"]["total_asipiration_number"]    
    if (current_Aspiration_count < total_asipiration_number):
        GV.next_E = 3
        str1 = "Aspiration count = {}/{}\n".format(current_Aspiration_count+1, total_asipiration_number) 
        str1 += "aspiration count not reached yet\n"
        GV.SM_TEXT_TO_DIAPLAY =str1 
    else:
        GV.next_E = 4
        str1 = "Aspiratin count reached" "  go to S4/E3"
        GV.SM_TEXT_TO_DIAPLAY = str1


def action4_3():
    if (GV.PAUSE == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S4,E3 -> action4_3" "  going to S4/E5"    
    if (GV.ERROR == True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = "S4,E3 -> action4_3" " going to S4/E6"
        return
    GV.SM_TEXT_TO_DIAPLAY = "  going back to S2/E0"
    GV.next_E = 0


def action4_4():
    if (GV.PAUSE == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S4,E4 -> action4_4" "  going to S4/E5"
    if (GV.ERROR == True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = "S4,E4 -> action4_4" " going to S4/E6"
        return
    GV.SM_TEXT_TO_DIAPLAY =  "  going to S5/E0"
    GV.next_E = 0


def action4_5():
    if (GV.ERROR == True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = "S4,E5 -> action4_5" " going to S4/E6"
        return    
    GV.next_E = 0
    GV. prev_S = 4
    GV.SM_TEXT_TO_DIAPLAY = "S4,E5 -> action4_3" "  going to S6/E0"


def action4_6():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S4,E6 -> action4_6" " going to ERROR state"


#-------------------------------------------------------------------------------------------
def action5_0():
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "  goint to S5/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY =  "  goint to S5/E4"
        return    
    GV.SM_TEXT_TO_DIAPLAY ="Set TEC to experiment temperature"
    GV.next_E = 1


def action5_1():
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S5,E1 -> action5_1" "  goint to S5/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S5,E1 -> action5_1" "  goint to S5/E4"
        return 
    GV.tec.disable()    
    # experiment_temp = RECIPE["Degas"]["RECIPE"]
    # GV.TEC_TARGET =   experiment_temp
    # GV.tec.set_temp(float(experiment_temp))
    time.sleep(1)
    tec_dic =  GV.tec.get_data()
    # obj_temp = round(tec_dic['object temperature'][0], 1)
    # target_temp = round(tec_dic['target object temperature'][0], 1)
    TEC_cur_status = tec_dic['loop status'][0]        
    logger.info('\t\tTurning off the TEC controller:     TEC status is {}'.format( TEC_cur_status))  
    GV.TEC_IS_ON = False
    GV.terminate_SM = True
    GV.next_E = 2
    GV.SM_TEXT_TO_DIAPLAY = "Degasing completed\n" "returning to the main GUI"
    

def action5_2():
    if (GV.ERROR == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S5,E2 -> action5_2" "  goint to S5/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S5,E2 -> action5_2" "  goint to S5/E4"
        return 

    GV.SM_TEXT_TO_DIAPLAY =" terminate the SM"
    GV.terminate_SM = True
    GV.next_E = 0

def action5_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S5,E3 -> action5_3" "  goint to S5/E4"
        return 
    
    GV.SM_TEXT_TO_DIAPLAY ="S5,E3 -> action5_3\n "" going to PAUSE state"
    GV.next_E = 0
    GV. prev_S = 5
    

def action5_3():
    GV.SM_TEXT_TO_DIAPLAY ="S5,E4 -> action5_4\n" "  going to ERROR state"
    GV.next_E = 0
    GV. prev_S = 5


#--------------
def action6_0():
    if (GV.PAUSE == True):
        GV.SM_TEXT_TO_DIAPLAY ="S6,E0 -> action6_0"
        GV.next_E = 0
    else:
        GV.SM_TEXT_TO_DIAPLAY ="S6,E0 -> action6_0\n" " prepare to resume workflow"
        GV.next_E = GV. prev_S    

def action6_1():
    # logger.info("S6,E1 -> action6_1")
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S6,E1 -> action6_1\n" "  going back to S1/E0"

def action6_2():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S6,E2 -> action6_2\n""  going back to S2/E0"

def action6_3():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S6,E3 -> action6_3\n""  going back to S3/E0"

def action6_4():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S6,E4 -> action6_4\n""  going back to S4/E0"

def action6_5():
    GV.next_E = 0
    # logger.info("S6,E5 -> action6_5")
    GV.SM_TEXT_TO_DIAPLAY ="S6,E5 -> action6_5\n""  going back to S5/E0"

def action6_6():
    GV.next_E = 0
    # logger.info("S6,E5 -> action6_5")
    GV.SM_TEXT_TO_DIAPLAY ="S6,E6 -> action6_6\n""  going to S6/E6"


#--------------
def action7_0():
    logger.info("S7,E0 -> action7_0")
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S7,E0 -> action7_0"

