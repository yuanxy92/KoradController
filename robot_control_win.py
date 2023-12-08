from koradserial import KoradSerial

id_part_dict = {'KORAD KA3005P V5.8 SN:03384540': 'Body',
                'KORAD KA3005P V5.8 SN:03383444': 'RB',
                'KORAD KA3005P V5.8 SN:03384673': 'LB',
                'KORAD KA3005P V5.8 SN:03384675': 'LF',
                'KORAD KA3005P V5.8 SN:03384669': 'RF'}
deviceTTYIDs = [6, 7, 8, 9, 11]
controllers = dict()
for i in range(len(deviceTTYIDs)):
    power = KoradSerial(f'COM{deviceTTYIDs[i]}')
    serial_num = power.model
    print(serial_num)
    controllers[id_part_dict[f'{serial_num}']] = power
    
a = 1