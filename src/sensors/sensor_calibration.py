
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
    for _ in _samples:
        t0 = time.time()
        acceleration.append(mpu.acceleration)
        delta_t = time.time()-t0
        if delta_t>=1/1000:
            continue
        else:
            time.sleep(hz-delta_t)
    
    print(f"end: {time.time()}")
    np.savetxt("data/accelerometer_data.txt",np.asanyarray(acceleration))

if __name__=="__main__":
    read_samples()