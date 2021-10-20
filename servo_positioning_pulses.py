import RotatingCamera
import sys

try:
    pulses = int(sys.argv[1])
    camera = RotatingCamera.RotatingCamera(gear_ratio=2.0)

    if(pulses > camera.servo_driver.T_max_counts):
        pulses = camera.servo_driver.T_max_counts
    if(pulses < camera.servo_driver.T_min_counts):
        pulses = camera.servo_driver.T_min_counts
    print('Pulses: {}'.format(pulses))
    camera.servo_driver.set_raw_position(pulses)
except Exception as e:
    print(e)
    raise SystemExit