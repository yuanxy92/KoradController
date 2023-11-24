from mcush import *

id_part_dict = {'54019392': '1', 
                '54015044': '2', 
                '54019689': '3', 
                '54019701': '4', 
                '54019699': '5'}
deviceTTYIDs = [6, 7, 8, 9, 11]
controllers = dict()
for i in range(5):
    power = Korad.KA3005P(f'/dev/ttyS{deviceTTYIDs[i]}')
    serial_num = power.getIntegerSerialNumber()
    print(serial_num)
    controllers[id_part_dict[f'{serial_num}']] = power
