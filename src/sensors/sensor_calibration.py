
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
    t0 = time.time()
    for i in _samples:
        acceleration.append(mpu.acceleration)
    tf = time.time()
    print(f"total time: {tf-t0}, frequency: {(tf-t0)/samples}")
    np.savetxt("data/accelerometer_data.txt",np.asarray(acceleration))

if __name__=="__main__":
    read_samples()