from ctypes import *


AXIS_ID_01 = 24
POWER_ON = 1
POWER_OFF =0

class motor_1():
    def __init__(self, speed, acceleration):
        self.speed = speed
        self.acceleration = acceleration
        self.mydll1 =CDLL("./config/TML_LIB.dll")
        
        self.fd = self.mydll1.TS_OpenChannel(b"COM7",0, AXIS_ID_01, 115200)
        # print("motor 1 - openning COM7 port:", fd)

        #/*	Load the *.t.zip with setup data generated with EasyMotion Studio or EasySetUp */
        # idxSetup = mydll1.TS_LoadSetup(b"./test1.t.zip")
        idxSetup = self.mydll1.TS_LoadSetup(b"./config/SpdTst.t.zip")
        if (idxSetup < 0):
            print('cannot  load motor 1 controller setup')
        else:
            print("Motor 1 controller setup loaded sucessfully")


        #/*	Setup the axis based on the setup data previously loaded */
        tt = self.mydll1.TS_SetupAxis(AXIS_ID_01, idxSetup)
        # print(' setup axis:', tt)

        #	Select the destination axis of the TML commands 
        tt =self. mydll1.TS_SelectAxis(AXIS_ID_01)
        # print(' select dest. axis:', tt)

        #/*	Execute the initialization of the drive (ENDINIT) */
        tt = self.mydll1.TS_DriveInitialisation()
        # print('init successful:', tt)

        # motor 1 power on:
        y = self.mydll1.TS_ReadStatus
        y.restype = c_bool
        y.argtypes = [c_int,POINTER(c_int)]
        p = c_int()
        buf = create_string_buffer(1)
        tt = self.mydll1.TS_Power(POWER_ON)
        # print('Power On successful:', tt)


        # sAxisOn_flag = pointer to unsinged short
        sAxiOn_flag = 0
        REG_SRL =3
        while ((p.value & (1<<15)) == 0):
            tt = y(REG_SRL,  byref(p))
            
        # print('{:X} = {:b} '.format(p.value,p.value))


    def set_speed(self, speed):
        # speed = 300.
        

        x = self.mydll1.TS_MoveVelocity
        x.restype = c_bool
        x.argtypes = [c_double,c_double, c_int, c_int]
        # tt = x(100., .01,1,0)
        tt = x(speed, self.acceleration,1,0)
        return tt
        # print(tt)


    def stop(self):
        speed = 0
        x = self.mydll1.TS_MoveVelocity
        x.restype = c_bool
        x.argtypes = [c_double,c_double, c_int, c_int]

        tt = x(speed, self.acceleration,1,0)
        # print(tt)


        tt = self.mydll1.TS_Power(POWER_OFF)
        # print('Power Off successful:', tt)

        self.mydll1.TS_CloseChannel(self.fd);