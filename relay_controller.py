# encoding=utf-8
import serial
import time

class RelayController:
    def __init__(self, serial_port):
        SerialPort = serial_port
        BaudRate = 9600
        self.ser = serial.Serial(SerialPort,BaudRate,timeout=0.5)
        print("ParameterSetting：SerialPort = {},BaudRate = {}".format(SerialPort,BaudRate))
        self.dataopen = []
        self.dataclose = []
        for idx in range(4):
            channel = (idx + 1) & 0xFF
            checkcode_open = (0x33 + 0x01 + 0x12 + 0x00 + 0x00 + 0x00 + channel) & 0xFF
            checkcode_close = (0x33 + 0x01 + 0x11 + 0x00 + 0x00 + 0x00 + channel) & 0xFF
            self.dataopen.append((0x33,0x01,0x12,0x00,0x00,0x00,channel,checkcode_open))
            self.dataclose.append((0x33,0x01,0x11,0x00,0x00,0x00,channel,checkcode_close))
        self.dict_idx = {"PRESS":0, "VAC":1, "AB":2}

    #Open
    def open(self, channel):
        if isinstance(channel, int):
            self.ser.write(self.dataopen[channel - 1])
        elif isinstance(channel, str):
            self.ser.write(self.dataopen[self.dict_idx[channel]])

    #Close
    def close(self, channel):
        if isinstance(channel, int):
            self.ser.write(self.dataclose[channel - 1])
        elif isinstance(channel, str):
            self.ser.write(self.dataclose[self.dict_idx[channel]])

if __name__ == '__main__': 
    controller = RelayController("COM3")
    for idx in range(4):
        controller.open(idx + 1)
        time.sleep(5)
        controller.close(idx + 1)
        time.sleep(5)