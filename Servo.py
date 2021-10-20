import Adafruit_PCA9685
from termcolor import colored

class Servo:
    def print_servo(self):
        attrs = vars(self)
        print(' '.join('%s-> %s' %item for item in attrs.items()))

    def set_position(self,servo_angle):
        '''Set servo position with theoretical values'''
        print('Servo set position: {:.2f}'.format(servo_angle))
        if(servo_angle > self.Theta_max):
            servo_angle= self.Theta_max
        if(servo_angle < self.Theta_min):
            servo_angle= self.Theta_min
        pulses_on = int(( self.T_counts * ( self.T_max_us - self.T_min_us ) * ( servo_angle - self.Theta_abs_min) ) / ( (self.Theta_max - self.Theta_min) * self.T_us ))
        print('Pulses on: '+str(pulses_on))
        self.pwm_driver.set_pwm(self.channel,0,pulses_on)

    def __init__(self,dev_name = 'servo', channel = 0, op_freq = 50.0, T_max_us = 2500, T_min_us = 500, T_center_us = 1500, Theta_max = 90, Theta_min = -90, Theta_center = 0) -> None:
        print('Servo init')
        if not isinstance(channel, (int)):
            raise TypeError("Servo channel must be an integer")
        if not isinstance(dev_name, str):
            raise TypeError("Device name must be a string")
        if not isinstance(op_freq, (float,int)):
            raise TypeError("Operating frequency must be float or integer")
        if not isinstance(T_max_us, (int)):
            raise TypeError("T_max_us must be an integer")
        if not isinstance(T_min_us, (int)):
            raise TypeError("T_min_us must be an integer")
        if not isinstance(T_center_us, (int)):
            raise TypeError("T_center_us must be an integer")

        if not isinstance(Theta_max, (int,float)):
            raise TypeError("Theta_max must be integer or float")
        if not isinstance(Theta_min, (int,float)):
            raise TypeError("Theta_min must be integer or float")
        if not isinstance(Theta_center, (int,float)):
            raise TypeError("Theta_center must be integer or float")
    
        self.device_name = dev_name   
        self.channel = channel
        self.operating_frequency = op_freq
        self.T_us = int(1000000/op_freq)
        self.T_counts = 4095
        self.pwm_driver = Adafruit_PCA9685.PCA9685()
        self.pwm_driver.set_pwm_freq(op_freq)
        self.T_max_us = T_max_us
        self.T_min_us = T_min_us
        self.T_center_us = T_center_us
        self.Theta_max = Theta_max
        self.Theta_min = Theta_min
        self.Theta_center = Theta_center
        self.m = ((Theta_max-Theta_center)/(T_max_us-T_center_us))
        self.Theta_abs_min = Theta_max - self.m * T_max_us
        self.T_max_counts = int(self.T_counts * self.T_max_us / self.T_us)
        self.T_min_counts = int(self.T_counts * self.T_min_us / self.T_us)
        self.T_center_counts = int(self.T_counts * self.T_center_us / self.T_us)


        self.print_servo()
        
