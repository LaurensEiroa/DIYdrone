import time
import board
import busio
from adafruit_pca9685 import PCA9685
from scr.Engine.motor import BLMotor

class PWM:
    def __init__(self,motors):
        # Create the I2C bus interface
        self.i2c = busio.I2C(board.SCL, board.SDA)

        # Create a PCA9685 object
        self.pca = PCA9685(self.i2c)

        self.motors = motors

        self.set_pwm_frequency()
        pass

    # Function to set the PWM frequency for a specific channel
    def set_pwm_frequency(self):
        for motor in self.motors:
            self.pca.channels[motor.get_channel()].frequency = motor.get_frequency()

    # Function to set the PWM duty cycle for a specific channel
    def set_pwm_duty_cycle(self):
        for motor in self.motors:
            self.pca.channels[motor.get_channel()].duty_cycle = int(motor.get_duty_cycle() * 65535 / 100)

def test():
    motor = [BLMotor(channel=4,frequency=50)]
    pwm = PWM(motors=motor)

    motor[0].set_duty_cycle(10)
    pwm.set_pwm_duty_cycle() 

    motor[0].set_duty_cycle(20)
    pwm.set_pwm_duty_cycle()
    time.sleep(5)

    motor[0].set_duty_cycle(0)
    pwm.set_pwm_duty_cycle()
    time.sleep(5)

if __name__=="__main__":
    test