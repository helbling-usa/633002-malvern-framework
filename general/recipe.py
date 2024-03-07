RECIPE= {
    "Startup": 
    {
        "enable": True,
        "gantry_move_speed_hor": 20,
        "gantry_move_speed_ver": 20,
        "gantry_home_timeout": 500,   
        "gantry_homing_speed": 1,
        "gantry_move_timeout": 60,
        "horizontal_cellfill_position": 50,
        "vertical_cellfill_position": 50
    },
    "PumpInit_Reload": 
    {
        "enable": False,
        "sample_pump_step": "micro step",
        "titrant_pump_step": "micro step",
        "titrant_pump_speed": 1000,
        "sample_pump_speed": 1000,
        "valve_move_timeout": 60,
        "pump_init_timeout": 60,
        "pump_move_timeout": 60,  
        "samplepump_fill_speed": 200,
        "titrantpump_fill_speed": 200
    },   
    "Degas": 
    {
        "enable": False,
        "sample_pump_step": "full step",
        "titrant_pump_step": "full step",
        "titrant_pump_speed": 150,
        "sample_pump_speed": 50,
        "valve_move_timeout": 60,        
        "pump_move_timeout": 600, 
        "detergentrinse_count": 1,
        "waterrinse_count": 1,		
        "meohrinse_count": 1,
        "s4_volume":10,
        "degascleanfluid_volume": 10,
        "s_port_volume": 5,
        "t_Port_volume": 5,
        "sp2_volume": 5,
        "tp3_volume": 5
    },
    "Load_Prime": 
    {
        "enable": False,
        "sample_pump_step": "full step",
        "titrant_pump_step": "full step",
        "titrant_pump_speed": 10,
        "sample_pump_speed": 10,
        "valve_move_timeout": 60,        
        "pump_move_timeout": 60, 
        "TC2_Volume": 120,
        "SC2_Volume": 150,
        "titrantwetloop1_volume": 5,
        "samplewetloop1_volume": 5
    },
    "GantrytoB": 
    {
        "enable": False,
        "sample_pump_step": "full step",
        "titrant_pump_step": "full step",
        "gantry_move_speed_hor": 5,
        "gantry_move_speed_ver": 5,
        "vertical_high_position": 15,
        "horizontal_titration_position": 50,
        "vertical_titration_position": 50,
        "gantry_move_timeout": 60
    },
    "Experiment": 
    {
        "enable": False,
        "sample_pump_step": "micro step",
        "titrant_pump_step": "micro step",
        "sample_pump_speed": 200,
        "titrationpump_speed": 10,
        "valve_move_timeout": 60,        
        "titrationpump_move_timeout": 600, 
        "dose_volume": 500,
        "totaldose_count": 3,
        "mixing_speed": 200,
        "equilmix_time": 600,
        "dosestandby_time": 600,
        "mixingsignal_timeout": 100,
        "equilsignal_timeout": 100,
        "dosesignal_timeout": 100
    },      
    "GantrytoA": 
    {
        "enable": True,
        "False": "full step",
        "titrant_pump_step": "full step",
        "gantry_move_speed_hor": 5,
        "gantry_move_speed_ver": 5,
        "vertical_high_position": 15,
        "horizontal_cellfill_position": 50,
        "vertical_cellfill_position": 50,
        "gantry_move_timeout": 60
    },
    "GantryReturn": 
    {
        "enable": True,
        "sample_pump_step": "full step",
        "titrant_pump_step": "full step",
        "gantry_move_speed_hor": 5,
        "gantry_move_speed_ver": 5,
        "vertical_base_position": 15,
        "horizontal_base_position": 25,
        "gantry_move_timeout": 60
    },
    "DegasClean": 
    {
        "enable": False,
        "sample_pump_step": "full step",
        "titrant_pump_step": "full step",
        "titrant_pump_speed": 1000,
        "sample_pump_speed": 1000,
        "valve_move_timeout": 60,        
        "pump_move_timeout": 600, 
        "detergentrinse_count": 1,
        "waterrinse_count": 1,		
        "meohrinse_count": 1,
        "s4_volume":10,
        "degascleanfluid_volume": 10
    },
    "SampleLineClean": 
    {
        "enable": False,
        "sample_pump_step": "full step",
        "titrant_pump_step": "full step",
        "titrant_pump_speed": 1000,
        "sample_pump_speed": 1000,
        "valve_move_timeout": 60,        
        "pump_move_timeout": 600, 
        "detergentrinse_count": 1,
        "waterrinse_count": 1,		
        "meohrinse_count": 1
    },
	"TitrantLineClean": 
    {
        "enable": False,
        "titrant_pump_speed": 1000,
        "sample_pump_speed": 1000,
	    "sample_pump_step": "full step",
	    "titrant_pump_step": "full step",
        "valve_move_timeout": 60,        
        "pump_move_timeout": 600, 
	    "detergentrinse_count": 1,
	    "waterrinse_count": 1,		
	    "meohrinse_count": 1
    },
	"RecovClean":
    {
        "enable": False,
        "sample_pump_step": "full step",
        "titrant_pump_step": "full step",
        "titrant_pump_speed": 1000,
        "sample_pump_speed": 1000,
        "valve_move_timeout": 60,        
        "pump_move_timeout": 600, 
	    "detergentrinse_count": 1,
	    "waterrinse_count": 1,		
	    "meohrinse_count": 1
    },
    "Func_DiluteDetergent": 
    {
        "enable": False,
        "sample_pump_step": "full step",
        "titrant_pump_step": "full step",
        "titrant_pump_speed": 300,
        "sample_pump_speed": 300,
        "detergent_volume": 60,                
        "water_volume": 50,
        "lastairslug_volume":50
    },
    "Func_NewAirSlugs": 
    {
        "enable": False,
        "sample_pump_step": "full step",
	    "titrant_pump_step": "full step",
        "titrant_pump_speed": 300,
        "sample_pump_speed": 300,
        "valve_move_timeout": 60,
        "pump_move_timeout": 600,
        "AirSlug_Total_count": 2,
        "AirSlug_Volume": 100,
        "LastAirSlug_Volume": 500,
        "WaterSlug_Volume": 500
    }    
 }


def init():
    global RECIPE    
    print("initialing recipe variables ....")
    # print(recipe)
    # print("--------------------------")
    pass
