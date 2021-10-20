import Servo

class RotatingCamera:
    def set_position(self, angle):
        print('Rotating camera angle: {:.2f}'.format(angle))
        servo_angle = angle / self.gear_ratio
        self.servo_driver.set_position(servo_angle)

    def __init__(self, gear_ratio = 1 ) -> None:
        print('Rotating camera init')
        self.gear_ratio = gear_ratio
        self.servo_driver = Servo.Servo(dev_name='servo',channel=0,op_freq=100,Theta_max=135,Theta_min=-135,Theta_center=0)