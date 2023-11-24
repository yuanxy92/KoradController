from mcush import *
import time

def enable(controllers):
    controllers['Body'].output(0.0)
    controllers['Body'].outputEnable()
    controllers['LF'].output(0.0)
    controllers['LF'].outputEnable()
    controllers['RF'].output(0.0)
    controllers['RF'].outputEnable()
    controllers['LB'].output(0.0)
    controllers['LB'].outputEnable()
    controllers['RB'].output(0.0)
    controllers['RB'].outputEnable()
    return

def disable(controllers):
    controllers['Body'].output(0.0)
    controllers['Body'].outputDisable()
    controllers['LF'].output(0.0)
    controllers['LF'].outputDisable()
    controllers['RF'].output(0.0)
    controllers['RF'].outputDisable()
    controllers['LB'].output(0.0)
    controllers['LB'].outputDisable()
    controllers['RB'].output(0.0)
    controllers['RB'].outputDisable()
    return

def standup(controllers):
    controllers['Body'].output(6.0)
    controllers['LF'].output(4.0)
    controllers['RF'].output(4.0)
    controllers['LB'].output(4.0)
    controllers['RB'].output(4.0)
    return

def crawl(controllers):
    controllers['LF'].output(5.0)
    controllers['LB'].output(5.0)
    controllers['RF'].output(1.0)
    controllers['RB'].output(1.0)
    time.sleep(2)
    controllers['LF'].output(1.0)
    controllers['LB'].output(1.0)
    controllers['RF'].output(5.0)
    controllers['RB'].output(5.0)
    time.sleep(2)
    controllers['LF'].output(5.0)
    controllers['LB'].output(5.0)
    controllers['RF'].output(1.0)
    controllers['RB'].output(1.0)
    time.sleep(2)
    controllers['LF'].output(1.0)
    controllers['LB'].output(1.0)
    controllers['RF'].output(5.0)
    controllers['RB'].output(5.0)
    time.sleep(2)
    controllers['LF'].output(5.0)
    controllers['LB'].output(5.0)
    controllers['RF'].output(1.0)
    controllers['RB'].output(1.0)
    time.sleep(2)
    controllers['LF'].output(1.0)
    controllers['LB'].output(1.0)
    controllers['RF'].output(5.0)
    controllers['RB'].output(5.0)
    time.sleep(2)
    return

def crawl2(controllers):
    von0 = 7.25
    von1 = 5.5
    von2 = 1.5
    voff = 0.0
    von_body1 = 2.5
    von_body2 = 6.0
    von_body3 = 3.0
    sleeptime = 1.5
    
    for idx in range(10):
        controllers['LB'].output(von1)
        controllers['RB'].output(von1)
        controllers['Body'].output(von_body2)
        time.sleep(sleeptime)
        controllers['LF'].output(von0)
        controllers['RF'].output(von0)
        controllers['Body'].output(von_body1)
        time.sleep(0.5)
        controllers['LB'].output(von2)
        controllers['RB'].output(von2)
        time.sleep(sleeptime)
        controllers['LF'].output(voff) 
        controllers['RF'].output(voff)
        controllers['LB'].output(voff)
        controllers['RB'].output(voff)
        controllers['Body'].output(voff)
        time.sleep(sleeptime)
    return

id_part_dict = {'54019392': 'Body', 
                '54015044': 'RB', 
                '54019689': 'RF', 
                '54019701': 'LF', 
                '54019699': 'LB'}
deviceTTYIDs = [6, 7, 8, 9, 11]
controllers = dict()
for i in range(5):
    power = Korad.KA3005P(f'/dev/ttyS{deviceTTYIDs[i]}')
    serial_num = power.getIntegerSerialNumber()
    print(serial_num)
    controllers[id_part_dict[f'{serial_num}']] = power

enable(controllers)
crawl2(controllers)
disable(controllers)

