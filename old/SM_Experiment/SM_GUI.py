# !/usr/bin/python3  
from tkinter import *  
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import time
import sys
import logging



logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
formatter = logging.Formatter('%(levelname)s:%(message)s')

file_handler = logging.FileHandler('error.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)



class SM_GUI():


      def __init__(self, root):

            self.set_fonts()
            self.set_main_window(root)
            self.setup_tabs(root)
            self.define_tab1()
            self.define_tab2()
            self.define_tab3()
            # root.iconbitmap("./Images/icon2.ico")



      def setup_tabs(self,root):
            #--------------------- DEFINE TABS ---------------------------------------
            self.tabControl = ttk.Notebook(root) 
            self.tab1 = Frame(self.tabControl) 
            self.tab2 = Frame(self.tabControl)
            self.tab3 = Frame(self.tabControl, bg=self.Color1)
            self.tabControl.add(self.tab1, text ='Experiment') 
            self.tabControl.add(self.tab2, text ='SM2') 
            self.tabControl.add(self.tab3, text ='SM3') 
            self.tabControl.pack(expand = 1, fill ="both") 
            #---------------------  PUMP TAB ----------------------------------------------------
            
            #------------- Draw Lines -------------------------------------------------
            # # Create a self.canvas2 widget
            self.canvas1=Canvas(self.tab1, width=1200, height=800,bg=self.Color1)
            self.canvas1.pack()

            s = ttk.Style()
            s.theme_create( "MyStyle", parent="alt", settings={
                  "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
                  "TNotebook.Tab": {"configure": {"padding": [70, 10],
                                                      "font" : ('URW Gothic L', '11', 'bold')},}})
            s.theme_use("MyStyle")


      def define_tab1(self):
            #---------------------------- PAUSE BUTTON ----------------------------------------
            self.b_pause = Button(self.tab1,text="Press to\nPAUSE", bg="#4287f5", 
                                 fg='black',font=self.Font4, height=2, width=10, 
                                 command=self.checkPauseButton)
            self.b_pause.pack()
            self.b_pause.place(x =160,y = 50)
            #---------------------------- ERROR BUTTON ----------------------------------------
            self.b_error = Button(self.tab1,text="Create\nERROR", bg="#4287f5", 
                                 fg='black',font=self.Font4, height=2, width=10, 
                                 command=self.checkErrorButton)
            self.b_error.pack()
            self.b_error.place(x =160,y = 150)
            #---------------------------- RESET BUTTON ----------------------------------------
            self.b_error = Button(self.tab1,text="Reset SM", bg="#dfeb07", 
                                 fg='black',font=self.Font4, height=2, width=10, 
                                 command=self.checkResetButton)
            self.b_error.pack()
            self.b_error.place(x =160,y = 350)
            #---------------------------- Z GANTRY POSITION BUTTON ----------------------------------------
            self.b_gantry = Button(self.tab1,text="Z Gantry Position\nHIGH", bg="#4287f5", 
                                 fg='black',font=self.Font4, height=2, width=17, 
                                 command=self.checkZGantryButton)
            self.b_gantry.pack()
            self.b_gantry.place(x =400,y = 50)
            #---------------------------- Pump in POSITION BUTTON ----------------------------------------
            self.b_pump = Button(self.tab1,text="Pump in Position\nFALSE", bg="#4287f5", 
                                 fg='black',font=self.Font4, height=2, width=17, 
                                 command=self.checkPumpInPosition)
            self.b_pump.pack()
            self.b_pump.place(x =400,y = 150)
            #---------------------------- Mixing signal OK BUTTON ----------------------------------------
            self.b_mix = Button(self.tab1,text="Mixing Signal Ready\n False", bg="#4287f5", 
                                 fg='black',font=self.Font4, height=2, width=17, 
                                 command=self.checkMixingButton)
            self.b_mix.pack()
            self.b_mix.place(x =400,y = 250)
            #---------------------------- qruilibrium reached BUTTON ----------------------------------------
            self.b_equi = Button(self.tab1,text="Equilibrium Reached\n False", bg="#4287f5", 
                                 fg='black',font=self.Font4, height=2, width=17, 
                                 command=self.checkEqulibriumButton)
            self.b_equi.pack()
            self.b_equi.place(x =400,y = 350)
            #---------------------------- Dose signal  BUTTON ----------------------------------------
            self.b_dose = Button(self.tab1,text="Dose Signal Recieved\n False", bg="#4287f5", 
                                 fg='black',font=self.Font4, height=2, width=17, 
                                 command=self.checkDoseRecievedButton)
            self.b_dose.pack()
            self.b_dose.place(x =400,y = 450)
            #---------------------------- Run SM  BUTTON ----------------------------------------
            self.b_run = Button(self.tab1,text="Run SM", bg="#07a81a", 
                                 fg='black',font=self.Font4, height=2, width=17, 
                                 command=self.checkRunSMButton)
            self.b_run.pack()
            self.b_run.place(x =800,y = 350)
            #---------------------------- Step throught SM  BUTTON ----------------------------------------
            self.b_step = Button(self.tab1,text="Step", bg="#07a81a", 
                                 fg='black',font=self.Font4, height=2, width=17, 
                                 command=self.checkStepSMButton)
            self.b_step.pack()
            self.b_step.place(x =800,y = 450)
            #---------------------------- EXIT BUTTON ----------------------------------------
            self.b_exit = Button(self.tab1,text="Exit\n Application", bg="#fc9d9d", 
                                 fg='black',font=self.Font4, height=2, width=14, 
                                 command=self.checkExitButton).place(x =900,y = 650)

            XX1 = 750
            Y1 = 50
            dY1 = 50
            XX2 = 150
            XX3 = 100
            Label(self.tab1, text = "Total Dose",font=self.Font5 , bg=self.Color1,
                  fg='black').place(x = XX1,y = Y1 + 1*dY1)  
            self.total_dose = Entry(self.tab1, width=5,font=self.Font5)
            self.total_dose.pack()
            self.total_dose.place(x = XX1 + XX2,y = Y1 + 1*dY1 ) 
            self.b_set_dose = Button(self.tab1,text="set", bg=self.Color2, fg=self.Color3, 
                                    command=self.check_Set_Dose_Button).place(x = XX1 + XX2+XX3,
                                                                        y = Y1 + 1*dY1 - 2)
            Label(self.tab1, text = "Delay Time (s)",font=self.Font5 , bg=self.Color1,
                  fg='black').place(x = XX1,y = Y1 + 2*dY1)  
            self.delay_time = Entry(self.tab1, width=5,font=self.Font5)
            self.delay_time.pack()
            self.delay_time.place(x = XX1 + XX2,y = Y1 + 2*dY1 ) 
            self.b_delay_time = Button(self.tab1,text="set", bg=self.Color2, fg=self.Color3, 
                                    command=self.check_Set_Delay_Time).place(x = XX1 + XX2+XX3,
                                                                        y = Y1 + 2*dY1 - 2)            
            Label(self.tab1, text = "Current Dose",font=self.Font5 , bg=self.Color1,
                  fg='black').place(x = XX1,y = Y1 + 3*dY1)  
            self.cur_dose = Label(self.tab1, text = '-----',font=self.Font5 )
            self.cur_dose.pack()
            self.cur_dose.place(x =XX1 + XX2 ,y = Y1 +3* dY1) 
            self.output = Text(self.tab1, height=5, width=50,bg='light yellow')
            self.output.pack()
            self.output.place(x = XX1,y = Y1 + 4*dY1)
            



      def define_tab2(self):
            # #---------------------  MOTORS TAB ---------------------------------------
            # # Create a canvas widget
            self.canvas2=Canvas(self.tab2, width=1200, height=800,bg=self.Color1 )
            self.canvas2.pack()
            # Add a few lines in self.canvas2 widget
            # self.canvas2.create_line(0,30,1200,30, fill='gray', width=1)
            # self.canvas2.create_line(300,30,300,800, fill='gray', width=1)
            # self.canvas2.create_line(600,30,600,800, fill='gray', width=1)
            # self.canvas2.create_line(900,30,900,800, fill='gray', width=1)
           

      def define_tab3(self):
            pass




      def set_main_window(self,root):
            # root.geometry("1200x800+50+50") 
            root.title("DEBUG / MANUAL MODE GUI") 
            root.resizable(False, False)
            # root.overrideredirect(True)
            window_height = 800
            window_width = 1200
            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            position_top = int(screen_height/2 -window_height/2)
            position_right = int(screen_width / 2 - window_width/2)
            # logger.debug('H:', screen_height, 'x W:', screen_width )
            logger.debug('H:{}x W{}:'.format( screen_height, screen_width ))
            root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
            def disable_event():
                  pass
            root.protocol("WM_DELETE_WINDOW", disable_event)
            # root.resizable(width=FALSE, height=FALSE)   


      def set_fonts(self):
            self.Font1 = 'sans 13' # fixed label text font
            self.Font2 = 'sans 11 italic' #variable label text font
            self.Font3 = 'sans 15'  # titles label text font 
            self.Font4 = 'sans 20'  # large title labels text font
            self.Font5 = 'Arial 16'  #valves title label text font
            self.Font6 = "Verdana 10 " # combo box text font
            self.Font7 = "Arial 14" # larger text for terminate/start/stop buttons

            self.Color1 = '#D9D9D9'  #label background color (gray)
            self.Color2 = "#c5ccd1"  #Button bg color (gray)
            self.Color3 = "red"   # buttons text color

            self.Title_large = 'red'
            self.Title_mid = 'blue'


      def checkPauseButton(self):
            logger.debug("child:Pause button pressed ...")

      def checkErrorButton(self):
            logger.debug("child: Error button pressed ...")

      def checkResetButton(self):
            logger.debug("child: Reset button pressed ...")

      def checkMixingButton(self):
            logger.debug("child: Mixing button pressed ...")
            
      def checkEqulibriumButton(self):
            logger.debug("child: Equilibrium  button pressed ...")

      def checkDoseRecievedButton(self):
            logger.debug("child: Dose receibed  button pressed ...")

      def checkZGantryButton(self):
            logger.debug("child: Z gantry  button is pressed ...")

      def checkPumpInPosition(self):
            logger.debug("child: pump in position button is pressed ...")

      def check_Set_Delay_Time(self):
            logger.debug("child: set delay time ...")

      def check_Set_Dose_Button(self):
            logger.debug("child: set dose button pressed ...")
            
      def checkRunSMButton(self):
            logger.debug("child: Run SM ...")

      def checkStepSMButton(self):
            logger.debug("child: Step through SM ...")

      def checkExitButton(self):
            logger.debug("exit button pressed ...")
            # self.timer.cancel()
            # self.root.destroy()
            sys.exit(0)


# if __name__ == '__main__':
#     # main()
#     root = Tk()
#     app = SM_GUI(root)
#     root.mainloop()
