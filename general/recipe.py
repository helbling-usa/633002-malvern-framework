RECIPE= {
"Constants":
    {
        "enable": False,
        "titrant_volume": 30,
        "sample_volume": 300,
        "AspirationVolume_Overshoot": 10, 
        "horizontal_cell_fill_position": 50,
        "vertical_cell_fill_position": 50,
        "tc2_volume": 120, 
        "sc2_volume": 150, 
        "horizontal_titration_position": 130,
        "vertical_titration_position": 50,
        "totalstack_volume":100,
        "s_port_volume": 300, 
        "t_port_volume": 50,
        "sp2_volume": 100,
        "tp3_volume":100, 
        "s5_volume":100,
        "degascleanfluid_volume":100, 
        "samplecleanfluid_volume":100, 
        "s4_volume":100
	},    
    "Startup": 
    {
        "enable": True,
        "gantry_move_speed": 1,
        "gantry_home_timeout": 500,   
        "gantry_homing_speed": 1,
        "gantry_move_timeout": 60
    },
    "PumpInit_Reload": 
    {
        "enable": False,
        "sample_pump_step": "full step",
        "titrant_pump_step": "full step",
        "titrant_pump_speed": 1000,
        "sample_pump_speed": 1000,
        "valve_move_timeout": 60,
        "pump_init_timeout": 60,
        "pump_move_timeout": 60,  
        "loadH2O2_timeout": 600,
        "TitrantPumpt_syringe_fill_volume": 100,
        "SamplePumpt_syringe_fill_volume": 100,
        "titrantpump_expelair_volume": 200,
        "samplepump_expelair_volume": 200
    },   
    "Degas": 
    {
        "enable": False,
        "sample_pump_step": "full step",
        "titrant_pump_step": "full step",
        "titrant_pump_speed": 100,
        "sample_pump_speed": 100,
        "valve_move_timeout": 30,        
        "pump_move_timeout": 360,
        "degas_temp": 25,
        "experiment_temp": 30,
        "temperature_settledown_timeout": 1000,
        "heat_time": 10,
        "AspirationVolume_Overshoot": 300,
        "total_asipiration_number":4
    },
    "Load_Prime": 
    {
        "enable": False,
        "sample_pump_step": "full step",
        "titrant_pump_step": "full step",
        "titrant_pump_speed": 1000,
        "sample_pump_speed": 1000,
        "valve_move_timeout": 60,        
        "pump_move_timeout": 600, 
        "TC2_Volume": 120,
        "SC2_Volume": 150
    },
    "GantrytoB": 
    {
        "enable": False,
        "sample_pump_step": "full step",
        "titrant_pump_step": "full step",
        "gantry_move_speed": 10,
        "horizontal_titration_position": 50,
        "vertical_titration_position": 50,
        "gantry_move_timeout": 60
    },
    "Experiment": 
    {
        "enable": False,
        "sample_pump_step": "full step",
        "titrant_pump_step": "full step",
        "titrationpump_speed": 100,
        "valve_move_timeout": 60,        
        "titrationpump_move_timeout": 600, 
        "dose_volume": 5,
        "totaldose_count": 3,
        "mixing_speed": 200,
        "equilmix_time": 600,
        "dosestandby_time": 600
    },    
    "GantrytoA": 
    {
        "enable": False,
        "sample_pump_step": "full step",
        "titrant_pump_step": "full step",
        "gantry_move_speed": 10,
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
        "meohrinse_count": 1
    },
    "SampleLineClean": 
    {
        "enable": False,
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
