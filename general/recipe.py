RECIPE= {
    "Startup": 
    {
        "enable": False,
        "gantry_move_speed": 0,
        "gantry_home_timeout": 0,   
        "gantry_homing_speed": 0,
        "horizontal_cell_fill_position": 0,
        "gantry_move_timeout": 0,
        "vertical_cell_fill_position": 0
    },
    "PumpInit_Reload": 
    {
        "enable": False,
        "pump_speed": 0,
        "valve_move_timeout": 0,
        "pump_init_timeout": 0,
        "pump_move_timeout": 0,  
        "loadH2O2_timeout": 0,
        "TitrantPumpt_syringe_fill_volume": 0,
        "SamplePumpt_syringe_fill_volume": 0,
        "titrantpump_expelair_volume": 0,
        "samplepump_expelair_volume": 0,
        "AirSlug_total_Count": 0,
		"AirSlug_Volume": 0,
		"WaterSlug_Volume": 0
    },
    "Degas": 
    {
        "enable": False,
        "pump_speed": 0,
        "valve_move_timeout": 0,        
        "pump_move_timeout": 0,
        "degas_temp": 0,
        "experiment_temp": 0,
        "temperature_settledown_timeout": 0,
        "heat_time": 0,
        "AspirationVolume_Overshoot": 0,
        "total_asipiration_number": 0
    },
    "Load_Prime": 
    {
        "enable": False,
        "pump_speed": 0,
        "valve_move_timeout": 0,
        "pump_move_timeout": 0,
        "TC2_Volume": 0,
        "SC2_Volume": 0
    },
    "GantrytoB": 
    {
        "enable": False,
        "gantry_move_speed": 0,
        "horizontal_titration_position": 0,
        "vertical_titration_position": 0,
        "gantry_move_timeout": 0
    },
    "Experiment": 
    {
        "enable": True,
        "titrationpump_speed": 100,
        "valve_move_timeout": 60,        
        "titrationpump_move_timeout": 600, 
        "dose_volume": 5,
        "totaldose_count": 5,
        "mixing_speed": 200,
        "equilmix_time": 600,
        "dosestandby_time": 600
    },
    "Func_NewAirSlugs": 
    {
        "enable": False,
        "pump_speed": 0,
        "valve_move_timeout": 0,
        "pump_move_timeout": 0,
        "AirSlug_Total_count": 0,
        "AirSlug_Volume": 0,
        "LastAirSlug_Volume": 0,
        "SC2_Volume": 0,
        "WaterSlug_Volume": 0
    }    
 }


def init():
    global RECIPE    
    print("initialing recipe variables ....")
    # print(recipe)
    # print("--------------------------")
    pass
