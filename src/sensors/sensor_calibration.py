
import time
import board
import busio
import adafruit_mpu6050
import numpy as np
from scipy.signal import butter, filtfilt



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

def process_data():
    import matplotlib.pyplot as plt
    path= "/home/laurens/Descargas/accelerometer_data.txt"
    data = np.loadtxt(path)
    samples = 1000
    sample_rate = 0.001933177947998047

    t = np.linspace(0,samples*sample_rate,samples,endpoint=False)
    print(f"time: {t[1]-t[0]}")
    plt.figure("data plot")
    plt.plot(t,data)


    yf = np.fft.fft(data[:,0])
    xf = np.fft.fftfreq(samples, sample_rate)[:samples//2]


    plt.figure("Frequency Domain Signal a_x")
    plt.plot(xf, 2.0/samples * np.abs(yf[:samples//2]))
    plt.grid()
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")




    plt.show()


if __name__=="__main__":
    #read_samples()
    process_data()