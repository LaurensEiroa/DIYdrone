import time
import board
import busio
import adafruit_mpu6050

def read_rata():
    i2c = busio.I2C(board.SCL, board.SDA)
    mpu = adafruit_mpu6050.MPU6050(i2c)

    acceleration = mpu.acceleration
    gyro = mpu.gyro
    temperature = mpu.temperature
    return acceleration,gyro,temperature

if __name__=="__main__":
    while True:
        acceleration, gyro, temperature = read_rata()
        
        print(f"Accel : ({acceleration[0]:.2f} i, {acceleration[1]:.2f} j, {acceleration[2]:.2f} k) m/s^2")
        print(f"Gyro : ({gyro[0]:.2f} i, {gyro[1]:.2f} j, {gyro[2]:.2f} k) rad/s")
        print(f"Temp: {temperature:.2f} C")
    
    time.sleep(1)
