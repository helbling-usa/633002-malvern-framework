import  SM_GUI
from    tkinter import * 
import  tkinter.messagebox 
# from    config.motor_3axes import motor_3axes as Motors
# import  config.Pump as P
import  time
import  u6
import  threading
# import  config.MeerstetterTEC as TEC
import  json
import  logging
import sys
import numpy as np
import threading

#-------------- GENERAL GLOBAL VARIABLES -----------------------------------------
ZGANTRY_DOWN = False
PAUSE = False
ERROR = False
MIXING_READY = False
EQUILIBRIUM_READY = False
DOSE_SIGNAL_READY = False
PUMP_IN_POSITION = False
TOTAL_DOSE = 5
DELAY_TIME = 5
KILL_THREADS = False
SM_TEXT_TO_DIAPLAY = "-------"
TAKE_STEP = False
RESET = False
#------------ SM GLOBAL VARIABLES -------------------------------------------
next_E = 0 
cur_S = None
prev_S = None
terminate_SM = False
doescount = 5
dose_number = 0
##-----------------   ("next STATE","FUCNCTION") --------------------------------------------------
#-------------   -------E0-------    ------E1-------  -------E2-------  -------E3-------  -------E4-------  -------E5-------  -------E6-------  
TT_EXPERIMENT = np.array([[( 1, 'self.action0_0'),  (0, 'None')          , (0, 'None')          , (0, 'None')          , (0, 'None')          , (0, 'None')          , (0, 'None')          ],  #<---STATE0
                          [( 1, 'self.action1_0'),  (2, 'self.action1_1'), (6, 'self.action1_2'), (7, 'self.action1_3'), (0, 'None')          , (0, 'None')          , (0, 'None')          ],  #<---STATE1
                          [( 2, 'self.action2_0'),  (2, 'self.action2_1'), (3, 'self.action2_2'), (6, 'self.action2_3'), (7, 'self.action2_4'), (0, 'None')          , (0, 'None')          ],  #<---STATE2
                          [( 3, 'self.action3_0'),  (4, 'self.action3_1'), (6, 'self.action3_2'), (7, 'self.action3_3'), (0, 'None')          , (0, 'None')          , (0, 'None')          ],  #<---STATE3
                          [( 4, 'self.action4_0'),  (4, 'self.action4_1'), (4, 'self.action4_2'), (5, 'self.action4_3'), (3, 'self.action4_4'), (6, 'self.action4_5'), (7, 'self.action4_6')],  #<---STATE4               
                          [( 5, 'self.action5_0'),  (5, 'self.action5_1'), (5, 'self.action5_2'), (6, 'self.action5_3'), (7, 'self.action5_4'), (0, 'None')          , (0, 'None')          ],  #<---STATE5
                          [( 6, 'self.action6_0'),  (1, 'self.action6_1'), (2, 'self.action6_2'), (3, 'self.action6_3'), (4, 'self.action6_4'), (5, 'self.action6_5'), (0, 'None')          ],  #<---STATE6
                          [( 7, 'self.action7_0'),  (0, 'None')          , (0, 'None')          , (0, 'None')          , (0, 'None')          , (0, 'None')          , (0, 'None')          ]   #<---STATE7
                          ])  


#------------------ initialize logger -------------------------------------
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(levelname)s:%(message)s')
file_handler = logging.FileHandler('error.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)




class run_SM_GUI(SM_GUI.SM_GUI):

    global TT_EXPERIMENT
    def __init__(self,root):
        super().__init__( root)
        self.root = root
        logger.info("Initializing hardware -------------------------------------")
        self.InitTimer()
        logger.info("------------------------------------------------------------------")
        #initialize GUI
        self.init_GUI()        
        # #---- extract recipe for config.json
        self.read_recipe()
        logger.info('System started successfully.')
        logger.info("Please use the GUI to enter a commamnd ...")


    def init_GUI(self):
        self.total_dose.insert(1,str(TOTAL_DOSE))
        self.delay_time.insert(1,str(DELAY_TIME))
        self.b_run['state']=NORMAL
        self.b_step['state'] = DISABLED
        self.output.insert(END,"the states will be displayed here...")


    def read_recipe(self):
        with open('./config/recipe.json') as json_file:
            ports = json.load(json_file)
        self.MIXING_MOTOR_SPEED = ports['MIXING_MOTOR_SPEED']
        self.DOSE_VOLUME = ports['DOSE_VOLUME']
        self.PUMP_SPEED = ports['PUMP_SPEED']
        self.GANTRY_Z_LOWERED_POSITION = int(ports['GANTRY_Z_LOWERED_POSITION'])

        if is_float(self.MIXING_MOTOR_SPEED) == True:
            self.MIXING_MOTOR_SPEED = int(self.MIXING_MOTOR_SPEED)
        else:
            logger.error("Problem reading MIXING_MOTOR_SPEED from recipe file")
            sys.exit(0)
        if is_float(self.DOSE_VOLUME) == True:
            self.DOSE_VOLUME = int(self.DOSE_VOLUME)
        else:
            logger.error("Problem reading PUMP1_POSITION from recipe file")
            sys.exit(0)
        if is_float(self.GANTRY_Z_LOWERED_POSITION) == True:
            self.GANTRY_Z_LOWERED_POSITION = int(self.GANTRY_Z_LOWERED_POSITION)
        else:
            logger.error("Problem reading GANTRY_Z_LOWERED_POSITION from recipe file")
            sys.exit(0)
        if is_float(self.PUMP_SPEED) == True:
            self.PUMP_SPEED = int(self.PUMP_SPEED)
        else:
            logger.error("Problem reading PUMP_SPEED from recipe file")
            sys.exit(0)

        logger.info("MIXING_MOTOR_SPEED = {}".format(self.MIXING_MOTOR_SPEED))
        logger.info("GANTRY_Z_LOWERED_POSITION = {}".format(self.GANTRY_Z_LOWERED_POSITION))
        logger.info("DOSE_VOLUME = {}".format(self.DOSE_VOLUME))
        logger.info("PUMP_SPEED = {}".format(self.PUMP_SPEED))
        

    def timerCallback_1(self):  
        global SM_TEXT_TO_DIAPLAY
        # logger.debug('timer is running')
        self.output.delete("1.0","end")
        
        self.output.insert(END,SM_TEXT_TO_DIAPLAY)
        self.cur_dose.config(text = str(dose_number))
        #-------- repeat the timer ----------------------------------------------
        self.timer = threading.Timer(1.0, self.timerCallback_1)
        self.timer.start()
        


    def checkExitButton(self):
        global KILL_THREADS
        logger.debug("exit button pressed ...")
        KILL_THREADS = True
        self.timer.cancel()
        self.root.destroy()
        sys.exit(0)

    def InitTimer(self):
        # #------ Starts timer
        logger.info('starting internal timer')
        self.timer = threading.Timer(1.0, self.timerCallback_1)
        self.timer.start()
        logger.info('\t\tInternal timer started')


    def checkPumpInPosition(self):
        global PUMP_IN_POSITION
        logger.debug("pump in position button is pressed ...")
        if PUMP_IN_POSITION == False:
            PUMP_IN_POSITION = True
            self.b_pump.config(text ="Pump in Position\nTRUE",)
            logger.debug('pump in position: true')
        else:
            PUMP_IN_POSITION = False
            self.b_pump.config(text ="Pump In Position\nFALSE",)
            logger.debug('pump in position: false')


    def checkZGantryButton(self):
        global ZGANTRY_DOWN
        logger.debug("Z gantry  button is pressed ...")
        if ZGANTRY_DOWN == False:
            ZGANTRY_DOWN = True
            self.b_gantry.config(text ="Z Gantry Position\nDOWN",)
            logger.debug('Z Gantry position is DOWN')
        else:
            ZGANTRY_DOWN = False
            self.b_gantry.config(text ="Z Gantry Position\nHIGH",)
            logger.debug('Z Gantry position is HIGH')


    def checkPauseButton(self):
        global PAUSE
        logger.debug("Pause button pressed ...")
        if PAUSE == False:
            PAUSE = True
            logger.debug('pause button is TRUE')
            self.b_pause.config(text="System\nPAUSED")
        else:
            PAUSE = False
            logger.debug('pause button is FALSE')
            self.b_pause.config(text="Press to\nPAUSE")


    def checkErrorButton(self):
        global ERROR
        logger.debug("Error button pressed ...")
        if ERROR == False:
            ERROR = True
            logger.debug('Error button is Activated')
            self.b_error.config(text="Error\nActivated")
        else:
            ERROR = False
            logger.debug('Error button is Deactivated')
            self.b_error.config(text="Create\nERROR")


    def checkResetButton(self):
        global RESET
        logger.debug(" Reset button pressed ...")
        RESET = True

        
    def checkMixingButton(self):        
        global MIXING_READY
        logger.debug("Mixing button pressed ...")
        if (MIXING_READY==False):
            self.b_mix.config(text="Mixing Signal Ready\n True")
            logger.debug("Mixing signal ready: True")
            MIXING_READY = True
        else:
            self.b_mix.config(text="Mixing Signal Ready\n False")
            logger.debug("Mixing signal ready: False")
            MIXING_READY = False


    def checkEqulibriumButton(self):
        global EQUILIBRIUM_READY
        logger.debug("Equilibrium  button pressed ...")
        if (EQUILIBRIUM_READY==False):
            self.b_equi.config(text="Equilibrium Reached\n True")
            logger.debug("Equlib. signal ready: True")
            EQUILIBRIUM_READY = True
        else:
            self.b_equi.config(text="Equlibrium Reached\n False")
            logger.debug("Equilib. signal ready: False")
            EQUILIBRIUM_READY = False


    def checkDoseRecievedButton(self):
        global DOSE_SIGNAL_READY
        logger.debug("Dose receibed  button pressed ...")
        if (DOSE_SIGNAL_READY==False):
            self.b_dose.config(text="Dose Signal Recieved\n True")
            logger.debug("Dose Signal Recieved: True")
            DOSE_SIGNAL_READY = True
        else:
            self.b_dose.config(text="Dose Signal Recieved\n False")
            logger.debug("Dose Signal Recieved: False")
            DOSE_SIGNAL_READY = False   


    def check_Set_Dose_Button(self):   
        global TOTAL_DOSE
        logger.debug("set dose button pressed ...")
        s = self.total_dose.get()        
        if (is_float(s) == True):
            TOTAL_DOSE = int(s)
            logger.debug("Total Dose = {}".format(s))
            


    def check_Set_Delay_Time(self):
        global DELAY_TIME
        logger.debug("parent: set delay time ...")
        s = self.delay_time.get()        
        if (is_float(s) == True):
            DELAY_TIME = int(s)
            logger.debug("delay time = {}".format(s))


    def checkRunSMButton(self):
        logger.debug("parent: Run SM ...")
        # self.execute()
        self.t1 = threading.Thread(target=self.execute, name='SM_experiment')
        self.t1.start()
        self.b_run['state']=DISABLED
        self.b_step['state'] = NORMAL


    def checkStepSMButton(self):
        global TAKE_STEP
        logger.debug("child: Step through SM ...")
        TAKE_STEP = True






    #---------------  ACTIONS  --------------
    def action0_0(self):
        global SM_TEXT_TO_DIAPLAY
        global next_E
        # print("S0,E0 -> action0_0")
        # print("\tSM initialized ...")
        # print("\tall tirtrant valves to default position")
        SM_TEXT_TO_DIAPLAY = "S0,E0 -> action0_0\n"         
        "\tV1 to Line to Pump\n"
        "\tV3 to Titrant Line\n"
        "\tV5 to Titrant Port\n"
        "\tV9 to Air\n"
        "SM initialized ..."
        next_E = 0    


    #--------------
    def action1_0(self):
        global SM_TEXT_TO_DIAPLAY
        global ZGANTRY_DOWN
        global next_E
        global PAUSE
        global ERROR

        if (PAUSE == True):
            next_E = 2            
            SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0\n" "Prepare to go to Pause State"
            return 
        if (ERROR == True):
            next_E = 3
            SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0\n" "Prepare to go to error State"
            return 
        
        # check gantryZ is in lowered position        
        if ZGANTRY_DOWN == True:
            str1 = "\tGantry Z is in lowered position"         
            next_E = 1    
        else:
            str1 = "\tGantry Z is NOT in lowered position.\nGoing to error state"
            next_E = 3
        # print(str1)
        SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0\n" + str1

    def action1_1(self):
        global SM_TEXT_TO_DIAPLAY
        global next_E
        global PAUSE     
        global ERROR
        if (PAUSE == True):
            next_E = 2            
            SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" "Prepare to go to Pause State"
            return 
        if (ERROR == True):
            next_E = 3
            SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" "Prepare to go to error State"
            return 
        
        next_E = 0
        SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" "\tpreprate to go to STATE2"

    def action1_2(self):
        global SM_TEXT_TO_DIAPLAY
        global next_E, prev_S
        global ERROR
        if (ERROR == True):
            next_E = 3
            SM_TEXT_TO_DIAPLAY = "S1,E2 -> action1_2\n" "Prepare to go to error State"
            return     
        next_E = 0
        prev_S = 1
        SM_TEXT_TO_DIAPLAY ="S1,E2 -> action1_2\n\tgo to PAUSE state"
        
    def action1_3(self):
        global SM_TEXT_TO_DIAPLAY
        global next_E
        next_E = 0
        SM_TEXT_TO_DIAPLAY = "S1,E3 -> action1_3\n\tgoing to ERROR state"

    #--------------    
    def action2_0(self):
        global SM_TEXT_TO_DIAPLAY
        global next_E
        global MIXING_READY
        global PAUSE     
        global ERROR
        if (PAUSE == True):
            next_E = 3            
            SM_TEXT_TO_DIAPLAY = "S2,E0 -> action2_1\n" "Prepare to go to Pause State"
            return 
        if (ERROR == True):
            next_E = 4
            SM_TEXT_TO_DIAPLAY = "S2,E0 -> action2_1\n" "Prepare to go to error State"
            return 
        
        #wait for mixing signal from thermal core        
        if (MIXING_READY==True):
            next_E = 1
            str1 = "\tMixing signal OK"
        else:
            next_E = 0
            str1 = "\tMixing signal Not Ready"
        SM_TEXT_TO_DIAPLAY ="S2,E0 -> action2_0\n" +str1

    def action2_1(self):
        global SM_TEXT_TO_DIAPLAY
        global next_E
        global EQUILIBRIUM_READY
        global PAUSE     
        global ERROR
        if (PAUSE == True):
            next_E = 3           
            SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1\n" "Prepare to go to Pause State"
            return 
        if (ERROR == True):
            next_E = 4
            SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1\n" "Prepare to go to error State"
            return 
                
        # print("S2,E1 -> action2_1")
        #wait for dose ready signal from thermal core
        str0 = "\tMixing Motor Speed = xxx\n"
        if (EQUILIBRIUM_READY == True):
            next_E = 2
            str1 = "\tEqulibrium Reached\n"
        else:
            next_E = 1
            str1 = "\tEqulibrium not reached yet\n"
        SM_TEXT_TO_DIAPLAY ="S2,E1 -> action2_1\n" + str0 + str1
        
    def action2_2(self):
        global SM_TEXT_TO_DIAPLAY
        global next_E
        #preprate to go to S3
        next_E = 0
        SM_TEXT_TO_DIAPLAY ="S2,E2 -> action2_2\n" "\tpreparing to go to S3/E0"

    def action2_3(self):
        global SM_TEXT_TO_DIAPLAY
        global next_E, prev_S
        global ERROR
        if (ERROR == True):
            next_E = 4
            SM_TEXT_TO_DIAPLAY = "S2,E3 -> action2_3\n" "Prepare to go to error State"
            return         
        # print("S2,E3 -> action2_3")
        next_E = 0
        prev_S = 2
        SM_TEXT_TO_DIAPLAY ="S2,E3 -> action2_3\n"

    def action2_4(self):
        global SM_TEXT_TO_DIAPLAY
        global next_E
        # print("S2,E4 -> action2_4")
        next_E = 0
        SM_TEXT_TO_DIAPLAY ="S2,E4 -> action2_4\n"


    #--------------
    def action3_0(self):
        global SM_TEXT_TO_DIAPLAY
        global next_E
        global DOSE_SIGNAL_READY
        global PAUSE     
        global ERROR
        if (PAUSE == True):
            next_E = 2          
            SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0\n" "Prepare to go to Pause State"
            return 
        if (ERROR == True):
            next_E = 3
            SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0\n" "Prepare to go to error State"
            return 
        #check if dose signal is receved 
        # dose_ready_signal_ok = True
        if (DOSE_SIGNAL_READY == True):
            next_E = 1
            str1 = "\tDose Signal Ready: OK"
        else:
            next_E = 0
            str1 = "\tDose Signal Not Ready yet. Waiting"
        SM_TEXT_TO_DIAPLAY ="S3,E0 -> action3_0\n"+str1

    def action3_1(self):
        global SM_TEXT_TO_DIAPLAY
        global next_E
        global PAUSE     
        global ERROR
        if (PAUSE == True):
            next_E = 2          
            SM_TEXT_TO_DIAPLAY = "S3,E1 -> action3_1\n" "Prepare to go to Pause State"
            return 
        if (ERROR == True):
            next_E = 3
            SM_TEXT_TO_DIAPLAY = "S3,E1 -> action3_1\n" "Prepare to go to error State"
            return         
        #prepare to go to S4
        next_E = 0
        SM_TEXT_TO_DIAPLAY ="S3,E1 -> action3_1\n""\tPreparing to go to S4/E0"

    def action3_2(self):
        global SM_TEXT_TO_DIAPLAY
        global next_E
        global ERROR
        if (ERROR == True):
            next_E = 3
            SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0\n" "Prepare to go to error State"
            return 
        
        next_E = 0
        SM_TEXT_TO_DIAPLAY ="S3,E2 -> action3_2\n"

    def action3_3(self):
        global SM_TEXT_TO_DIAPLAY
        global next_E, prev_S
        # print("S3,E3 -> action3_3")
        next_E = 0
        prev_S = 3
        SM_TEXT_TO_DIAPLAY ="S3,E3 -> action3_3\n"

    #--------------
    def action4_0(self):
        global SM_TEXT_TO_DIAPLAY
        global next_E
        global PAUSE     
        global ERROR
        if (PAUSE == True):
            next_E = 5
            SM_TEXT_TO_DIAPLAY = "S4,E0 -> action4_0\n" "Prepare to go to Pause State"
            return 
        if (ERROR == True):
            next_E = 6
            SM_TEXT_TO_DIAPLAY = "S4,E0 -> action4_0\n" "Prepare to go to error State"
            return 
        
        #pump 1 to position xxx
        next_E = 1
        
        SM_TEXT_TO_DIAPLAY ="S4,E0 -> action4_0\n" "\tSend Pump 1 to position xxx\n"

    def action4_1(self):
        global SM_TEXT_TO_DIAPLAY
        global next_E
        global PUMP_IN_POSITION
        global PAUSE     
        global ERROR
        if (PAUSE == True):
            next_E = 5
            SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1\n" "Prepare to go to Pause State"
            return 
        if (ERROR == True):
            next_E = 6
            SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1\n" "Prepare to go to error State"
            return 
        
        #check pump position"
        if (PUMP_IN_POSITION == True):
            next_E = 2
            str1 = "\tPump In Position: OK"
        else:
            next_E = 1
            str1 = "\tPump Not in Position"

        SM_TEXT_TO_DIAPLAY ="S4,E1 -> action4_1\n"+ str1

    def action4_2(self):
        global SM_TEXT_TO_DIAPLAY
        global next_E, dose_number, doescount   
        global PAUSE     
        global ERROR        
        if (PAUSE == True):
            next_E = 5
            SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1\n" "Prepare to go to Pause State"
            return 
        if (ERROR == True):
            next_E = 6
            SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1\n" "Prepare to go to error State"
            return          
        #increment dose number variable
        dose_number += 1        
        #check if dose count is reached:
        if dose_number > doescount:
            next_E = 3
            str1 = "\tDose completed"
        else:
            str1 = '\tdose number:{} is in process...'.format(dose_number)
            next_E = 4
        SM_TEXT_TO_DIAPLAY ="S4,E2 -> action4_2\n" + str1


    def action4_3(self):
        global SM_TEXT_TO_DIAPLAY
        global next_E, prev_S
        global PAUSE     
        global ERROR        
        if (PAUSE == True):
            next_E = 5
            SM_TEXT_TO_DIAPLAY = "S4,E3 -> action4_3\n" "Prepare to go to Pause State"
            return 
        if (ERROR == True):
            next_E = 6
            SM_TEXT_TO_DIAPLAY = "S4,E3 -> action4_3\n" "Prepare to go to error State"
            return         
        # print("S4,E3 -> action4_3")
        next_E = 0
        prev_S = 4
        SM_TEXT_TO_DIAPLAY = "S4,E3 -> action4_3\n"


    def action4_4(self):
        global SM_TEXT_TO_DIAPLAY
        global next_E, prev_S
        global PAUSE     
        global ERROR   
        if (PAUSE == True):
            next_E = 5
            SM_TEXT_TO_DIAPLAY = "S4,E4 -> action4_4\n" "Prepare to go to Pause State"
            return 
        if (ERROR == True):
            next_E = 6
            SM_TEXT_TO_DIAPLAY = "S4,E4 -> action4_4\n" "Prepare to go to error State"
            return                
        # print("S4,E4 -> action4_4")
        next_E = 0
        prev_S = 4
        SM_TEXT_TO_DIAPLAY ="S4,E4 -> action4_4\n"


    def action4_5(self):
        global SM_TEXT_TO_DIAPLAY
        global next_E
        global ERROR   
        if (ERROR == True):
            next_E = 6
            SM_TEXT_TO_DIAPLAY = "S4,E5 -> action4_5\n" "Prepare to go to error State"
            return          
        # print("S4,E5 -> action4_5")
        next_E = 0
        SM_TEXT_TO_DIAPLAY ="S4,E5 -> action4_5\n"


    def action4_6(self):
        global SM_TEXT_TO_DIAPLAY
        global next_E
        # print("S4,E6 -> action4_6")
        next_E = 0
        SM_TEXT_TO_DIAPLAY ="S4,E6 -> action4_6\n"


    #-------------- 
    def action5_0(self):
        global SM_TEXT_TO_DIAPLAY
        global next_E
        global PAUSE     
        global ERROR   
        if (PAUSE == True):
            next_E = 3
            SM_TEXT_TO_DIAPLAY = "S5,E0 -> action5_0\n" "Prepare to go to Pause State"
            return 
        if (ERROR == True):
            next_E = 4
            SM_TEXT_TO_DIAPLAY = "S5,E0 -> action5_0\n" "Prepare to go to error State"
            return    
                
        # experiment is complete
        next_E = 1
        SM_TEXT_TO_DIAPLAY ="S5,E0 -> action5_0\n" "\tSTATE 5: Experiment complete"


    def action5_1(self):
        global SM_TEXT_TO_DIAPLAY
        global next_E
        global PAUSE     
        global ERROR   
        if (PAUSE == True):
            next_E = 3
            SM_TEXT_TO_DIAPLAY = "S5,E1 -> action5_1\n" "Prepare to go to Pause State"
            return 
        if (ERROR == True):
            next_E = 4
            SM_TEXT_TO_DIAPLAY = "S5,E1 -> action5_1\n" "Prepare to go to error State"
            return 
                
        # print("S5,E1 -> action5_1")
        next_E = 2
        SM_TEXT_TO_DIAPLAY ="S5,E1 -> action5_1\n"
        

    def action5_2(self):
        global SM_TEXT_TO_DIAPLAY
        global next_E, terminate_SM
        global PAUSE     
        global ERROR   
        if (PAUSE == True):
            next_E = 3
            SM_TEXT_TO_DIAPLAY = "S5,E2 -> action5_2\n" "Prepare to go to Pause State"
            return 
        if (ERROR == True):
            next_E = 4
            SM_TEXT_TO_DIAPLAY = "S5,E2 -> action5_2\n" "Prepare to go to error State"
            return 
        
        next_E = 0
        terminate_SM = True
        SM_TEXT_TO_DIAPLAY ="S5,E2 -> action5_2 \n----> Terminate state machine"
        

    def action5_3(self):
        global SM_TEXT_TO_DIAPLAY
        global next_E, prev_S
        global ERROR   
        if (ERROR == True):
            next_E = 4
            SM_TEXT_TO_DIAPLAY = "S5,E1 -> action5_1\n" "Prepare to go to error State"
            return 
        
        next_E = 0
        prev_S = 5
        SM_TEXT_TO_DIAPLAY = "S5,E3 -> action5_3\n"


    def action5_4(self):
        global SM_TEXT_TO_DIAPLAY
        global next_E
        # print("S5,E4 -> action5_4")
        next_E = 0
        SM_TEXT_TO_DIAPLAY ="S5,E4 -> action5_4\n"


    #--------------
    def action6_0(self):
        global SM_TEXT_TO_DIAPLAY
        global next_E
        global PAUSE
        global prev_S

        if (PAUSE == True):
            next_E = 0
        else:
            next_E = prev_S
        SM_TEXT_TO_DIAPLAY ="S6,E0 -> action6_0\n"

    def action6_1(self):
        global SM_TEXT_TO_DIAPLAY
        global next_E
        # print("S6,E1 -> action6_1")
        next_E = 0
        SM_TEXT_TO_DIAPLAY ="S6,E1 -> action6_1"

    def action6_2(self):
        global SM_TEXT_TO_DIAPLAY
        global next_E
        # print("S6,E2 -> action6_2")
        next_E = 0
        SM_TEXT_TO_DIAPLAY ="S6,E2 -> action6_2\n"

    def action6_3(self):
        global SM_TEXT_TO_DIAPLAY
        global next_E, prev_S
        # print("S6,E3 -> action6_3")
        next_E = 0
        SM_TEXT_TO_DIAPLAY ="S6,E3 -> action6_3\n"

    def action6_4(self):
        global SM_TEXT_TO_DIAPLAY
        global next_E
        next_E = 0
        SM_TEXT_TO_DIAPLAY ="S6,E4 -> action6_4\n"

    def action6_5(self):
        global SM_TEXT_TO_DIAPLAY
        global next_E
        next_E = 0
        # print("S6,E5 -> action6_5")
        SM_TEXT_TO_DIAPLAY ="S6,E5 -> action6_5\n"


    #--------------
    def action7_0(self):
        global SM_TEXT_TO_DIAPLAY
        global next_E
        print("S7,E0 -> action7_0")
        next_E = 0
        SM_TEXT_TO_DIAPLAY ="S7,E0 -> action7_0\n"

    #--------------

    def execute(self):
        global S_cur 
        global Event 
        global next_E 
        global KILL_THREADS
        global TAKE_STEP
        global SM_TEXT_TO_DIAPLAY
        global RESET
        S_cur = Event = 0
        print('init S:{}  init E:{}'.format(S_cur, Event))

        while (terminate_SM == False):
            # time.sleep(DELAY_TIME) 
            time.sleep(.5)
            if (TAKE_STEP == True and KILL_THREADS == False and RESET==False):
                TAKE_STEP = False
                S_next = TT_EXPERIMENT[S_cur][Event]
                Next_State = int(S_next[0])    
                Next_action= S_next[1]
                S_cur = Next_State            
                eval(Next_action+'()')
                Event = next_E 
                
            if (KILL_THREADS == True):
                    break
            if (RESET == True):
                S_cur = Event = 0
                SM_TEXT_TO_DIAPLAY = "reset the SM"
                RESET = False
                break

        print('SM Terminated')
        self.b_run['state']=NORMAL
        self.b_step['state']=DISABLED

    #-------------------------------------------------------------
    #-------------- END OF ACTIONS -------------------------------
    #-------------------------------------------------------------



def is_float(element: any) -> bool:
    #If you expect None to be passed:
    if element is None: 
        return False
    try:
        float(element)
        return True
    except ValueError:
        return False


def main(): #run mianloop 
    
    root = Tk()
    # app = GUI.GUI(root)
    run_SM_GUI(root)

    root.mainloop()

if __name__ == '__main__':
    main()