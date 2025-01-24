
import time
import board
import busio
import adafruit_mpu6050
import numpy as np



def read_samples(samples=1000):
    i2c = busio.I2C(board.SCL, board.SDA)
    mpu = adafruit_mpu6050.MPU6050(i2c)
    _samples = range(samples)
    acceleration = []
    hz = 1/samples
    print(f"start: {time.time()}")
    t0 = time.time()
    for i in _samples:
        acceleration.append(mpu.acceleration)
        if time.time() - t0-i*0.001>=0.001:
            continue
        else:
            print("once")
            time.sleep(time.time() - t0-i*0.001)
    
    print(f"end: {time.time()}")
    np.savetxt("data/accelerometer_data.txt",np.asanyarray(acceleration))

if __name__=="__main__":
    read_samples()