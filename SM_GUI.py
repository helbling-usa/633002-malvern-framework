# !/usr/bin/python3  
from tkinter import *  
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog as fd
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
            self.root = root
            self.set_fonts()
            self.set_main_window()
            self.set_buttons()
            self.set_lights()
            # self.setup_tabs(self.root)
            # self.define_tab1()



      def set_main_window(self):
            # self.root.geometry("1200x800+50+50") 
            self.root.title("DEBUG / MANUAL MODE GUI") 
            self.root.resizable(False, False)
            # self.root.overrideredirect(True)
            window_height = 800
            window_width = 1200
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            position_top = int(screen_height/2 -window_height/2)
            position_right = int(screen_width / 2 - window_width/2)
            logger.debug('H:{}x W{}:'.format( screen_height, screen_width ))
            self.root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
            def disable_event():
                  pass
            self.root.protocol("WM_DELETE_WINDOW", disable_event)
            self.canvas1=Canvas(self.root, width=1200, height=800,bg=self.Color1)
            self.canvas1.pack()
            s = ttk.Style()
            s.theme_create( "MyStyle", parent="alt", settings={
                  "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
                  "TNotebook.Tab": {"configure": {"padding": [70, 10],
                                                      "font" : ('URW Gothic L', '11', 'bold')},}})
            s.theme_use("MyStyle")
            #draw the lines on the convas
            self.canvas1.create_line(40,80,530,80, fill='gray', width=2)      #horizontal 
            self.canvas1.create_line(40,270,530,270, fill='gray', width=2)    #horizontal 
            self.canvas1.create_line(40,80,40,270, fill='gray', width=2)      #vertical
            self.canvas1.create_line(530,80,530,270, fill='gray', width=2)    #vertical



      def set_buttons(self):
            self.b_exit = Button(self.root,text="Exit\n Application", bg="#fc9d9d", 
                                 fg='black',font=self.Font4, height=2, width=14, 
                                 command=self.checkExitButton).place(x =900,y = 650)

            COL1 = 50
            Y1  = 50
            dY1 = 50
            COL2 = 140
            COL3 = 290
            COL4 = 325
            COL5 = 375
            Label(self.root, text = "Recipe File",font=self.Font1 , bg=self.Color1,
                  fg='black').place(x = COL1,y = Y1 + 1*dY1)  

            self.text_fname = Text(self.root, height=1, width=18,font=self.Font2 )
            self.text_fname.pack()
            self.text_fname.place(x=COL2, y=Y1+1*dY1+2)
            
            self.b_set_dose = Button(self.root,text="▼", font=self.Font2,
                                     command=self.b_select_recipe_file).place(x = COL3,y = Y1 + 1*dY1 - 2)
            self.b_set_dose = Button(self.root,text="Start", font=self.Font2, bg="#558ff2", 
                                     command=self.b_start_recipe).place(x = COL4, y = Y1 + 1*dY1 - 2)
            self.b_set_dose = Button(self.root,text="Next", font=self.Font2, bg="#558ff2", 
                                     command=self.b_next).place(x = COL5, y = Y1 + 1*dY1 - 2)


            Label(self.root, text = "Current Procedure:",font=self.Font1 , bg=self.Color1,
                  fg='black').place(x = COL1,y = Y1 + 2*dY1)  

            self.t_cur_proc = Text(self.root, height=1, width=25,font=self.Font2 ,bg="#f5f7bc",)
            self.t_cur_proc.pack()
            self.t_cur_proc.place(x=COL1+5, y=Y1+2*dY1+30)

            Label(self.root, text = "Current State:",font=self.Font1 , bg=self.Color1,
                  fg='black').place(x = COL1,y = Y1 + 3*dY1+10)  

            self.t_cur_state = Text(self.root, height=1, width=25,font=self.Font2 ,bg="#f5f7bc",)
            self.t_cur_state.pack()
            self.t_cur_state.place(x=COL1+5, y=Y1+3*dY1+40)

            Label(self.root, text = "Status:",font=self.Font2 , bg=self.Color1,
                  fg='black').place(x = COL4,y = Y1 + 2*dY1-10)  

            self.t_status = Text(self.root, height=6, width=30,font=self.Font2 ,bg="#f5f7bc",)
            self.t_status.pack()
            self.t_status.place(x=COL3-10, y=Y1+2*dY1+10)



      def set_lights(self):
            image1 = Image.open('./Images/led-green-off.png')
            image1 = image1.resize((24, 24))
            icon_off = ImageTk.PhotoImage(image1)
            image1 = Image.open('./Images/led-green-on.png')
            image1 = image1.resize((24, 24))
            icon_on = ImageTk.PhotoImage(image1)

            COL6 = 550
            COL7 = 740
            Y1  = 50
            dY1 = 50
            Label(self.root, text = "Avtive   Homed",font=self.Font5 , bg=self.Color1,
                  fg='black').place(x = COL7,y = Y1 + 0*dY1)  
            Label(self.root, text = "   Pump 1 Titrant:",font=self.Font5 , bg=self.Color1,
                  fg='black').place(x = COL6,y = Y1 + 1*dY1)  
            Label(self.root, text = "    Pump 2 Sample:",font=self.Font5 , bg=self.Color1,
                  fg='black').place(x = COL6,y = Y1 + 2*dY1)
            Label(self.root, text = "Horizontal Gantry:",font=self.Font5 , bg=self.Color1,
                  fg='black').place(x = COL6,y = Y1 + 3*dY1)
            Label(self.root, text = "  Vertical Gantry:",font=self.Font5 , bg=self.Color1,
                  fg='black').place(x = COL6,y = Y1 + 4*dY1)
            Label(self.root, text = "     Mixing Motor:",font=self.Font5 , bg=self.Color1,
                  fg='black').place(x = COL6,y = Y1 + 5*dY1)
            
            dd=10
            dist = 80
            self.led_off_1 = Label(self.root, image=icon_off)
            self.led_off_1.image = icon_off
            self.led_off_1.place(x = COL7+dd,y = Y1 + 1*dY1)

            self.led_on_1  = Label(self.root, image=icon_on)
            self.led_on_1.image = icon_on
            self.led_on_1.place(x =COL7+dd,y = Y1 + 1*dY1)

            self.led_off_2 = Label(self.root, image=icon_off)
            self.led_off_2.image = icon_off
            self.led_off_2.place(x = COL7+dist+dd,y = Y1 + 1*dY1)
            self.led_on_2  = Label(self.root, image=icon_on)
            self.led_on_2 .image = icon_on
            self.led_on_2.place(x =COL7+dist+dd,y = Y1 + 1*dY1)

            self.led_off_3 = Label(self.root, image=icon_off)
            self.led_off_3.image = icon_off
            self.led_off_3.place(x = COL7+dd,y = Y1 + 2*dY1)
            self.led_on_3  = Label(self.root, image=icon_on)
            self.led_on_3.image = icon_on
            self.led_on_3.place(x =COL7+dd,y = Y1 + 2*dY1)

            self.led_off_4 = Label(self.root, image=icon_off)
            self.led_off_4.image = icon_off
            self.led_off_4.place(x = COL7+dd+dist,y = Y1 + 2*dY1)

            self.led_on_4  = Label(self.root, image=icon_on)
            self.led_on_4.image = icon_on
            self.led_on_4.place(x =COL7+dist+dd,y = Y1 + 2*dY1)

            self.led_off_5 = Label(self.root, image=icon_off)
            self.led_off_5.image = icon_off
            self.led_off_5.place(x = COL7+dd,y = Y1 + 3*dY1)
            self.led_on_5  = Label(self.root, image=icon_on)
            self.led_on_5.image = icon_on
            self.led_on_5.place(x =COL7+dd,y = Y1 + 3*dY1)

            self.led_off_6 = Label(self.root, image=icon_off)
            self.led_off_6.image = icon_off
            self.led_off_6.place(x = COL7+dd+dist,y = Y1 + 3*dY1)
            self.led_on_6  = Label(self.root, image=icon_on)
            self.led_on_6.image = icon_on
            self.led_on_6.place(x =COL7+dist+dd,y = Y1 + 3*dY1)

            self.led_off_7 = Label(self.root, image=icon_off)
            self.led_off_7.image = icon_off
            self.led_off_7.place(x = COL7+dd,y = Y1 + 4*dY1)
            self.led_on_7  = Label(self.root, image=icon_on)
            self.led_on_7.image = icon_on
            self.led_on_7.place(x =COL7+dd,y = Y1 + 4*dY1)

            # dd = 50
            self.led_off_8 = Label(self.root, image=icon_off)
            self.led_off_8.image = icon_off
            self.led_off_8.place(x = COL7+dd+dist,y = Y1 + 4*dY1)
            self.led_on_8  = Label(self.root, image=icon_on)
            self.led_on_8.image = icon_on
            self.led_on_8.place(x =COL7+dist+dd,y = Y1 + 4*dY1)

            self.led_off_9 = Label(self.root, image=icon_off)
            self.led_off_9.image = icon_off
            self.led_off_9.place(x = COL7+dd,y = Y1 + 5*dY1)
            self.led_on_9  = Label(self.root, image=icon_on)
            self.led_on_9.image = icon_on
            self.led_on_9.place(x =COL7+dd,y = Y1 + 5*dY1)

            self.led_off_10 = Label(self.root, image=icon_off)
            self.led_off_10.image = icon_off
            self.led_off_10.place(x = COL7+dd+dist,y = Y1 + 5*dY1)
            self.led_on_10  = Label(self.root, image=icon_on)
            self.led_on_10.image = icon_on
            self.led_on_10.place(x =COL7+dist+dd,y = Y1 + 5*dY1)

            COL8 = 946
            COL9 = 950
            COL10 = 1025
            COL11 = 1030
            Y1  = 50
            dY1 = 40
            dd=40
            Label(self.root, text = "Bubble Sensors",font=self.Font5 , bg=self.Color1,
                  fg='black').place(x = COL9,y = Y1 + 0*dY1)                  
            Label(self.root, text = "BS1:",font=self.Font1 , bg=self.Color1,
                  fg='black').place(x = COL8,y = Y1 + 1*dY1)
            Label(self.root, text = "BS2:",font=self.Font1 , bg=self.Color1,
                  fg='black').place(x = COL8,y = Y1 + 2*dY1)
            Label(self.root, text = "BS3:",font=self.Font1 , bg=self.Color1,
                  fg='black').place(x = COL8,y = Y1 + 3*dY1)
            Label(self.root, text = "BS4:",font=self.Font1 , bg=self.Color1,
                  fg='black').place(x = COL8,y = Y1 + 4*dY1)
            Label(self.root, text = "BS5:",font=self.Font1 , bg=self.Color1,
                  fg='black').place(x = COL8,y = Y1 + 5*dY1)
            Label(self.root, text = "BS6:",font=self.Font1 , bg=self.Color1,
                  fg='black').place(x = COL8,y = Y1 + 6*dY1)
            Label(self.root, text = "BS7:",font=self.Font1 , bg=self.Color1,
                  fg='black').place(x = COL8,y = Y1 + 7*dY1)
            
            Label(self.root, text = "BS8:",font=self.Font1 , bg=self.Color1,
                  fg='black').place(x = COL10,y = Y1 + 1*dY1)
            Label(self.root, text = "BS8:",font=self.Font1 , bg=self.Color1,
                  fg='black').place(x = COL10,y = Y1 + 2*dY1)
            Label(self.root, text = "BS9:",font=self.Font1 , bg=self.Color1,
                  fg='black').place(x = COL10,y = Y1 + 3*dY1)
            Label(self.root, text = "BS10:",font=self.Font1 , bg=self.Color1,
                  fg='black').place(x = COL10,y = Y1 + 4*dY1)
            Label(self.root, text = "BS11:",font=self.Font1 , bg=self.Color1,
                  fg='black').place(x = COL10,y = Y1 + 5*dY1)
            Label(self.root, text = "BS12:",font=self.Font1 , bg=self.Color1,
                  fg='black').place(x = COL10,y = Y1 + 6*dY1)
            Label(self.root, text = "BS13:",font=self.Font1 , bg=self.Color1,
                  fg='black').place(x = COL10,y = Y1 + 7*dY1)

            self.led_off_11 = Label(self.root, image=icon_off)
            self.led_off_11.image = icon_off
            self.led_off_11.place(x = COL9+dd,y = Y1 + 1*dY1)            
            self.led_on_11  = Label(self.root, image=icon_on)
            self.led_on_11.image = icon_on
            self.led_on_11.place(x =COL9+dd,y = Y1 + 1*dY1)

            self.led_off_12 = Label(self.root, image=icon_off)
            self.led_off_12.image = icon_off
            self.led_off_12.place(x = COL9+dd,y = Y1 + 2*dY1)            
            self.led_on_12  = Label(self.root, image=icon_on)
            self.led_on_12.image = icon_on
            self.led_on_12.place(x =COL9+dd,y = Y1 + 2*dY1)

            self.led_off_13= Label(self.root, image=icon_off)
            self.led_off_13.image = icon_off
            self.led_off_13.place(x = COL9+dd,y = Y1 + 3*dY1)            
            self.led_on_13  = Label(self.root, image=icon_on)
            self.led_on_13.image = icon_on
            self.led_on_13.place(x =COL9+dd,y = Y1 + 3*dY1)

            self.led_off_14 = Label(self.root, image=icon_off)
            self.led_off_14.image = icon_off
            self.led_off_14.place(x = COL9+dd,y = Y1 + 4*dY1)            
            self.led_on_14  = Label(self.root, image=icon_on)
            self.led_on_14.image = icon_on
            self.led_on_14.place(x =COL9+dd,y = Y1 + 4*dY1)

            self.led_off_15 = Label(self.root, image=icon_off)
            self.led_off_15.image = icon_off
            self.led_off_15.place(x = COL9+dd,y = Y1 + 5*dY1)            
            self.led_on_15  = Label(self.root, image=icon_on)
            self.led_on_15.image = icon_on
            self.led_on_15.place(x =COL9+dd,y = Y1 + 5*dY1)

            self.led_off_16 = Label(self.root, image=icon_off)
            self.led_off_16.image = icon_off
            self.led_off_16.place(x = COL9+dd,y = Y1 + 6*dY1)            
            self.led_on_16  = Label(self.root, image=icon_on)
            self.led_on_16.image = icon_on
            self.led_on_16.place(x =COL9+dd,y = Y1 + 6*dY1)

            self.led_off_17 = Label(self.root, image=icon_off)
            self.led_off_17.image = icon_off
            self.led_off_17.place(x = COL9+dd,y = Y1 + 7*dY1)            
            self.led_on_17  = Label(self.root, image=icon_on)
            self.led_on_17.image = icon_on
            self.led_on_17.place(x =COL9+dd,y = Y1 + 7*dY1)

            self.led_off_18 = Label(self.root, image=icon_off)
            self.led_off_18.image = icon_off
            self.led_off_18.place(x = COL11+dd,y = Y1 + 1*dY1)            
            self.led_on_18  = Label(self.root, image=icon_on)
            self.led_on_18.image = icon_on
            self.led_on_18.place(x =COL11+dd,y = Y1 + 1*dY1)

            self.led_off_19 = Label(self.root, image=icon_off)
            self.led_off_19.image = icon_off
            self.led_off_19.place(x = COL11+dd,y = Y1 + 2*dY1)            
            self.led_on_19  = Label(self.root, image=icon_on)
            self.led_on_19.image = icon_on
            self.led_on_19.place(x =COL11+dd,y = Y1 + 2*dY1)

            self.led_off_20 = Label(self.root, image=icon_off)
            self.led_off_20.image = icon_off
            self.led_off_20.place(x = COL11+dd,y = Y1 + 3*dY1)            
            self.led_on_20  = Label(self.root, image=icon_on)
            self.led_on_20.image = icon_on
            self.led_on_20.place(x =COL11+dd,y = Y1 + 3*dY1)

            self.led_off_21 = Label(self.root, image=icon_off)
            self.led_off_21.image = icon_off
            self.led_off_21.place(x = COL11+dd,y = Y1 + 4*dY1)            
            self.led_on_21  = Label(self.root, image=icon_on)
            self.led_on_21.image = icon_on
            self.led_on_21.place(x =COL11+dd,y = Y1 + 4*dY1)

            self.led_off_22 = Label(self.root, image=icon_off)
            self.led_off_22.image = icon_off
            self.led_off_22.place(x = COL11+dd,y = Y1 + 5*dY1)            
            self.led_on_22  = Label(self.root, image=icon_on)
            self.led_on_22.image = icon_on
            self.led_on_22.place(x =COL11+dd,y = Y1 + 5*dY1)

            self.led_off_23 = Label(self.root, image=icon_off)
            self.led_off_23.image = icon_off
            self.led_off_23.place(x = COL11+dd,y = Y1 + 6*dY1)            
            self.led_on_23  = Label(self.root, image=icon_on)
            self.led_on_23.image = icon_on
            self.led_on_23.place(x =COL11+dd,y = Y1 + 6*dY1)

            self.led_off_24 = Label(self.root, image=icon_off)
            self.led_off_24.image = icon_off
            self.led_off_24.place(x = COL11+dd,y = Y1 + 7*dY1)            
            self.led_on_24  = Label(self.root, image=icon_on)
            self.led_on_24.image = icon_on
            self.led_on_24.place(x =COL11+dd,y = Y1 + 7*dY1)

      def set_fonts(self):
            #----- Fonts ---------------------------------------
            self.Font1 = 'sans 13' # fixed label text font
            self.Font2 = 'sans 11 italic' #variable label text font
            self.Font3 = 'sans 15'  # titles label text font 
            self.Font4 = 'sans 20'  # large title labels text font
            self.Font5 = 'Arial 16'  #valves title label text font
            self.Font6 = "Verdana 10 " # combo box text font
            self.Font7 = "Arial 14" # larger text for terminate/start/stop buttons
            #----- Colors ---------------------------------------
            self.Color1 = '#D9D9D9'  #label background color (gray)
            self.Color2 = "#c5ccd1"  #Button bg color (gray)
            self.Color3 = "red"   # buttons text color




      def b_start_recipe(self):
            logger.debug("parent: start button pressed")
      
      def b_next(self):
            logger.debug("parent: next button pressed")

      def b_select_recipe_file(self):            
            logger.debug("parent: open button pressed")

      def checkExitButton(self):
            logger.debug("parent: exit button pressed ...")
            # sys.exit(0)

