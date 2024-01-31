#------------ SM GLOBAL VARIABLES -------------------------------------------

next_E = 0 
cur_S = 0
prev_S = 0
terminate_SM = False
doescount = 5
dose_number = 0
SM_TEXT_TO_DIAPLAY = "--"
PAUSE = False
ERROR = False
NEXT = False
activate_NEXT_button = False


def reset():
    next_E = 0 
    cur_S = 0
    prev_S = 0
    terminate_SM = False
    doescount = 5
    dose_number = 0
    SM_TEXT_TO_DIAPLAY = "--"
    PAUSE = False
    ERROR = False

# class General_vars():
#     def __init__(self) -> None:
#         self.next_E = 0 
#         self.cur_S = 0
#         self.prev_S = 0
#         self.terminate_SM = False
#         self.doescount = 5
#         self.dose_number = 0
#         self.SM_TEXT_TO_DIAPLAY = "--"
#         self.PAUSE = False
#         self.ERROR = False
    
#     def reset(self):
#         self.next_E = 0 
#         self.cur_S = 0
#         self.prev_S = 0
#         self.terminate_SM = False
#         self.doescount = 5
#         self.dose_number = 0
#         self.SM_TEXT_TO_DIAPLAY = "--"
#         self.PAUSE = False
#         self.ERROR = False


def init():
    # GENERAL = General_vars()
    reset()
   