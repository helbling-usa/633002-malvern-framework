import  numpy as np
import  general.global_vars as GV
import  HW
import  time
from    general.recipe import RECIPE

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


#---------------  ACTIONS  --------------
def action0_0():
    str1 = "S0,E0 -> action0_0" "  -V1 to LinetoPump\n" "  -V3 to TitrantLine\n" "  -V5 to TitrantPort\n" "  -V2 to LinetoGas\n"
    str1 = str1 + "  -V4 to SampleLine\n"  "  -V7 to SamplePort"
    GV.SM_TEXT_TO_DIAPLAY = str1
    GV.current_Aspiration_count = 0
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
    
    GV.pump1.set_valve(HW.TIRRANT_PUMP_ADDRESS, 'I')
    time.sleep(.5)
    GV.pump1.set_valve(HW.TITRANT_LOOP_ADDRESS, 'I')
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.TITRANT_CLEANING_ADDRESS,1)        
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.TITRANT_PIPETTE_ADDRESS,3)
    time.sleep(.5)

    GV.pump1.set_valve(HW.SAMPLE_PUMP_ADDRESS, 'I')
    time.sleep(.5)
    GV.pump1.set_multiwayvalve(HW.TITRANT_PORT_ADDRESS,2)
    time.sleep(.5)


    GV.pump1.set_speed(HW.TIRRANT_PUMP_ADDRESS,RECIPE["PumpInit_Reload"]["pump_speed"])
    time.sleep(1)
    GV.pump1.set_speed(HW.SAMPLE_PUMP_ADDRESS,RECIPE["PumpInit_Reload"]["pump_speed"])
    time.sleep(1)


    str1 = "S0,E0 -> action0_0" "  -V1 to LinetoPump\n" "  -V3 to TitrantLine\n" "  -V5 to TitrantPort\n" "  -V2 to LinetoGas\n"
    str1 = str1 + "  -V4 to SampleLine\n"  "  -V7 to SamplePort"
    GV.SM_TEXT_TO_DIAPLAY = "S1,E0 -> action1_0\n" + str1
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
    GV.SM_TEXT_TO_DIAPLAY = "S1,E1 -> action1_1\n" + str1
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
    GV.SM_TEXT_TO_DIAPLAY ="S1,E2 -> action1_2\n" "  go to S2/E0 state"
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
    if (GV.PAUSE == True):
        GV.next_E = 4        
        GV.SM_TEXT_TO_DIAPLAY = "S2,E0 -> action2_1\n" "  going to S2/E4"
        return 
    if (GV.ERROR == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S2,E0 -> action2_1\n" "  going to S2/E5"
        return 
    
    temp = RECIPE['Degas']['degas_temp']
    print("===================>",temp)
    GV.tec.set_temp(float(temp))

    tec_dic =  GV.tec.get_data()
    obj_temp = round(tec_dic['object temperature'][0], 1)
    target_temp = round(tec_dic['target object temperature'][0], 1)
    TEC_cur_status = tec_dic['loop status'][0]        
    print('--->obj temp:{} , target temp:{}    status:{}'.format(obj_temp,  target_temp,TEC_cur_status))  
    
    # GV.tec.mc.enable()
    # GV.tec.mc.disable()

    total_asipiration_number = RECIPE["Degas"]["total_asipiration_number"]    
    str0 = "\ncurrent # Aspiration:{}\nTotal Aspirations:{}".format(GV.current_Aspiration_count, total_asipiration_number)
    str1 = "  set TEC to temp\n" "  going to S2/E1"
    GV.SM_TEXT_TO_DIAPLAY ="S2,E0 -> action2_0\n" +str1 + str0
    GV.next_E = 1

def action2_1():
    timeout = False
    if (GV.PAUSE == True):
        GV.next_E = 4        
        GV.SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1\n" "  going to S2/E4"
        return 
    if (GV.ERROR == True  or  timeout==True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S2,E1 -> action2_1\n" "  going to S2/E5"
        return 
    
    total_asipiration_number = RECIPE["Degas"]["total_asipiration_number"]    
    str0 = "\ncurrent # Aspiration:{}\nTotal Aspirations:{}".format(GV.current_Aspiration_count, total_asipiration_number)    
    str1 = "  waiting for heat time"
    GV.SM_TEXT_TO_DIAPLAY ="S2,E1 -> action2_1\n" + str1 + str0
    GV.next_E = 2
    
def action2_2():
    timeout = False
    # passed_time = 10 # measure the  heating time
    if (GV.PAUSE == True):
        GV.next_E = 4        
        GV.SM_TEXT_TO_DIAPLAY = "S2,E2 -> action2_2\n" "  going to S2/E4"
        return 
    if (GV.ERROR == True  or  timeout==True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S2,E2 -> action2_2\n" "  going to S2/E5"
        return
        
    heat_time = RECIPE["Degas"]["heat_time"]
    t_end = time.time() + heat_time
    counter = 0
    while time.time() < t_end:
        time.sleep(1)
        counter += 1
        print("\t time:", counter, " / ", heat_time)


    # if (passed_time < GV.heat_time):
    #     GV.SM_TEXT_TO_DIAPLAY ="S2,E2 -> action2_2" "  witing to reach. heat time .."
    #     GV.next_E = 2
    # else:
    GV.SM_TEXT_TO_DIAPLAY ="S2,E2 -> action2_2\n" "  Heat time reached\n"  "  go to S3/E0"
    GV.next_E = 3

def action2_3():
    if (GV.PAUSE == True):
        GV.next_E = 4        
        GV.SM_TEXT_TO_DIAPLAY = "S2,E3 -> action2_3\n" "  going to S2/E4"
        return 
    if (GV.ERROR == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S2,E3 -> action2_3\n" "  going to S2/E5"
        return
    
    total_asipiration_number = RECIPE["Degas"]["total_asipiration_number"]    
    str0 = "\ncurrent # Aspiration:{}\nTotal Aspirations:{}".format(GV.current_Aspiration_count, total_asipiration_number)    
    str1 = str1 = "pump 1 pickup Var.:\n  Tit. Vol. +Asp. Overshoot\n""pump 2 pickup Var.:\n  Sample Vol. +Asp. Overshoot"
    GV.SM_TEXT_TO_DIAPLAY ="S2,E3 -> action2_3\n" + str1 + str0
    GV.next_E = 0


def action2_4():
    if (GV.ERROR == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S2,E4 -> action2_4\n" "  going to S2/E5"
        return         
    
    GV.SM_TEXT_TO_DIAPLAY ="S2,E4 -> action2_4"
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
    pump_speed = RECIPE["Degas"]["pump_speed"]    
    AspirationVolume_Overshoot = RECIPE["Degas"]["AspirationVolume_Overshoot"]

    pump_address1 = HW.TIRRANT_PUMP_ADDRESS
    pump_address2 = HW.SAMPLE_PUMP_ADDRESS

    starting_pos1 = GV.pump1.get_plunger_position(pump_address1)
    time.sleep(.5)
    GV.pump1.set_speed(pump_address1, pump_speed)
    time.sleep(.5)
    next_pos1 =  starting_pos1 + AspirationVolume_Overshoot
    GV.pump1.set_pos_absolute(pump_address1, next_pos1)
    time.sleep(1)

    starting_pos2 = GV.pump1.get_plunger_position(pump_address2)
    time.sleep(.5)
    GV.pump1.set_speed(pump_address2, pump_speed)
    time.sleep(1)
    next_pos2 =  starting_pos2 + AspirationVolume_Overshoot
    GV.pump1.set_pos_absolute(pump_address2, next_pos2)



    pump_pos1 = 0
    pump_pos2 = 0

    while (pump_pos1 != next_pos1  or   pump_pos2 != next_pos2):
        pump_pos1 = GV.pump1.get_plunger_position(pump_address1)        
        time.sleep(0.5)
        pump_pos2 = GV.pump1.get_plunger_position(pump_address2)
        print("\tpump1 pos:",pump_pos1, "/", next_pos1,"\t\tpump2 pos:",pump_pos2,"/", next_pos2)
        time.sleep(0.5)

    #check if dose signal is receved 
    GV.next_E = 1
    str1 = "pump 1 pickup Var.:\nTit. Vol. +Asp. Overshoot\n""pump 2 pickup Var.:\nSample Vol. +Asp. Overshoot"
    GV.SM_TEXT_TO_DIAPLAY ="S3,E0 -> action3_0" + str1


def action3_1():
    timeout = False
    Done = True
    if (GV.PAUSE == True):
        GV.next_E = 3        
        GV.SM_TEXT_TO_DIAPLAY = "S3,E1 -> action3_1\n" "  going to S3/E3"
        return 
    if (GV.ERROR == True or timeout==True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S3,E1 -> action3_1\n" "  going to S3/E4"
        return    
         
    if (Done == False):
        GV.next_E = 1
        GV.SM_TEXT_TO_DIAPLAY ="S3,E1 -> action3_1\n""   waiting for pump to reach position"
    else:
        GV.next_E = 2
        GV.SM_TEXT_TO_DIAPLAY ="S3,E1 -> action3_1\n""  go to S3/E2"


def action3_2():
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S3,E0 -> action3_0" "  going to S3/E4"
        return 
    
    total_asipiration_number = RECIPE["Degas"]["total_asipiration_number"]    
    str0 = "\ncurrent # Aspiration:{}\nTotal Aspirations:{}".format(GV.current_Aspiration_count, total_asipiration_number)    
    str1 =  "pump 1 dispense Var.:\nTit. Vol. +Asp. Overshoot\n""pump 2 dispense Var.:\nSample Vol. +Asp. Overshoot"
    GV.SM_TEXT_TO_DIAPLAY ="S3,E2 -> action3_2\n" + str1 + str0
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
    # print("S3,E3 -> action3_3")
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

    pump_speed = RECIPE["Degas"]["pump_speed"]    
    AspirationVolume_Overshoot = RECIPE["Degas"]["AspirationVolume_Overshoot"]

    pump_address1 = HW.TIRRANT_PUMP_ADDRESS
    pump_address2 = HW.SAMPLE_PUMP_ADDRESS

    starting_pos1 = GV.pump1.get_plunger_position(pump_address1)
    time.sleep(.5)
    GV.pump1.set_speed(pump_address1, pump_speed)
    time.sleep(.5)
    next_pos1 =  starting_pos1 - AspirationVolume_Overshoot
    GV.pump1.set_pos_absolute(pump_address1, next_pos1)
    time.sleep(1)

    starting_pos2 = GV.pump1.get_plunger_position(pump_address2)
    time.sleep(.5)
    GV.pump1.set_speed(pump_address2, pump_speed)
    time.sleep(1)
    next_pos2 =  starting_pos2 - AspirationVolume_Overshoot
    GV.pump1.set_pos_absolute(pump_address2, next_pos2)



    pump_pos1 = 0
    pump_pos2 = 0

    while (pump_pos1 != next_pos1  or   pump_pos2 != next_pos2):
        pump_pos1 = GV.pump1.get_plunger_position(pump_address1)        
        time.sleep(0.5)
        pump_pos2 = GV.pump1.get_plunger_position(pump_address2)
        print("\tpump1 pos:",pump_pos1, "/", next_pos1,"\t\tpump2 pos:",pump_pos2,"/", next_pos2)
        time.sleep(0.5)



    str1 =  "pump 1 dispense Var.:\nTit. Vol. +Asp. Overshoot\n""pump 2 dispense Var.:\nSample Vol. +Asp. Overshoot"
    GV.SM_TEXT_TO_DIAPLAY ="S4,E0 -> action4_0" + str1
    GV.next_E = 1


def action4_1():
    timeout = False
    Done = True
    if (GV.PAUSE == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1\n" " going to S4/E5"
        return 
    if (GV.ERROR == True or timeout==True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = "S4,E1 -> action4_1\n" " going to S4/E6"
        return 


    if (Done == False):
        GV.SM_TEXT_TO_DIAPLAY ="S4,E1 -> action4_1\n""   waiting for pump to reach position"
        GV.next_E = 1
    else:
        str1 = "  pumps in  position...\n" "  go to S4/E2"
        GV.SM_TEXT_TO_DIAPLAY ="S4,E1 -> action4_1"+ str1
        GV.next_E = 2

def action4_2():    
    if (GV.PAUSE == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S4,E2 -> action4_2\n" " going to S4/E5"
        return 
    if (GV.ERROR == True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = "S4,E2 -> action4_2\n" " going to S4/E6"
        return          

    GV.current_Aspiration_count += 1
    total_asipiration_number = RECIPE["Degas"]["total_asipiration_number"]    
    # str0 = "current # Aspiration:{}  Total Aspirations:{}".format(GV.current_Aspiration_count, total_asipiration_number)
    if (GV.current_Aspiration_count <= total_asipiration_number):
        GV.next_E = 3
        str1 = "aspiration count = {}/{}\n".format(GV.current_Aspiration_count, total_asipiration_number) 
        str1 += "aspiration count not reached yet\n"
        GV.SM_TEXT_TO_DIAPLAY ="S4,E2 -> action4_2" + str1 
    else:
        GV.next_E = 4
        str1 = "  aspiratin count reached" "  go to S4/E3"
        GV.SM_TEXT_TO_DIAPLAY ="S4,E2 -> action4_2" + str1



def action4_3():
    if (GV.PAUSE == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S4,E3 -> action4_3" "  going to S4/E5"    
    if (GV.ERROR == True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = "S4,E3 -> action4_3" " going to S4/E6"
        return         

    GV.SM_TEXT_TO_DIAPLAY = "S4,E3 -> action4_3" "  going back to S2/E0"
    GV.next_E = 0


def action4_4():
    if (GV.PAUSE == True):
        GV.next_E = 5
        GV.SM_TEXT_TO_DIAPLAY = "S4,E4 -> action4_4" "  going to S4/E5"
    if (GV.ERROR == True):
        GV.next_E = 6
        GV.SM_TEXT_TO_DIAPLAY = "S4,E4 -> action4_4" " going to S4/E6"
        return         

    GV.SM_TEXT_TO_DIAPLAY = "S4,E4 -> action4_4" "  going to S5/E0"
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
        GV.SM_TEXT_TO_DIAPLAY = "S5,E0 -> action5_0" "  goint to S5/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S5,E0 -> action5_0" "  goint to S5/E4"
        return    
            
    GV.SM_TEXT_TO_DIAPLAY ="S5,E0 -> action5_0" "  set TEC to experiment temperature"
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
    
    GV.terminate_SM = True
    GV.next_E = 2
    GV.SM_TEXT_TO_DIAPLAY ="S5,E1 -> action5_1\n"  "  Degasing completed\n" "  returning to the main GUI"
    

def action5_2():
    if (GV.ERROR == True):
        GV.next_E = 3
        GV.SM_TEXT_TO_DIAPLAY = "S5,E2 -> action5_2" "  goint to S5/E3"
        return 
    if (GV.ERROR == True):
        GV.next_E = 4
        GV.SM_TEXT_TO_DIAPLAY = "S5,E2 -> action5_2" "  goint to S5/E4"
        return 

    GV.SM_TEXT_TO_DIAPLAY ="S5,E2 -> action5_2\n "" terminate the SM"
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
    # print("S6,E1 -> action6_1")
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
    # print("S6,E5 -> action6_5")
    GV.SM_TEXT_TO_DIAPLAY ="S6,E5 -> action6_5\n""  going back to S5/E0"

def action6_6():
    GV.next_E = 0
    # print("S6,E5 -> action6_5")
    GV.SM_TEXT_TO_DIAPLAY ="S6,E6 -> action6_6\n""  going to S6/E6"

#--------------
def action7_0():
    print("S7,E0 -> action7_0")
    GV.next_E = 0
    GV.SM_TEXT_TO_DIAPLAY ="S7,E0 -> action7_0"

