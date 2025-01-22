import time
import board
import busio
from adafruit_pca9685 import PCA9685
from src.Engine.motor import BLMotor

class PWM:
    def __init__(self,motors):
        # Create the I2C bus interface
        self.i2c = busio.I2C(board.SCL, board.SDA)

        # Create a PCA9685 object
        self.pca = PCA9685(self.i2c)

        self.motors = motors

        self.pca.frequency = motors[0].get_frequency()
        pass

    # Function to set the PWM duty cycle for a specific channel
    def set_pwm_duty_cycle(self):
        for motor in self.motors:
            self.pca.channels[motor.get_channel()].duty_cycle = int(motor.get_duty_cycle() * 65535 / 100)

def test():
    motors_number=5
    print("loading motor")
    motor = [BLMotor(channel=i,frequency=60) for i in range(motors_number)]
    print("motor_created")
    pwm = PWM(motors=motor)
    print("pwm set 0")
    for i in range(motors_number):
        motor[i].set_duty_cycle(0)
    pwm.set_pwm_duty_cycle() 
    time.sleep(10)

    print("pwm set 50")
    for i in range(motors_number):
        motor[i].set_duty_cycle(50)
    pwm.set_pwm_duty_cycle()
    time.sleep(10)

    print("pwm set 100")
    for i in range(motors_number):
        motor[i].set_duty_cycle(100)
    pwm.set_pwm_duty_cycle()
    time.sleep(10)

    
    print("pwm set 0")
    for i in range(motors_number):
        motor[i].set_duty_cycle(0)
    pwm.set_pwm_duty_cycle() 
    time.sleep(10)

if __name__=="__main__":
    test()