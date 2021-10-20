import Adafruit_PCA9685
import sys
import RotatingCamera
import time
import colorama
from termcolor import colored
from Servo import *

#from sklearn import linear_model
#from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

from utilities.json_utilities import *

pulses_on_list = []
angles_list = np.arange(-180.0,200.0,22.5)
lookup_table_json = 'servo_lookup_table.json'
servo_channel = 0

print(angles_list)

try:
    colorama.init(autoreset=True)
    # Objeto rotating camera
    camera = RotatingCamera.RotatingCamera(gear_ratio=2.0)
    choice = 'c'

    print(colored('Data capture','yellow'))
    event = 0
    angles_len = len(angles_list)
    while(event != angles_len):
        if(choice is not 'r'):
            # Acercamiento a setpoint teorico
            camera.set_position(angles_list[event])
        else:
            # Conserva posicion actual
            pass
        # Input de pulsos en on deseados para el servo
        print(colored('event: {}'.format(event),'magenta'))
        ok = False
        while(not ok):
            try:
                pulses_on = int(input(colored('Type pulses_on for angle = {:.1f} : '.format(angles_list[event]),'blue')))
                ok = True
            except Exception as e:
                print(colored(e,'red'))
                ok = False
        print(colored('Wait for servo positioning...','yellow'),end='')
        camera.servo_driver.pwm_driver.set_pwm(servo_channel,0,pulses_on)
        time.sleep(5)
        print(colored('OK','green'))
        time.sleep(2)

        choice = input('Type r to repeat pulses_on capture or Enter to continue ')
        if(choice is not 'r'):
            event += 1
            pulses_on_list.append(pulses_on)   # Llenado de lista de pulsos en on
            choice = 'c'

    print(colored('Data acquisition OK','cyan'))
    print(colored('pulses_on_list: '+str(pulses_on_list),'blue'))
    print(colored('angles_list: '+str(angles_list),'green'))


    while True:
        choice = input(colored('Update lookup table? y/n\n','magenta'))
        if(choice in ('y','n')):
            if(choice is 'y'):
                # Actualizacion de JSON de tabla de consulta
                lookup_table = json_to_dict(lookup_table_json) 
                lookup_table['angles'] = list(angles_list)
                lookup_table['pulses_on'] = pulses_on_list
                dict_to_json(lookup_table,lookup_table_json)


                print(colored('Lookup table updated','blue'))
                print('angles: '+str(lookup_table['angles']))
                print('pulses on: '+str(lookup_table['pulses_on']))
                break
            else:
                print(colored('Lookup table not updated','yellow'))
                break

    

except KeyboardInterrupt:
    print(colored('Keyboard Interrupt','red'))