import  general.SM_GUI as SM_GUI
from    tkinter import * 
from    tkinter import filedialog as fd
import  tkinter.messagebox 
from    Lib.motor_3axes import motor_3axes as Motors
import  Lib.Pump as P
import  time
import  u6
import  threading
import  Lib.MeerstetterTEC as TEC
import  json
import  logging
import  sys
import  numpy as np
import  general.global_vars as GV
from    general.recipe import RECIPE
import  SM.Constants
import  SM.Startup
import  SM.PumpInit_Reload
import  SM.Degas
import  SM.Load_Prime
import  SM.GantrytoB
import  SM.Experiment
import  SM.GantrytoA
import  SM.GantryReturn
import  SM.DegasClean
import  SM.SampleLineClean
import  SM.TitrantLineClean
import  SM.RecovClean
import  SM.Func_DiluteDetergent
import  SM.Func_NewAirSlugs
import  hardware.config as HW
import  grpc
import  unary.unary_pb2_grpc as pb2_grpc
import  unary.unary_pb2 as pb2


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


class run_SM_GUI(SM_GUI.SM_GUI):
    
    def __init__(self,root):
        super().__init__( root)
        self.root = root
        logger.info("Initializing hardware -------------------------------------")        
        logger.info("------------------------------------------------------------------")
        logger.info('System started successfully.')
        logger.info("Please use the GUI to enter a commamnd ...")
        # self.t1 = threading.Thread(target=self.execute, name='SM_experiment')
        logger.info("Initializing global variables")
        # settings.init()
        # self.PortAssignment()
        self.init_pumps_valves()
        self.init__motors_all_axes() 
        self.init_labjack()
        self.init_tec_controller()
        self.init_timer()
        self.b_nextbutton["state"] = DISABLED
        self.b_start["state"] = DISABLED
        GV.SM_list = [SM.Startup, SM.PumpInit_Reload, SM.Degas, SM.Load_Prime, SM.GantrytoB, SM.Experiment, 
                      SM.GantrytoA,SM.GantryReturn, SM.DegasClean, SM.SampleLineClean, SM.TitrantLineClean, SM.RecovClean,
                        SM.Func_DiluteDetergent, SM.Func_NewAirSlugs]
        GV.SM_list_str = ["Startup", "PumpInit_Reload", "Degas", "Load_Prime", "GantrytoB", "Experiment", 
                          "GantrytoA", "GantryReturn","DegasClean", "SampleLineClean", "TitrantLineClean", "RecovClean", 
                          "Func_DiluteDetergent", "Func_NewAirSlugs"]
        GV.grPC_Client = UnaryClient()  #start grPC client service


    def init_pumps_valves(self):        
        # logger.info("Initializing Pumps/Valves.....")
        com_port = HW.PUMP1_PORT
        GV.pump1 = P.Pump(com_port)


    def init__motors_all_axes(self):
        logger.info("Initializing motors .....")        
        com_port = HW.TECHNOSOFT_PORT.encode()        
        logger.info('com port = {}'.format( HW.TECHNOSOFT_PORT))
        primary_axis =  b"Mixer"
        AXIS_ID_01 = HW.MIXER_AXIS_ID
        AXIS_ID_02 = HW.GANTRY_HOR_AXIS_ID
        AXIS_ID_03 = HW.GANTRY_VER_AXIS_ID
        GV.motors = Motors(com_port, AXIS_ID_01, AXIS_ID_02, AXIS_ID_03 ,primary_axis)   
 
        
    def init_labjack(self):
        # # initialize labjack
        logger.info("\t\tInitializing Labjack.....")
        GV.labjack = u6.U6()
        GV.labjack.writeRegister(50590, 15)     
        logger.info('\t\tlabjack initialized')


    def init_tec_controller(self):
        # ------create object of TEC5 
        # logger.info("Initialzing TEC Temperature Controller---------------------")
        GV.tec = TEC.MeerstetterTEC(HW.TEC_PORT)
        logger.info("\t\tTEC controller initialized ")


    def init_timer(self):
        # #------ Starts timer
        logger.info('\t\tstarting internal timer')
        self.timer = threading.Timer(1.0, self.timerCallback_1)
        self.timer.start()
        logger.info('\t\tInternal timer started')


    def timerCallback_1(self):
        self.update_status_window()        
        self.check_next_button()
        self.update_experiment()
        self.update_valves()   
        self.read_bubble_sensors()
        self.update_gui_leds()     
        #-------- repeat the timer ----------------------------------------------
        self.timer = threading.Timer(.5, self.timerCallback_1)
        self.timer.start()


    def update_status_window(self):
        self.t_status.delete("1.0", END)
        self.t_status.insert(END, GV.SM_TEXT_TO_DIAPLAY)
    


    def check_next_button(self):
        #take care of NEXT button
        if  (GV.PAUSE == True):
            self.b_pause.config(text=' Resume All ')

        if (GV.activate_NEXT_button == True):
            self.b_nextbutton["state"] = NORMAL
        else:
            self.b_nextbutton["state"] = DISABLED
        

    def update_experiment(self):
        self.text_tec_target.delete("1.0", END)
        self.text_tec_target.insert(END, GV.TEC_TARGET)
        self.text_tec_actual.delete("1.0", END)
        self.text_tec_actual.insert(END, GV.TEC_ACTUAL)
        self.text_dose_vol.delete("1.0", END)
        self.text_dose_vol.insert(END, GV.DOSE_VOLUME)
        self.text_dose_completed.delete("1.0", END)
        self.text_dose_completed.insert(END, GV.DOSE_COMPLETED)
        self.text_total_doses.delete("1.0", END)
        self.text_total_doses.insert(END, GV.TOTAL_DOSES)
        self.text_mixing_speed.delete("1.0", END)
        self.text_mixing_speed.insert(END, GV.MIXING_SPEED)
        COL1 = 50
        Y3  = 410+8
        if (GV.TEC_IS_ON == False):
            self.led_on_30.place_forget()
            self.led_off_30.pack()
            self.led_off_30.place(x = COL1,y = Y3)
        else:
            self.led_off_30.place_forget()
            self.led_on_30.pack()
            self.led_on_30.place(x =COL1,y = Y3)


    def update_valves(self):
        self.text_pump_valve1.delete("1.0", END)
        self.text_pump_valve1.insert(END, GV.VALVE_1)
        self.text_loop_valve3.delete("1.0", END)
        self.text_loop_valve3.insert(END, GV.VALVE_3)
        self.text_pipette_valve5.delete("1.0", END)
        self.text_pipette_valve5.insert(END, GV.VALVE_5)
        self.text_cleaning_valve9.delete("1.0", END)
        self.text_cleaning_valve9.insert(END, GV.VALVE_9)
        self.text_pump_valve2.delete("1.0", END)
        self.text_pump_valve2.insert(END, GV.VALVE_2)
        self.text_loop_valve4.delete("1.0", END)
        self.text_loop_valve4.insert(END, GV.VALVE_4)
        self.text_titrant_valve6.delete("1.0", END)
        self.text_titrant_valve6.insert(END, GV.VALVE_6)
        self.text_degasser_valve7.delete("1.0", END)
        self.text_degasser_valve7.insert(END, GV.VALVE_7)
        self.text_cleaning_valve8.delete("1.0", END)
        self.text_cleaning_valve8.insert(END, GV.VALVE_8)


    def read_bubble_sensors(self):
        # read bubble sensor and update the LEDs
        GV.V_BS1 = (GV.labjack.getAIN(HW.BS1_IO_PORT))
        GV.V_BS2 = (GV.labjack.getAIN(HW.BS2_IO_PORT))
        GV.V_BS3 = (GV.labjack.getAIN(HW.BS3_IO_PORT))
        GV.V_BS4 = (GV.labjack.getAIN(HW.BS4_IO_PORT))
        GV.V_BS5 = (GV.labjack.getAIN(HW.BS5_IO_PORT))
        GV.V_BS6 = (GV.labjack.getAIN(HW.BS6_IO_PORT))
        GV.V_BS7 = (GV.labjack.getAIN(HW.BS7_IO_PORT))
        GV.V_BS8 = (GV.labjack.getAIN(HW.BS8_IO_PORT))
        GV.V_BS9 = (GV.labjack.getAIN(HW.BS9_IO_PORT))
        GV.V_BS10 = (GV.labjack.getAIN(HW.BS10_IO_PORT))
        GV.V_BS11 = (GV.labjack.getAIN(HW.BS11_IO_PORT))
        GV.V_BS12 = (GV.labjack.getAIN(HW.BS12_IO_PORT))
        GV.V_BS13 = (GV.labjack.getAIN(HW.BS13_IO_PORT))
        GV.V_BS14 = (GV.labjack.getAIN(HW.BS14_IO_PORT))


    def update_gui_leds(self):
        COL7 = 830
        Y1  = 50
        dY1 = 50
        dd=10
        dist = 80
        if (GV.pump1_titrant_active_led == False):
            self.led_on_1.place_forget()
            self.led_off_1.pack()
            self.led_off_1.place(x = COL7+dd,y = Y1 + 1*dY1)
        else:
            self.led_off_1.place_forget()
            self.led_on_1.pack()
            self.led_on_1.place(x =COL7+dd,y = Y1 + 1*dY1)
        
        if (GV.pump1_titrant_homed_led == False):
            self.led_on_2.place_forget()
            self.led_off_2.pack()
            self.led_off_2.place(x = COL7+dist+dd,y = Y1 + 1*dY1)
        else:
            self.led_off_2.place_forget()
            self.led_on_2.pack()
            self.led_on_2.place(x =COL7+dist+dd,y = Y1 + 1*dY1)

        if (GV.pump2_sample_active_led == False):
            self.led_on_3.place_forget()
            self.led_off_3.pack()
            self.led_off_3.place(x = COL7+dd,y = Y1 + 2*dY1)
        else:
            self.led_off_3.place_forget()
            self.led_on_3.pack()
            self.led_on_3.place(x =COL7+dd,y = Y1 + 2*dY1)
        
        if (GV.pump2_sample_homed_led == False):
            self.led_on_4.place_forget()
            self.led_off_4.pack()
            self.led_off_4.place(x = COL7+dist+dd,y = Y1 + 2*dY1)
        else:
            self.led_off_4.place_forget()
            self.led_on_4.pack()
            self.led_on_4.place(x =COL7+dist+dd,y = Y1 + 2*dY1)

        if (GV.horizontal_gantry_active_led == False):
            self.led_on_5.place_forget()
            self.led_off_5.pack()
            self.led_off_5.place(x = COL7+dd,y = Y1 + 3*dY1)
        else:
            self.led_off_5.place_forget()
            self.led_on_5.pack()
            self.led_on_5.place(x =COL7+dd,y = Y1 + 3*dY1)
        
        if (GV.horizontal_gantry_homed_led == False):
            self.led_on_6.place_forget()
            self.led_off_6.pack()
            self.led_off_6.place(x = COL7+dist+dd,y = Y1 + 3*dY1)
        else:
            self.led_off_6.place_forget()
            self.led_on_6.pack()
            self.led_on_6.place(x =COL7+dist+dd,y = Y1 + 3*dY1)

        if (GV.vertical_gantry_active_led == False):
            self.led_on_7.place_forget()
            self.led_off_7.pack()
            self.led_off_7.place(x = COL7+dd,y = Y1 + 4*dY1)
        else:
            self.led_off_7.place_forget()
            self.led_on_7.pack()
            self.led_on_7.place(x =COL7+dd,y = Y1 + 4*dY1)
        
        if (GV.vertical_gantry_homed_led == False):
            self.led_on_8.place_forget()
            self.led_off_8.pack()
            self.led_off_8.place(x = COL7+dist+dd,y = Y1 + 4*dY1)
        else:
            self.led_off_8.place_forget()
            self.led_on_8.pack()
            self.led_on_8.place(x =COL7+dist+dd,y = Y1 + 4*dY1)

        if (GV.mixing_motor_active_led == False):
            self.led_on_9.place_forget()
            self.led_off_9.pack()
            self.led_off_9.place(x = COL7+dd,y = Y1 + 5*dY1)
        else:
            self.led_off_9.place_forget()
            self.led_on_9.pack()
            self.led_on_9.place(x =COL7+dd,y = Y1 + 5*dY1)
        
        # Update The GUI with current value of bubble sensors
        COL9 = 1020
        COL11 = 1100
        Y1  = 50
        dY1 = 40
        dd=40
        # logger.info('---',GV.V_BS11)
        if (GV.V_BS1 < HW.BS_THRESHOLD):
            self.led_on_11.place_forget()
            self.led_off_11.pack()
            self.led_off_11.place(x = COL9+dd,y = Y1 + 1*dY1)
        else:
            self.led_off_11.place_forget()
            self.led_on_11.pack()            
            self.led_on_11.place(x =COL9+dd,y = Y1 + 1*dY1)

        if (GV.V_BS2 < HW.BS_THRESHOLD):
            self.led_on_12.place_forget()
            self.led_off_12.pack()
            self.led_off_12.place(x = COL9+dd,y = Y1 + 2*dY1)            
        else:
            self.led_off_12.place_forget()
            self.led_on_12.pack()            
            self.led_on_12.place(x =COL9+dd,y = Y1 + 2*dY1)

        if (GV.V_BS3 < HW.BS_THRESHOLD):
            self.led_on_13.place_forget()
            self.led_off_13.pack()
            self.led_off_13.place(x = COL9+dd,y = Y1 + 3*dY1)            
        else:
            self.led_off_13.place_forget()
            self.led_on_13.pack()            
            self.led_on_13.place(x =COL9+dd,y = Y1 + 3*dY1)

        if (GV.V_BS4 < HW.BS_THRESHOLD):
            self.led_on_14.place_forget()
            self.led_off_14.pack()
            self.led_off_14.place(x = COL9+dd,y = Y1 + 4*dY1)            
        else:
            self.led_off_14.place_forget()
            self.led_on_14.pack()            
            self.led_on_14.place(x =COL9+dd,y = Y1 + 4*dY1)

        if (GV.V_BS5 < HW.BS_THRESHOLD):
            self.led_on_15.place_forget()
            self.led_off_15.pack()
            self.led_off_15.place(x = COL9+dd,y = Y1 + 5*dY1)            
        else:
            self.led_off_15.place_forget()
            self.led_on_15.pack()            
            self.led_on_15.place(x =COL9+dd,y = Y1 + 5*dY1)

        if (GV.V_BS6 < HW.BS_THRESHOLD):
            self.led_on_16.place_forget()
            self.led_off_16.pack()
            self.led_off_16.place(x = COL9+dd,y = Y1 + 6*dY1)            
        else:
            self.led_off_16.place_forget()
            self.led_on_16.pack()            
            self.led_on_16.place(x =COL9+dd,y = Y1 + 6*dY1)

        if (GV.V_BS7 < HW.BS_THRESHOLD):
            self.led_on_17.place_forget()
            self.led_off_17.pack()
            self.led_off_17.place(x = COL9+dd,y = Y1 + 7*dY1)            
        else:
            self.led_off_17.place_forget()
            self.led_on_17.pack()            
            self.led_on_17.place(x =COL9+dd,y = Y1 + 7*dY1)                                                

        if (GV.V_BS8 < HW.BS_THRESHOLD):
            self.led_on_18.place_forget()
            self.led_off_18.pack()
            self.led_off_18.place(x = COL11+dd,y = Y1 + 1*dY1)
        else:
            self.led_off_18.place_forget()
            self.led_on_18.pack()            
            self.led_on_18.place(x =COL11+dd,y = Y1 + 1*dY1)

        if (GV.V_BS9 < HW.BS_THRESHOLD):
            self.led_on_19.place_forget()
            self.led_off_19.pack()
            self.led_off_19.place(x = COL11+dd,y = Y1 + 2*dY1)            
        else:
            self.led_off_19.place_forget()
            self.led_on_19.pack()            
            self.led_on_19.place(x =COL11+dd,y = Y1 + 2*dY1)

        if (GV.V_BS10 < HW.BS_THRESHOLD):
            self.led_on_20.place_forget()
            self.led_off_20.pack()
            self.led_off_20.place(x = COL11+dd,y = Y1 + 3*dY1)            
        else:
            self.led_off_20.place_forget()
            self.led_on_20.pack()            
            self.led_on_20.place(x =COL11+dd,y = Y1 + 3*dY1)

        if (GV.V_BS11 < HW.BS_THRESHOLD):
            self.led_on_21.place_forget()
            self.led_off_21.pack()
            self.led_off_21.place(x = COL11+dd,y = Y1 + 4*dY1)            
        else:
            self.led_off_21.place_forget()
            self.led_on_21.pack()            
            self.led_on_21.place(x =COL11+dd,y = Y1 + 4*dY1)

        if (GV.V_BS12 < HW.BS_THRESHOLD):
            self.led_on_22.place_forget()
            self.led_off_22.pack()
            self.led_off_22.place(x = COL11+dd,y = Y1 + 5*dY1)            
        else:
            self.led_off_22.place_forget()
            self.led_on_22.pack()            
            self.led_on_22.place(x =COL11+dd,y = Y1 + 5*dY1)

        if (GV.V_BS13 < HW.BS_THRESHOLD):
            self.led_on_23.place_forget()
            self.led_off_23.pack()
            self.led_off_23.place(x = COL11+dd,y = Y1 + 6*dY1)            
        else:
            self.led_off_23.place_forget()
            self.led_on_23.pack()            
            self.led_on_23.place(x =COL11+dd,y = Y1 + 6*dY1)

        if (GV.V_BS14 < HW.BS_THRESHOLD):
            self.led_on_24.place_forget()
            self.led_off_24.pack()
            self.led_off_24.place(x = COL11+dd,y = Y1 + 7*dY1)            
        else:
            self.led_off_24.place_forget()
            self.led_on_24.pack()            
            self.led_on_24.place(x =COL11+dd,y = Y1 + 7*dY1)     


    def b_select_recipe_file(self):            
        filetypes = (
                ('json', '*.json'),
                ('All files', '*.*')
        )
        recipe_filepath = fd.askopenfilename(
                title='Open a file',
                initialdir='./recipes',
                filetypes=filetypes)        
        self.decode_recipe(recipe_filepath)        
        self.b_nextbutton["state"] = DISABLED
        self.b_start["state"] = NORMAL

        
    def decode_recipe(self, recipe_filepath):
        # global GV
        with open(recipe_filepath , 'r') as f:
            recipe_json = json.load(f)                
        #Sanity check: to see if all statemachines are listed in the json file, if not exit
        input_SMs = list(recipe_json.keys())
        input_SMs.sort()        
        all_SMs = GV.SM_list_str.copy()
        all_SMs.sort()   
        if (all_SMs == input_SMs):
            logger.info('json file validated')
        else:
            logger.error('json file not valid: some statemachines are missing ...')
            tkinter.messagebox.showerror("ERROR","Recipe File Not Valid")
            return
        self.text_fname.config(state=NORMAL)
        self.text_fname.delete("1.0", END)
        recipe_file_name = recipe_filepath.split('/')
        self.text_fname.insert(END, recipe_file_name[-1])
        self.text_fname.config(state=DISABLED)
        #copy recipe.json into recipe dictionary global variable
        info_str = ""
        GV.SM_enabled_dic = {}
        for key in recipe_json.keys():
            # logger.info("==", key)
            RECIPE[key] = recipe_json[key]
            if (recipe_json[key]['enable'] == True):
                GV.SM_enabled_dic[key] = True
                str_new = "{:.<20s}{:.>20s}\n".format(key,"Enabled")
                info_str = info_str + str_new
            else:
                GV.SM_enabled_dic[key] = False                
                str_new = "{:.<20s}{:.>20s}\n".format(key,"Disabled")
                info_str = info_str + str_new
        #Display SMs enable status in the status box
        self.t_status.delete("1.0", END)
        GV.SM_TEXT_TO_DIAPLAY = info_str
        self.t_status.insert(END, GV.SM_TEXT_TO_DIAPLAY )


    def b_start_recipe(self):
        logger.debug("Start button pressed")
        for item,item_str in zip(GV.SM_list, GV.SM_list_str):                        
            # logger.info("item:", item_str, "  value:", GV.SM_enabled_dic[item_str] )
            logger.info("item: {}  value: {}".format( item_str, GV.SM_enabled_dic[item_str] ))
            if (GV.SM_enabled_dic[item_str] == True):
                # logger.info(item_str, '  is about to run')
                logger.info(f'{item_str}  is about to run')
                str = "SM."+item_str 
                # logger.info("module:", str, '  ==== ', sys.modules[str]
                logger.info("Running:{} Statemachine".format( sys.modules[str].name()))
                self.t1 = threading.Thread(target=self.execute, args=(sys.modules[str],))
                self.t1.start()
                GV.SM_enabled_dic[item_str] = False
                break
            logger.info("------------------next state machine -----------------")        
        logger.info('Recipe terminated')
        self.b_start["state"] =  DISABLED  #enable START button on the GUI
        self.b_start.config(text=' Start ')


    def b_next(self):
        logger.debug("child: next button pressed")
        GV.NEXT = True


    def reset_SM_vars(self):
        GV.next_E = 0 
        GV.cur_S = 0
        GV.prev_S = 0
        GV.terminate_SM = False
        # GV.doescount = 5
        # GV.dose_number = 0
        GV.SM_TEXT_TO_DIAPLAY = "--"
        GV.PAUSE = False
        GV.ERROR = False 


    def execute(self, statemachine):
        self.b_start["state"] =  DISABLED  #disable START button on the GUI
        self.reset_SM_vars()
        Event = 0
        # i=0
        while (GV.terminate_SM == False):
            time.sleep(.5)   
            # logger.info("------------------")
            # logger.info("---cur_s:",GV.cur_S, " E:",Event)
            S_next = statemachine.TT[GV.cur_S][Event]
            # logger.info("---",S_next)
            Next_State = int(S_next[0])    
            Next_action= statemachine.name() + '.'+ S_next[1]
            GV.cur_S = Next_State  
            logger.info("    ---> running: {}      next state: {}".format( Next_action, Next_State)          )
            eval('SM.'+Next_action+'()')
            message = format_string(GV.SM_TEXT_TO_DIAPLAY)
            logger.info(message)
            # logger.info(GV.SM_TEXT_TO_DIAPLAY)
            # self.t_status.delete("1.0", END)
            # self.t_status.insert(END, GV.SM_TEXT_TO_DIAPLAY)
            Event = GV.next_E 
            self.t_cur_state.delete("1.0",END)
            self.t_cur_state.insert(END, statemachine.state_name[Next_State])            
            self.t_cur_proc.delete("1.0",END)
            self.t_cur_proc.insert(END, statemachine.name())
        logger.info('SM Terminated')
        self.b_start["state"] =  NORMAL  #enable START button on the GUI
        self.b_start.config(text=' Continue ')
        
        
    def checkExitButton(self):
        # global KILL_THREADS
        logger.debug("exit button pressed ...")
        logger.debug("killing timer thread")
        # KILL_THREADS = True
        self.timer.cancel()
        logger.debug("destroying GUI")
        self.root.destroy()
        logger.debug("exiting the code")
        sys.exit(0)
        

    def checkPauseButton(self):
        # logger.debug("child: Pause button pressed ...")
        if (GV.PAUSE == False):
            GV.PAUSE = True
            self.b_pause.config(text=' Resume All ')
        else:
            GV.PAUSE = False
            self.b_pause.config(text='   Pause All  ')


def is_float(element: any) -> bool:
    #If you expect None to be passed:
    if element is None: 
        return False
    try:
        float(element)
        return True
    except ValueError:
        return False

"""add 2 tabs to each line of the input string"""
def format_string(str_in):
    str_list = str_in.split('\n')
    str_out =""
    for row in str_list:
        str_out +="\t\t"+row+"\n"
    return str_out


class UnaryClient(object):
    """
    Client for gRPC functionality
    """
    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051
        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))
        # bind the client and the server
        self.stub = pb2_grpc.UnaryStub(self.channel)

    def get_url(self, message):
        """
        Client function to call the rpc for GetServerResponse
        """
        message = pb2.Message(message=message)
        # logger.info(f'{message}')
        return self.stub.GetServerResponse(message)
    


def main(): #run mianloop 
    
    root = Tk()
    # app = GUI.GUI(root)
    run_SM_GUI(root)

    root.mainloop()




if __name__ == '__main__':    
    main()
