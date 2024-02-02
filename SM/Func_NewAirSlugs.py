import  general.global_vars as GV
import  time
from    general.recipe import RECIPE






# pump_address2 = 5  #HW.SAMPLE_PUMP_ADDRESS  
# valve_address2 = 8  # HW.DEGASSER_ADDRESS

pump_address1 = 1 #HW.TIRRANT_PUMP_ADDRESS
valve_address1 = 9 # HW.SAMPLE_CLEANING_ADDRESS




def NewAirSlugs(pump_address, valve_address):
    pump_speed = RECIPE["Func_NewAirSlugs"]["pump_speed"]
    air_slug_total_count = RECIPE["Func_NewAirSlugs"]["AirSlug_Total_count"]
    air_slug_volume = RECIPE["Func_NewAirSlugs"]["AirSlug_Volume"]
    LastAirSlug_Volume = RECIPE["Func_NewAirSlugs"]["LastAirSlug_Volume"]
    SC2_Volume = RECIPE["Func_NewAirSlugs"]["SC2_Volume"]
    WaterSlug_Volume = RECIPE["Func_NewAirSlugs"]["WaterSlug_Volume"]

    
    tot =0

    starting_pos = GV.pump1.get_plunger_position(pump_address)
    
    GV.pump1.set_speed(pump_address, pump_speed)
    time.sleep(1)

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
 

if __name__ == "__main__":
    NewAirSlugs(pump_address1, valve_address1)

