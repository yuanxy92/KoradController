from koradserial import KoradSerial

partnames = ['Body', 'LF', 'RF', 'LB', 'RB']
id_part_dict = {'KORAD KA3005P V5.8 SN:03384540': 'Body',
                'KORAD KA3005P V5.8 SN:03383444': 'RB',
                'KORAD KA3005P V5.8 SN:03384673': 'LB',
                'KORAD KA3005P V5.8 SN:03384675': 'LF',
                'KORAD KA3005P V5.8 SN:03384669': 'RF'}
deviceTTYIDs = [6, 7, 8, 9, 11]
controllers = dict()
# for i in range(len(deviceTTYIDs)):
#     power = KoradSerial(f'COM{deviceTTYIDs[i]}')
#     serial_num = power.model
#     print(serial_num)
#     controllers[id_part_dict[f'{serial_num}']] = power

# # test set voltage to 1
# for idx in range(5):
#     controllers[partnames[idx]].channels[0].voltage = 0.0
#     controllers[partnames[idx]].channels[0].current = 1.0

# init controller window
import tkinter
from tkinter import *
from tkinter.font import Font

root = tkinter.Tk()

my_font_l = Font(family="Arial", size=20, weight="bold")
my_font = Font(family="Arial", size=15, weight="bold")
voltage_step = 0.1
def voltage_body_p():
    controllers['Body'].channels[0].voltage = controllers['Body'].channels[0].voltage + voltage_step
    print("Hello World!")
def voltage_body_m():
    controllers['Body'].channels[0].voltage = controllers['Body'].channels[0].voltage - voltage_step
def voltage_LF_p():
    print("Hello World!")
def voltage_LF_m():
    print("Hello World!")
def voltage_RF_p():
    print("Hello World!")
def voltage_RF_m():
    print("Hello World!")
def voltage_LB_p():
    print("Hello World!")
def voltage_LB_m():
    print("Hello World!")
def voltage_RB_p():
    print("Hello World!")
def voltage_RB_m():
    print("Hello World!")

root.geometry('1000x600')
root.title('Pneumatic Soft Robot Controller')
btn_width = 25
btn_height = 3

label_button_onoff = Label(root, text="ON/OFF", font=my_font_l, fg='red')
label_button_onoff.grid(row=0, column=3, columnspan=1, sticky=N+S+W+E)
btn_on = Button(root, text='Body\n+', width=btn_width, height=btn_height, font=my_font, command=voltage_body_p)
btn_on.grid(row=0, column=3, rowspan=2, sticky=N+S)
btn_off = Button(root, text='Body\n-', width=btn_width, height=btn_height, font=my_font, command=voltage_body_m)
btn_off.grid(row=1, column=3, rowspan=2, sticky=N+S)

label_button = Label(root, text="Buttons for voltage", font=my_font_l, fg='red')
label_button.grid(row=0, column=0, columnspan=3, sticky=N+S+W+E)

btn_body = Button(root, text='Body\n+', width=btn_width, height=btn_height, font=my_font, command=voltage_body_p)
btn_body.grid(row=1, column=1, rowspan=2, sticky=N+S)
btn_body = Button(root, text='Body\n-', width=btn_width, height=btn_height, font=my_font, command=voltage_body_m)
btn_body.grid(row=3, column=1, rowspan=2, sticky=N+S)

btn_LF_p = Button(root, text='Left front leg\n+', width=btn_width, height=btn_height, font=my_font)
btn_LF_p.grid(row=1, column=0, sticky=N+S+W+E)
btn_LF_m = Button(root, text='Left front leg\n-', width=btn_width, height=btn_height, font=my_font)
btn_LF_m.grid(row=2, column=0, sticky=N+S+W+E)
btn_RF_p = Button(root, text='Right front leg\n+', width=btn_width, height=btn_height, font=my_font)
btn_RF_p.grid(row=1, column=2, sticky=N+S+W+E)
btn_RF_m = Button(root, text='Right front leg\n-', width=btn_width, height=btn_height, font=my_font)
btn_RF_m.grid(row=2, column=2, sticky=N+S+W+E)

btn_LB_p = Button(root, text='Left hind leg\n+', width=btn_width, height=btn_height, font=my_font)
btn_LB_p.grid(row=3, column=0, sticky=N+S+W+E)
btn_LB_m = Button(root, text='Left hind leg\n-', width=btn_width, height=btn_height, font=my_font)
btn_LB_m.grid(row=4, column=0, sticky=N+S+W+E)
btn_RB_p = Button(root, text='Right hind leg\n+', width=btn_width, height=btn_height, font=my_font)
btn_RB_p.grid(row=3, column=2, sticky=N+S+W+E)
btn_RB_m = Button(root, text='Right hind leg\n-', width=btn_width, height=btn_height, font=my_font)
btn_RB_m.grid(row=4, column=2, sticky=N+S+W+E)

label_current = Label(root, text="Current voltage:", font=my_font_l, fg='red')
label_current.grid(row=5, column=0, columnspan=3, sticky=N+S+W+E)
label_body = Label(root, text="Body voltage:\n", width=btn_width, height=btn_height, font=my_font)
label_body.grid(row=6, column=1, rowspan=2, sticky=N+S)
label_LF = Label(root, text="Left front leg voltage:\n", width=btn_width, height=btn_height, font=my_font)
label_LF.grid(row=6, column=0, sticky=N+S+W+E)
label_RF = Label(root, text="Right front leg voltage:\n", width=btn_width, height=btn_height, font=my_font)
label_RF.grid(row=6, column=2, sticky=N+S+W+E)
label_LB = Label(root, text="Left hind leg voltage:\n", width=btn_width, height=btn_height, font=my_font)
label_LB.grid(row=7, column=0, sticky=N+S+W+E)
label_RB = Label(root, text="Right hind leg voltage:\n", width=btn_width, height=btn_height, font=my_font)
label_RB.grid(row=7, column=2, sticky=N+S+W+E)

root.mainloop()



a = 1