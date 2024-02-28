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

mixing_signal_start_time = 0
mixing_signal_wait_time = 0
equi_signal_start_time = 0
equi_signal_wait_time = 0
dose_standby_start_time=  0
dose_standby_wait_time = 0
##-----------------   ("next STATE","FUCNCTION") --------------------------------------------------
#-------------   -------E0-------    ------E1-------  -------E2-------  -------E3-------  -------E4-------  -------E5-------  -------E6-------  
TT = np.array([[( 1, 'action0_0'),  (0, 'None')     , (0, 'None')     , (0, 'None')     , (0, 'None')     , (0, 'None')     , (0, 'None')      ],  #<---STATE0
               [( 1, 'action1_0'),  (2, 'action1_1'), (6, 'action1_2'), (7, 'action1_3'), (0, 'None')     , (0, 'None')     , (0, 'None')      ],  #<---STATE1
               [( 2, 'action2_0'),  (2, 'action2_1'), (3, 'action2_2'), (6, 'action2_3'), (7, 'action2_4'), (0, 'None')     , (0, 'None')      ],  #<---STATE2
               [( 3, 'action3_0'),  (4, 'action3_1'), (6, 'action3_2'), (7, 'action3_3'), (0, 'None')     , (0, 'None')     , (0, 'None')      ],  #<---STATE3
               [( 4, 'action4_0'),  (4, 'action4_1'), (4, 'action4_2'), (5, 'action4_3'), (3, 'action4_4'), (6, 'action4_5'), (7, 'action4_6') ],  #<---STATE4
               [( 5, 'action5_0'),  (5, 'action5_1'), (5, 'action5_2'), (6, 'action5_3'), (7, 'action5_4'), (0, 'None')     , (0, 'None')      ],  #<---STATE5
               [( 6, 'action6_0'),  (1, 'action6_1'), (2, 'action6_2'), (3, 'action6_3'), (4, 'action6_4'), (5, 'action6_5'), (0, 'None')      ],  #<---STATE6
               [( 7, 'action7_0'),  (0, 'None')     , (0, 'None')     , (0, 'None')     , (0, 'None')     , (0, 'None')     , (0, 'None')      ]   #<---STATE7
               ])  

def name():
    return "Experiment"


state_name = {0:"S0: Initialization", 1:"S1: CheckPos", 2:"S2: Mix", 3:"S3: DoseStandby", 
              4:"S4: Dose", 5:"S5: Experiment", 6:"GV.PAUSE", 7:"GV.ERROR"}





#---------------  ACTIONS  --------------
def action0_0():

    #seting the scale factor for converting volume to pump position units
    sample_pump_step = RECIPE["Experiment"]["sample_pump_step"]
    titrant_pump_step = RECIPE["Experiment"]["titrant_pump_step"]
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

    GV.pump1.set_valve(HW.TIRRANT_PUMP_ADDRESS, HW.VALVE1_P2)
    time.sleep(1)
    GV.pump1.set_valve(HW.TITRANT_LOOP_ADDRESS, HW.VALVE3_P3)
    time.sleep(1)
    GV.pump1.set_valve(HW.TITRANT_PIPETTE_ADDRESS,HW.VALVE5_P1)
    time.sleep(1)
    GV.pump1.set_multiwayvalve(HW.TITRANT_CLEANING_ADDRESS,HW.VALVE9_P2)        
    time.sleep(1)
    pump1_speed = int(RECIPE["Experiment"]["titrant_pump_speed"] * GV.PUMP_TITRANT_SCALING_FACTOR)
    pump2_speed = int(RECIPE["Experiment"]["sample_pump_speed"] * GV.PUMP_SAMPLE_SCALING_FACTOR)
    GV.pump1.set_speed(HW.TIRRANT_PUMP_ADDRESS, pump1_speed)
    time.sleep(1)
    GV.pump1.set_speed(HW.SAMPLE_PUMP_ADDRESS, pump2_speed)
    time.sleep(1)

    str1  = "SM initialized ..." "V1 to Line to Pump\n" "V3 to Titrant Line\n" 
    str1 = str1 + "V5 to Titrant Port\n" " V9 to Air\n" 
    GV.VALVE_1 = "Line to Pump"
    GV.VALVE_3 = "Titrant Line"
    # GV.VALVE_4 = "Titrant Port"
    GV.VALVE_5 = "Titrant Cannula"
    GV.VALVE_9 = "V9 to Air"
    GV.SM_TEXT_TO_DIAPLAY = str1
    GV.next_E = 0    


#--------------
def action1_0():

    if (GV.PAUSE == True):
        GV.next_E = 2            
        GV.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0\n" "Prepare to go to PAUSE State"
        return 
    if (GV.ERROR == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0\n" "Prepare to go to ERROR State"
        return 
    GV.SM_TEXT_TO_DIAPLAY = "Gantry Z is moving to lowered position"
    GV.next_E = 1    


def action1_1():
    global mixing_signal_start_time

    if (GV.PAUSE == True):
        GV.next_E = 2            
        GV.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" "Prepare to go to PAUSE State"
        return 
    if (GV.ERROR == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" "Prepare to go to ERROR State"
        return 
    #Vertical Gantry to z position
    GV.motors.select_axis(HW.GANTRY_VER_AXIS_ID)
    v_position = RECIPE["GantrytoB"]["vertical_titration_position"]    
    # GV.motors.set_POSOKLIM(1)    
    next_pos = int(v_position / HW.TML_LENGTH_2_MM_VER )
    # move_speed = RECIPE['GantrytoB']['gantry_move_speed'] 
    # logger.info("Moving gantry to pos: {}".format(next_pos))
    # GV.motors.move_absolute_position(next_pos, move_speed, HW.GANTRY_VER_ACCELERATION)
    ##wait until move is done
    cur_motor_pos= GV.motors.read_actual_position()
    # while ( abs(cur_motor_pos - next_pos) > 10):
    #     time.sleep(1)
    #     cur_motor_pos= GV.motors.read_actual_position()
    logger.info("\t\tV. Gantry  current pos: {},  Lower position:{}".format(cur_motor_pos, next_pos))
    if ( abs(cur_motor_pos - next_pos) > 10):
        GV.SM_TEXT_TO_DIAPLAY = "Gantry not in lower position\n""going to error state"
        GV.next_E = 0
    else:
        # GV.vertical_gantry_active_led = False
        GV.SM_TEXT_TO_DIAPLAY =  "Waiting for Mixing Signal"
        mixing_signal_start_time = time.time()
        logger.info("\tWaiting for Mixing Signal")
        GV.next_E = 0


def action1_2():
    if (GV.ERROR == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S1,E2 -> action1_2\n" "Prepare to go to ERROR State"
        return     
    GV.next_E = 0
    GV.prev_S = 1
    GV.SM_TEXT_TO_DIAPLAY ="S1,E2 -> action1_2\n\tgo to PAUSE state"

    
def action1_3():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY = "S1,E3 -> action1_3\n\tgoing to GV.ERROR state"

#--------------    
def action2_0():
    global mixing_signal_start_time
    global mixing_signal_wait_time
    global equi_signal_start_time
    if (GV.PAUSE == True):
        GV.next_E = 3            
        GV.SM_TEXT_TO_DIAPLAY = "S2,E0 -> action2_1\n" "Prepare to go to PAUSE State"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S2,E0 -> action2_1\n" "Prepare to go to ERROR State"
        return 
         
    mixingsignal_timeout = RECIPE["Experiment"]["mixingsignal_timeout"]
    #wait for mixing signal from thermal core        
    result = GV.grPC_Client.get_url(message="Mixing_Signal_Ready")
    # print(f'{result}')
    # print('==============',result.message)
    # print('==============',result.value)
    if result.message == "Mixing_Signal_Ready":
        if result.value == 1:
            logger.info('\tmixing signal is ready')
            GV.MixingSignalReady = True
        else:
            # print('mixing signal is not ready')
            GV.MixingSignalReady = False
    #measure the wait time
    mixing_signal_wait_time = time.time() - mixing_signal_start_time

    logger.info("\t\tMixing wait time:{:.0f} / {:.0f}".format(mixing_signal_wait_time, mixingsignal_timeout))
    time.sleep(1)
    if (mixing_signal_wait_time > mixingsignal_timeout):
        GV.next_E = 4
        str1 =  "mixing signal timeout\n" "going to error state"    
    elif (GV.MixingSignalReady==True):
        GV.next_E = 1
        equi_signal_start_time = time.time()
        logger.info("\tWaiting for Equlibrium Signal")
        str1 = "Waiting for  equilibrium signal..." 
        mixing_speed = RECIPE["Experiment"]["mixing_speed"]
        GV.motors.select_axis(HW.MIXER_AXIS_ID)
        acceleration = 1        # mixing motor acceleration
        GV.motors.set_speed(mixing_speed,acceleration)
        GV.MIXING_SPEED = mixing_speed                  #to update the GUI experiment    
    else:        
        GV.next_E = 0
        str1 = "Mixing signal Not Ready\n" "Waiting for mixing signal"
    GV.SM_TEXT_TO_DIAPLAY =str1



def action2_1():
    global equi_signal_start_time
    global equi_signal_wait_time
    if (GV.PAUSE == True):
        GV.next_E = 3           
        GV.SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1\n" "Prepare to go to PAUSE State"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1\n" "Prepare to go to ERROR State"
        return     
    #wait for dose ready signal from thermal core
    equilsignal_timeout = RECIPE["Experiment"]["equilsignal_timeout"]
    result = GV.grPC_Client.get_url(message="Equilibrium_Reached")
    # print(f'{result}')
    # print('==============',result.message)
    # print('==============',result.value)
    if result.message == "Equilibrium_Reached":
        if result.value > 0:
            logger.info('\tequi. reached')
            GV.EquilibriumReached = True            
        else:
            # print('equil. not reached')
            GV.EquilibriumReached = False
            
    #measure the wait time
    equi_signal_wait_time = time.time() - equi_signal_start_time
    logger.info("\t\tEquilibrium wait time:{:.0f} / {:.0f}".format(equi_signal_wait_time, equilsignal_timeout))
    time.sleep(1)

    if (equi_signal_wait_time > equilsignal_timeout):
        GV.next_E = 4
        str1 =  "Equlibrium signal timeout\n" "going to error state"    
    elif (GV.EquilibriumReached == True):
        GV.next_E = 2
        str1 = "\tEqulibrium Reached\n"
    else:
        GV.next_E = 1
        str1 = "\tMixing Motor Speed = {}\n""\tEqulibrium not reached yet\n".format(RECIPE["Experiment"]["mixing_speed"])
    GV.SM_TEXT_TO_DIAPLAY =str1
    

def action2_2():
    global dose_standby_start_time
    #preprate to go to S3
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="Dose signal not recieved\n" "Waiting for Dose Signal"
    dose_standby_start_time = time.time()
    logger.info("\tWaiting for Dose Signal")


def action2_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S2,E3 -> action2_3\n" "Prepare to go to GV.ERROR State"
        return         
    # print("S2,E3 -> action2_3")
    GV.next_E = 0
    GV.prev_S = 2
    GV.SM_TEXT_TO_DIAPLAY ="S2,E3 -> action2_3\n"


def action2_4():
    # print("S2,E4 -> action2_4")
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S2,E4 -> action2_4\n"


#--------------
def action3_0():
    global dose_standby_start_time
    global dose_standby_wait_time
    if (GV.PAUSE == True):
        GV.next_E = 2          
        GV.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0\n" "Prepare to go to PAUSE State"
        return 
    if (GV.ERROR == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0\n" "Prepare to go to ERROR State"
        return 
    dosesignal_timeout = RECIPE["Experiment"]["dosesignal_timeout"]
    #check if dose signal is receved 
    result = GV.grPC_Client.get_url(message="Dose_Signal_Ready")
    # print(f'{result}')
    # print('==============',result.message)
    # print('==============',result.value)
    if result.message == "Dose_Signal_Ready":
        if result.value > 0 :
            logger.info('\tDose signal recieved')
            GV.DoseSignalRecived = True
        else:
            # print('Dose signal not recieved')
            GV.DoseSignalRecived = False

    #measure the wait time
    dose_standby_wait_time = time.time() - dose_standby_start_time
    logger.info("\t\tDose recieve wait time:{:.0f} / {:.0f}".format(dose_standby_wait_time, dosesignal_timeout))
    time.sleep(1)

    if (dose_standby_wait_time > dosesignal_timeout):
        GV.next_E = 3
        str1 = "Dose standby timout"
    elif (GV.DoseSignalRecived == True):
        GV.next_E = 1
        str1 = "\tDose Signal Ready: OK"
    else:
        GV.next_E = 0
        str1 = "Dose signal not recieved\n" "Waiting for Dose Signal"
    GV.SM_TEXT_TO_DIAPLAY =str1


def action3_1():
    if (GV.PAUSE == True):
        GV.next_E = 2          
        GV.SM_TEXT_TO_DIAPLAY = "S3,E1 -> action3_1\n" "Prepare to go to PAUSE State"
        return 
    if (GV.ERROR == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S3,E1 -> action3_1\n" "Prepare to go to ERROR State"
        return         
    #prepare to go to S4
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S3,E1 -> action3_1\n""\tPreparing to go to S4/E0"


def action3_2():
    if (GV.ERROR == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "Pump 1 to position xx(dose)"
        return     
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S3,E2 -> action3_2\n"


def action3_3():
    GV.next_E = 0
    GV.prev_S = 3
    GV.SM_TEXT_TO_DIAPLAY ="S3,E3 -> action3_3\n"


#--------------
def action4_0():
    if (GV.PAUSE == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S4,E0 -> action4_0\n" "Prepare to go to PAUSE State"
        return 
    if (GV.ERROR == True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = "S4,E0 -> action4_0\n" "Prepare to go to ERROR State"
        return 
    
    dose_volume = RECIPE["Experiment"]["dose_volume"]
    #pump 1 to position xxx
    GV.next_E = 1    
    GV.SM_TEXT_TO_DIAPLAY ="Pump 1 to position {}".format(dose_volume)

def action4_1():
    if (GV.PAUSE == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1\n" "Prepare to go to GV.PAUSE State"
        return 
    if (GV.ERROR == True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1\n" "Prepare to go to GV.ERROR State"
        return 
        
    dose_volume = RECIPE["Experiment"]["dose_volume"]
    GV.DOSE_VOLUME = dose_volume        # to update the GUI experiment
    pump_address1 = HW.TIRRANT_PUMP_ADDRESS
    pump_pos1 = GV.pump1.get_plunger_position(pump_address1)
    next_pos1 =  pump_pos1 - dose_volume   #it's a dispense motion
    time.sleep(1)
    GV.pump1.set_pos_absolute(pump_address1, next_pos1)
    time.sleep(1)
    # logger.info("\tPump1 pos: {},  target: {}".format(pump_pos1, next_pos1))    
    while (pump_pos1 != next_pos1 ):
        pump_pos1 = GV.pump1.get_plunger_position(pump_address1)        
        time.sleep(0.5)
        print("\t\tpump1 pos:",pump_pos1, "/", next_pos1)
        time.sleep(0.5)
    time.sleep(5)
    GV.next_E = 2
    str1 = "\tPump In Position: OK"
    GV.SM_TEXT_TO_DIAPLAY = str1


def action4_2():    
    global dose_standby_start_time 
    if (GV.PAUSE == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1\n" "Prepare to go to PAUSE State"
        return 
    if (GV.ERROR == True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1\n" "Prepare to go to ERROR State"
        return          
    
    totaldose_count = RECIPE["Experiment"]["totaldose_count"]
    GV.TOTAL_DOSES = totaldose_count        #to update the GUI experiment
    #increment dose number variable
    GV.current_dose_volume += 1
    GV.DOSE_COMPLETED = GV.current_dose_volume          #to update the GUI experiment
    #check if dose count is reached:
    if GV.current_dose_volume >= totaldose_count:
        GV.next_E = 3
        str1 = "Dose completed"
    else:
        str1 = 'dose number {} is done '.format(GV.current_dose_volume)
        dose_standby_start_time = time.time()
        logger.info("\tWaiting for Dose Signal")
        GV.next_E = 4
    GV.SM_TEXT_TO_DIAPLAY ="S4,E2 -> action4_2\n" + str1


def action4_3():     
    if (GV.PAUSE == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S4,E3 -> action4_3\n" "Prepare to go to PAUSE State"
        return 
    if (GV.ERROR == True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = "S4,E3 -> action4_3\n" "Prepare to go to ERROR State"
        return         
    # print("S4,E3 -> action4_3")
    GV.next_E = 0
    GV.prev_S = 4
    GV.SM_TEXT_TO_DIAPLAY = "S4,E3 -> action4_3\n""SM completed"  "Terminating SM"


def action4_4():
    if (GV.PAUSE == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S4,E4 -> action4_4\n" "Prepare to go to PAUSE State"
        return 
    if (GV.ERROR == True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = "S4,E4 -> action4_4\n" "Prepare to go to ERROR State"
        return                
    # print("S4,E4 -> action4_4")
    GV.next_E = 0
    GV.prev_S = 4
    GV.SM_TEXT_TO_DIAPLAY ="S4,E4 -> action4_4\n"


def action4_5():
    if (GV.ERROR == True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = "S4,E5 -> action4_5\n" "Prepare to go to GV.ERROR State"
        return          
    # print("S4,E5 -> action4_5")
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S4,E5 -> action4_5\n"


def action4_6():
    # print("S4,E6 -> action4_6")
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S4,E6 -> action4_6\n"


#-------------- 
def action5_0():
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S5,E0 -> action5_0\n" "Prepare to go to PAUSE State"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S5,E0 -> action5_0\n" "Prepare to go to ERROR State"
        return                
    # experiment is complete
    GV.next_E = 1
    GV.SM_TEXT_TO_DIAPLAY ="S5,E0 -> action5_0\n" "\tSTATE 5: Experiment complete"


def action5_1(): 
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S5,E1 -> action5_1\n" "Prepare to go to PAUSE State"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S5,E1 -> action5_1\n" "Prepare to go to ERROR State"
        return     
    # Turn off the mixing motor
    GV.motors.select_axis(HW.MIXER_AXIS_ID)
    acceleration = 1        # mixing motor acceleration
    mixing_speed = 0
    GV.motors.set_speed(mixing_speed,acceleration)
    GV.MIXING_SPEED = mixing_speed                  #to update the GUI experiment

    GV.terminate_SM = True
    # print("S5,E1 -> action5_1")
    GV.next_E = 2
    GV.SM_TEXT_TO_DIAPLAY ="Experiment completed\n"
    

def action5_2(): 
    if (GV.PAUSE == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S5,E2 -> action5_2\n" "Prepare to go to PAUSE State"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S5,E2 -> action5_2\n" "Prepare to go to ERROR State"
        return 
    
    GV.next_E = 0
    terminate_SM = True
    GV.SM_TEXT_TO_DIAPLAY ="S5,E2 -> action5_2 \n----> Terminate state machine"
    

def action5_3():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S5,E1 -> action5_1\n" "Prepare to go to ERROR State"
        return 
    
    GV.next_E = 0
    GV.prev_S = 5
    GV.SM_TEXT_TO_DIAPLAY = "S5,E3 -> action5_3\n"


def action5_4():

    # print("S5,E4 -> action5_4")
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S5,E4 -> action5_4\n"


#--------------
def action6_0():
    if (GV.PAUSE == True):
        GV.next_E = 0
    else:
        GV.next_E = GV.prev_S
    GV.SM_TEXT_TO_DIAPLAY ="S6,E0 -> action6_0\n"

def action6_1():
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S6,E1 -> action6_1"

def action6_2():
    global mixing_signal_wait_time
    mixing_signal_start_time = time.time()
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S6,E2 -> action6_2\n"

def action6_3():
    global dose_standby_start_time
    dose_standby_start_time = time.time()
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S6,E3 -> action6_3\n"

def action6_4():

    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S6,E4 -> action6_4\n"

def action6_5():

    GV.next_E = 0
    # print("S6,E5 -> action6_5")
    GV.SM_TEXT_TO_DIAPLAY ="S6,E5 -> action6_5\n"


#--------------
def action7_0():

    print("S7,E0 -> action7_0")
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S7,E0 -> action7_0\n"

#--------------