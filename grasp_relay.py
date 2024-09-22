# encoding=utf-8
from koradserial import KoradSerial
import serial
import time
import relay_controller as rc

class gas_control():
    def __init__(self) -> None:
        # init relay
        id_part_dict = {'KORAD KA3005P V5.8 SN:03384673': 'BILI',
                        'KORAD KA3005P V5.8 SN:03384675': 'BILI2'}
        self.relay_controllers = rc.RelayController("COM3")
        # init power for press control
        controllers = dict()
        for i in [4,5]:
            power = KoradSerial(f'COM{i}')
            serial_num = power.model
            print(serial_num)
            controllers[id_part_dict[f'{serial_num}']] = power
        self.controllers = controllers
        self.working_flag = False

    def vaccum(self,target_voltage=5.0,duration=-1):
        controllers = self.controllers
        #VAC是正负压气阀的负压   AB是两位三通阀
        # if self.working_flag:
        #     print('working!!!')
        #     return
        self.relay_controllers.open("VAC")
        # controllers['VAC'].channels[0].voltage = 24
        # controllers['VAC'].channels[0].current = 0.2
        # controllers['VAC'].output.on()
        time.sleep(0.2)

        self.relay_controllers.open("AB")
        # controllers['AB'].channels[0].voltage = 24
        # controllers['AB'].channels[0].current = 0.2
        # controllers['AB'].output.on()
        gate_key = 'BILI2'
        controllers[gate_key].channels[0].voltage = target_voltage
        controllers[gate_key].channels[0].current = 0.5
        controllers[gate_key].output.on()

        self.working_flag = True
        if duration>0:
            time.sleep(duration)
            self.vaccum_off()

    def vaccum_off(self):
        gate_key = 'BILI2'
        self.controllers[gate_key].output.off()
        time.sleep(1)
        # self.controllers['AB'].output.off()
        self.relay_controllers.close("AB")
        time.sleep(1)
        #放气
        # self.controllers['VAC'].output.off()
        self.relay_controllers.close("VAC")
        time.sleep(1)
        print('finish vaccum')
        self.working_flag = False
        
    #RB是正负压气阀的正压  body是比例阀  两位三通常态就在正压上
    def grasp(self,target_voltage = 5.0,duration=-1):    
        controllers = self.controllers
        # if self.working_flag:
        #     print('working!!')
        #     return
        gate_key = 'BILI'
        # self.relay_controllers.open("AB")
        # time.sleep(1)
        self.relay_controllers.open("PRESS")
        # controllers['PRESS'].channels[0].voltage = 24
        # controllers['PRESS'].channels[0].current = 0.2
        # controllers['PRESS'].output.on()
        time.sleep(0.2)
        #target_voltage = 5.0
        step = 0.5

        controllers[gate_key].channels[0].voltage = target_voltage
        controllers[gate_key].channels[0].current = 0.5
        controllers[gate_key].output.on()
        self.working_flag = True
        if duration>0:
            self.grasp_off()
    
    def set_voltage(self,target_voltage = 5.0,gate_key = 'BILI'):
        controllers = self.controllers
        controllers[gate_key].channels[0].voltage = target_voltage
        controllers[gate_key].channels[0].current = 0.5
        controllers[gate_key].output.on()
    
    def grasp_off(self,gate_key='BILI'):
        self.controllers[gate_key].output.off()
        time.sleep(2)
        if gate_key == 'BILI':
            self.relay_controllers.close("PRESS")
        # self.controllers['PRESS'].output.off()
        print('finish grasp!')
        self.working_flag = False
    
    def set_working_flag(self,flag):
        self.working_flag = flag



if __name__ == '__main__':

    g_control = gas_control()
    g_control.vaccum(target_voltage=5.0, duration=-1)
    time.sleep(5)
    g_control.vaccum_off()
    time.sleep(5)
    g_control.grasp(target_voltage=5.0, duration=-1)
    time.sleep(5)
    g_control.grasp_off()

    # id_part_dict = {'KORAD KA3005P V5.8 SN:03384673': 'BILI',
    #                 'KORAD KA3005P V5.8 SN:03384675': 'BILI2'}
    # relay_controllers = rc.RelayController("COM3")
    # # init power for press control
    # controllers = dict()
    # for i in [4,5]:
    #     power = KoradSerial(f'COM{i}')
    #     serial_num = power.model
    #     print(serial_num)
    #     controllers[id_part_dict[f'{serial_num}']] = power
    # controllers = controllers
    # working_flag = False
    
    # a = 1

