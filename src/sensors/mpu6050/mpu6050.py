import time
import board
import busio
import adafruit_mpu6050

def read_rata(angle=False):
    i2c = busio.I2C(board.SCL, board.SDA)
    mpu = adafruit_mpu6050.MPU6050(i2c)
    if angle:
        acceleration = mpu.acceleration
        t1 = time.time()
        gyro = mpu.gyro
        t2 = time.time()
        temperature = mpu.temperature
        gx,gy,gz = gyro[0],gyro[1],gyro[2]
        gyro = (float(gx)*(t2-t1),float(gy)*(t2-t1),float(gz)*(t2-t1))
        return acceleration,gyro,temperature
    t0 = time.time()
    acceleration = mpu.acceleration
    t1 = time.time()
    gyro = mpu.gyro
    t2 = time.time()
    temperature = mpu.temperature
    return acceleration,gyro,temperature

def test():
    while True:
        acceleration, gyro, temperature = read_rata()
        
        #print(f"Accel : ({acceleration[0]:.2f} i, {acceleration[1]:.2f} j, {acceleration[2]:.2f} k) m/s^2")
        print(f"Gyro : ({gyro[0]:.2f} i, {gyro[1]:.2f} j, {gyro[2]:.2f} k) rad/s")
        #print(f"Temp: {temperature:.2f} C")
        time.sleep(0.5)

if __name__=="__main__":
    test()
    
