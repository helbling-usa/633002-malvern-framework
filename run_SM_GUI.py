import  SM_GUI
from    tkinter import * 
from    tkinter import filedialog as fd
import  tkinter.messagebox 
from    config.motor_3axes import motor_3axes as Motors
import  config.Pump as P
import  time
import  u6
import  threading
import  config.MeerstetterTEC as TEC
import  json
import  logging
import  sys
import  numpy as np
import  threading
import  general.General_vars as GENERAL
from    general.recipe import RECIPE
import  SM.Startup
import  HW
#--------------  GLOBAL VARIABLES -----------------------------------------

# GENERAL = General_vars()

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
        self.PortAssignment()
        self.Init_Pumps_Valves()
        self.Init__motors_all_axes() 
        self.InitLabjack()
        self.InitTecController()
        self.InitTimer()
        




    def InitTimer(self):
        # #------ Starts timer
        logger.info('starting internal timer')
        self.timer = threading.Timer(1.0, self.timerCallback_1)
        self.timer.start()
        logger.info('\t\tInternal timer started')


    def timerCallback_1(self):  
        # global SM_TEXT_TO_DIAPLAY
        # logger.debug('timer is running')
        self.read_BubbleSensors()
        self.updateGUI_LEDs()


        # self.output.delete("1.0","end")
        # self.output.insert(END,SM_TEXT_TO_DIAPLAY)
        # self.cur_dose.config(text = str(dose_number))
        #-------- repeat the timer ----------------------------------------------
        self.timer = threading.Timer(.50, self.timerCallback_1)
        self.timer.start()
        



    def InitLabjack(self):
        # # initialize labjack
        logger.info("Initializing Labjack.....")
        HW.labjack = u6.U6()
        HW.labjack.writeRegister(50590, 15)     
        # print("--->", HW.labjack.getAIN(0))   
        # logger.info('\t\tlabjack initialized')


    def read_BubbleSensors(self):
        # read bubble sensor and update the LEDs
        HW.BS1 = (HW.labjack.getAIN(0))
        HW.BS2 = (HW.labjack.getAIN(1))
        HW.BS3 = (HW.labjack.getAIN(2))
        HW.BS4 = (HW.labjack.getAIN(3))
        HW.BS5 = (HW.labjack.getAIN(4))
        HW.BS6 = (HW.labjack.getAIN(5))
        HW.BS7 = (HW.labjack.getAIN(6))
        HW.BS8 = (HW.labjack.getAIN(7))
        HW.BS9 = (HW.labjack.getAIN(8))
        HW.BS10 = (HW.labjack.getAIN(9))
        HW.BS11 = (HW.labjack.getAIN(10))
        HW.BS12 = (HW.labjack.getAIN(11))
        HW.BS13 = (HW.labjack.getAIN(12))
        HW.BS14 = (HW.labjack.getAIN(13))


    def updateGUI_LEDs(self):
        COL7 = 740
        Y1  = 50
        dY1 = 50
        dd=10
        dist = 80
        if (HW.pump1_titrant_active_led == False):
            self.led_on_1.place_forget()
            self.led_off_1.pack()
            self.led_off_1.place(x = COL7+dd,y = Y1 + 1*dY1)
        else:
            self.led_off_1.place_forget()
            self.led_on_1.pack()
            self.led_on_1.place(x =COL7+dd,y = Y1 + 1*dY1)
        
        if (HW.pump1_titrant_homed_led == False):
            self.led_on_2.place_forget()
            self.led_off_2.pack()
            self.led_off_2.place(x = COL7+dist+dd,y = Y1 + 1*dY1)
        else:
            self.led_off_2.place_forget()
            self.led_on_2.pack()
            self.led_on_2.place(x =COL7+dist+dd,y = Y1 + 1*dY1)

        if (HW.pump2_sample_active_led == False):
            self.led_on_3.place_forget()
            self.led_off_3.pack()
            self.led_off_3.place(x = COL7+dd,y = Y1 + 2*dY1)
        else:
            self.led_off_3.place_forget()
            self.led_on_3.pack()
            self.led_on_3.place(x =COL7+dd,y = Y1 + 2*dY1)
        
        if (HW.pump2_sample_homed_led == False):
            self.led_on_4.place_forget()
            self.led_off_4.pack()
            self.led_off_4.place(x = COL7+dist+dd,y = Y1 + 2*dY1)
        else:
            self.led_off_4.place_forget()
            self.led_on_4.pack()
            self.led_on_4.place(x =COL7+dist+dd,y = Y1 + 2*dY1)

        if (HW.horizontal_gantry_active_led == False):
            self.led_on_5.place_forget()
            self.led_off_5.pack()
            self.led_off_5.place(x = COL7+dd,y = Y1 + 3*dY1)
        else:
            self.led_off_5.place_forget()
            self.led_on_5.pack()
            self.led_on_5.place(x =COL7+dd,y = Y1 + 3*dY1)
        
        if (HW.horizontal_gantry_homed_led == False):
            self.led_on_6.place_forget()
            self.led_off_6.pack()
            self.led_off_6.place(x = COL7+dist+dd,y = Y1 + 3*dY1)
        else:
            self.led_off_6.place_forget()
            self.led_on_6.pack()
            self.led_on_6.place(x =COL7+dist+dd,y = Y1 + 3*dY1)


        if (HW.vertical_gantry_active_led == False):
            self.led_on_7.place_forget()
            self.led_off_7.pack()
            self.led_off_7.place(x = COL7+dd,y = Y1 + 4*dY1)
        else:
            self.led_off_7.place_forget()
            self.led_on_7.pack()
            self.led_on_7.place(x =COL7+dd,y = Y1 + 4*dY1)
        
        if (HW.vertical_gantry_homed_led == False):
            self.led_on_8.place_forget()
            self.led_off_8.pack()
            self.led_off_8.place(x = COL7+dist+dd,y = Y1 + 4*dY1)
        else:
            self.led_off_8.place_forget()
            self.led_on_8.pack()
            self.led_on_8.place(x =COL7+dist+dd,y = Y1 + 4*dY1)

        if (HW.mixing_motor_active_led == False):
            self.led_on_9.place_forget()
            self.led_off_9.pack()
            self.led_off_9.place(x = COL7+dd,y = Y1 + 5*dY1)
        else:
            self.led_off_9.place_forget()
            self.led_on_9.pack()
            self.led_on_9.place(x =COL7+dd,y = Y1 + 5*dY1)
        
        if (HW.mixing_motor_homed_led == False):
            self.led_on_10.place_forget()
            self.led_off_10.pack()
            self.led_off_10.place(x = COL7+dist+dd,y = Y1 + 5*dY1)
        else:
            self.led_off_10.place_forget()
            self.led_on_10.pack()
            self.led_on_10.place(x =COL7+dist+dd,y = Y1 + 5*dY1)


        # Update The GUI with current value of bubble sensors
        COL9 = 950
        COL11 = 1030
        Y1  = 50
        dY1 = 40
        dd=40
        # print('---',HW.BS11)
        if (HW.BS1 < HW.BS_THRESHOLD):
            self.led_on_11.place_forget()
            self.led_off_11.pack()
            self.led_off_11.place(x = COL9+dd,y = Y1 + 1*dY1)
        else:
            self.led_off_11.place_forget()
            self.led_on_11.pack()            
            self.led_on_11.place(x =COL9+dd,y = Y1 + 1*dY1)

        if (HW.BS2 < HW.BS_THRESHOLD):
            self.led_on_12.place_forget()
            self.led_off_12.pack()
            self.led_off_12.place(x = COL9+dd,y = Y1 + 2*dY1)            
        else:
            self.led_off_12.place_forget()
            self.led_on_12.pack()            
            self.led_on_12.place(x =COL9+dd,y = Y1 + 2*dY1)

        if (HW.BS3 < HW.BS_THRESHOLD):
            self.led_on_13.place_forget()
            self.led_off_13.pack()
            self.led_off_13.place(x = COL9+dd,y = Y1 + 3*dY1)            
        else:
            self.led_off_13.place_forget()
            self.led_on_13.pack()            
            self.led_on_13.place(x =COL9+dd,y = Y1 + 3*dY1)

        if (HW.BS4 < HW.BS_THRESHOLD):
            self.led_on_14.place_forget()
            self.led_off_14.pack()
            self.led_off_14.place(x = COL9+dd,y = Y1 + 4*dY1)            
        else:
            self.led_off_14.place_forget()
            self.led_on_14.pack()            
            self.led_on_14.place(x =COL9+dd,y = Y1 + 4*dY1)

        if (HW.BS5 < HW.BS_THRESHOLD):
            self.led_on_15.place_forget()
            self.led_off_15.pack()
            self.led_off_15.place(x = COL9+dd,y = Y1 + 5*dY1)            
        else:
            self.led_off_15.place_forget()
            self.led_on_15.pack()            
            self.led_on_15.place(x =COL9+dd,y = Y1 + 5*dY1)

        if (HW.BS6 < HW.BS_THRESHOLD):
            self.led_on_16.place_forget()
            self.led_off_16.pack()
            self.led_off_16.place(x = COL9+dd,y = Y1 + 6*dY1)            
        else:
            self.led_off_16.place_forget()
            self.led_on_16.pack()            
            self.led_on_16.place(x =COL9+dd,y = Y1 + 6*dY1)

        if (HW.BS7 < HW.BS_THRESHOLD):
            self.led_on_17.place_forget()
            self.led_off_17.pack()
            self.led_off_17.place(x = COL9+dd,y = Y1 + 7*dY1)            
        else:
            self.led_off_17.place_forget()
            self.led_on_17.pack()            
            self.led_on_17.place(x =COL9+dd,y = Y1 + 7*dY1)                                                

        if (HW.BS8 < HW.BS_THRESHOLD):
            self.led_on_18.place_forget()
            self.led_off_18.pack()
            self.led_off_18.place(x = COL11+dd,y = Y1 + 1*dY1)
        else:
            self.led_off_18.place_forget()
            self.led_on_18.pack()            
            self.led_on_18.place(x =COL11+dd,y = Y1 + 1*dY1)

        if (HW.BS9 < HW.BS_THRESHOLD):
            self.led_on_19.place_forget()
            self.led_off_19.pack()
            self.led_off_19.place(x = COL11+dd,y = Y1 + 2*dY1)            
        else:
            self.led_off_19.place_forget()
            self.led_on_19.pack()            
            self.led_on_19.place(x =COL11+dd,y = Y1 + 2*dY1)

        if (HW.BS10 < HW.BS_THRESHOLD):
            self.led_on_20.place_forget()
            self.led_off_20.pack()
            self.led_off_20.place(x = COL11+dd,y = Y1 + 3*dY1)            
        else:
            self.led_off_20.place_forget()
            self.led_on_20.pack()            
            self.led_on_20.place(x =COL11+dd,y = Y1 + 3*dY1)

        if (HW.BS11 < HW.BS_THRESHOLD):
            self.led_on_21.place_forget()
            self.led_off_21.pack()
            self.led_off_21.place(x = COL11+dd,y = Y1 + 4*dY1)            
        else:
            self.led_off_21.place_forget()
            self.led_on_21.pack()            
            self.led_on_21.place(x =COL11+dd,y = Y1 + 4*dY1)

        if (HW.BS12 < HW.BS_THRESHOLD):
            self.led_on_22.place_forget()
            self.led_off_22.pack()
            self.led_off_22.place(x = COL11+dd,y = Y1 + 5*dY1)            
        else:
            self.led_off_22.place_forget()
            self.led_on_22.pack()            
            self.led_on_22.place(x =COL11+dd,y = Y1 + 5*dY1)

        if (HW.BS13 < HW.BS_THRESHOLD):
            self.led_on_23.place_forget()
            self.led_off_23.pack()
            self.led_off_23.place(x = COL11+dd,y = Y1 + 6*dY1)            
        else:
            self.led_off_23.place_forget()
            self.led_on_23.pack()            
            self.led_on_23.place(x =COL11+dd,y = Y1 + 6*dY1)

        if (HW.BS14 < HW.BS_THRESHOLD):
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
                initialdir='.',
                filetypes=filetypes)        
        self.decode_recipe(recipe_filepath)
        


    def PortAssignment(self):

        logger.info("Assigning Ports .....")
        # #---- extract port numbers for config.json
        with open('./config/config.json') as json_file:
            ports = json.load(json_file)
        #assign port numbers to the hardware
        # logger.info('ports:', ports)
        HW.TEC_PORT = ports['TEC']
        HW.PUMP1_PORT = ports['PUMP']
        HW.TECHNOSOFT_PORT = ports['TECHNOSOFT']
        HW.GANTRY_VER_AXIS_ID = int(ports['GANTRY_VER_AXIS_ID'])
        HW.GANTRY_HOR_AXIS_ID = int(ports['GANTRY_HOR_AXIS_ID'])
        HW.MIXER_AXIS_ID = int(ports['MIXER_AXIS_ID'])        
        print('==================================')

        print("tec:",HW.TEC_PORT )
        print("pump1:",HW.PUMP1_PORT )
        print("technosoft:",HW.TECHNOSOFT_PORT)
        print("gantry v:",HW.GANTRY_VER_AXIS_ID)
        print("gantry H:",HW.GANTRY_HOR_AXIS_ID)
        print("mixer",HW.MIXER_AXIS_ID )




    def Init_Pumps_Valves(self):        
        # # #------ init. Pump 1
        # logger.info("Initializing Pumps/Valves.....")
        com_port = HW.PUMP1_PORT
        HW.pump1 = P.Pump(com_port)
        
        # HW.pump1.pump_Zinit(HW.TIRRANT_PUMP_ADDRESS)
        # logger.info("\t\tPump1 initialized")
        # time.sleep(3)
        
        # HW.pump1.pump_Zinit(HW.SAMPLE_PUMP_ADDRESS)
        # logger.info("\t\tPump2 initialized")
        # time.sleep(3)

        # HW.pump1.set_speed(HW.TIRRANT_PUMP_ADDRESS,HW.DEFAULT_PUMP_SPEEED)
        # logger.info("\t\tPump1 speed is set to {}".format(HW.DEFAULT_PUMP_SPEEED))
        
        # HW.pump1.set_speed(HW.SAMPLE_PUMP_ADDRESS,HW.DEFAULT_PUMP_SPEEED)
        # logger.info("\t\tPump2 speed is set to {}".format(HW.DEFAULT_PUMP_SPEEED))


        # logger.info("\t\tSetting valves to default positions")
        # HW.pump1.set_valve(HW.TIRRANT_PUMP_ADDRESS, 'E')
        # HW.pump1.set_valve(HW.TITRANT_LOOP_ADDRESS, 'E')
        # HW.pump1.set_multiwayvalve(HW.TITRANT_PIPETTE_ADDRESS,3)
        # HW.pump1.set_multiwayvalve(HW.TITRANT_CLEANING_ADDRESS,1)        
        # HW.pump1.set_valve(HW.SAMPLE_PUMP_ADDRESS, 'E')
        # HW.pump1.set_valve(HW.SAMPLE_LOOP_ADDRESS, 'E')
        # HW.pump1.set_multiwayvalve(HW.TITRANT_PORT_ADDRESS,3)
        # HW.pump1.set_multiwayvalve(HW.DEGASSER_ADDRESS,1)        
        # HW.pump1.set_multiwayvalve(HW.SAMPLE_CLEANING_ADDRESS,1)        


    def Init__motors_all_axes(self):
        # logger.info("Initializing motors .....")        
        com_port = HW.TECHNOSOFT_PORT.encode()        
        primary_axis =  b"Mixer"
        AXIS_ID_01 = HW.MIXER_AXIS_ID
        AXIS_ID_02 = HW.GANTRY_HOR_AXIS_ID
        AXIS_ID_03 = HW.GANTRY_VER_AXIS_ID
        HW.motors = Motors(com_port, AXIS_ID_01, AXIS_ID_02, AXIS_ID_03 ,primary_axis)   
 



        
    def InitTecController(self):
        # ------create object of TEC5 
        # logger.info("Initialzing TEC Temperature Controller---------------------")
        HW.tec = TEC.MeerstetterTEC(HW.TEC_PORT)
        # logger.info(self.mc.get_data())
        # logger.info("\t\tTEC controller initialized ")



    def decode_recipe(self, recipe_filepath):
        global GENERAL

        with open(recipe_filepath , 'r') as f:
            recipe_json = json.load(f)        
        
        #Sanity check: to see if all statemachines are listed in the json file, if not exit
        input_SMs = list(recipe_json.keys())
        input_SMs.sort()        
        all_SMs = ['Startup', 'PumpInit_Reload', 'Degas', 'Load_Prime','Func_NewAirSlugs']
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
        # SM_enabled_dic = {}
        for key in recipe_json.keys():
            # print("==", key)
            RECIPE[key] = recipe_json[key]
            if (recipe_json[key]['enable'] == True):
                # SM_enabled_dic[key] = True
                info_str = info_str +key+": Enabled"+ "\n"
            else:
                # SM_enabled_dic[key] = False
                info_str = info_str +key+": Disabled"+ "\n"

        #Display SMs enable status in the status box
        self.t_status.delete("1.0", END)
        self.t_status.insert(END, info_str)

        # print("===============")
        # print(RECIPE)
        # print("===============")
        # print("global vars:", GENERAL.SM_TEXT_TO_DIAPLAY)






    def b_start_recipe(self):
        logger.debug("child: start button pressed")
        print("Running:{} Statemachine".format( SM.Startup.name()))
        # self.execute(SM.Startup)
        self.t1 = threading.Thread(target=self.execute, args=(SM.Startup,))
        self.t1.start()

    def b_next(self):
        logger.debug("child: next button pressed")



    def reset_SM_vars(self):
        global GENERAL
        GENERAL.next_E = 0 
        GENERAL.cur_S = 0
        GENERAL.prev_S = 0
        GENERAL.terminate_SM = False
        GENERAL.doescount = 5
        GENERAL.dose_number = 0
        GENERAL.SM_TEXT_TO_DIAPLAY = "--"
        GENERAL.PAUSE = False
        GENERAL.ERROR = False 


    def execute(self, statemachine):
        global GENERAL
        self.reset_SM_vars()
        # print('cur state:', GENERAL.cur_S, 'next event:', GENERAL.next_E)    
        Event = 0
        # i=0
        while (GENERAL.terminate_SM == False):
            time.sleep(.5)   
            print("------------------")
            print("---cur_s:",GENERAL.cur_S, " E:",Event)
            S_next = statemachine.TT[GENERAL.cur_S][Event]
            print("---",S_next)
            Next_State = int(S_next[0])    
            Next_action= statemachine.name() + '.'+ S_next[1]
            GENERAL.cur_S = Next_State  
            print("next action:", Next_action, '  cur_S:', Next_State)          
            eval('SM.'+Next_action+'()')
            print(GENERAL.SM_TEXT_TO_DIAPLAY)
            self.t_status.delete("1.0", END)
            self.t_status.insert(END, GENERAL.SM_TEXT_TO_DIAPLAY)
            Event = GENERAL.next_E 
            self.t_cur_state.delete("1.0",END)
            self.t_cur_state.insert(END, statemachine.state_name[Next_State])            
            self.t_cur_proc.delete("1.0",END)
            self.t_cur_proc.insert(END, statemachine.name())

        print('SM Terminated')
        
        
    def checkExitButton(self):
        # global KILL_THREADS
        logger.debug("exit button pressed ...")
        # KILL_THREADS = True
        self.timer.cancel()
        # self.root.destroy()
        sys.exit(0)






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