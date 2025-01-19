from scr.sensors.bmp280.bmp280 import read_data as read_bmp
from scr.sensors.mpu6050.mpu6050 import read_rata as read_imu
import time

if __name__=="__main__":
    while True:
        temperature, pressure, altitude= read_bmp()
    
        print(f"Temperature: {temperature:.2f} C")
        print(f"Pressure: {pressure:.2f} hPa")
        print(f"Altitude: {altitude:.2f} m")
        acceleration, gyro, temperature = read_imu()
        print(f"Accel : ({acceleration[0]:.2f} i, {acceleration[1]:.2f} j, {acceleration[2]:.2f} k) m/s^2")
        print(f"Gyro : ({gyro[0]:.2f} i, {gyro[1]:.2f} j, {gyro[2]:.2f} k) rad/s")
        print(f"Temp: {temperature:.2f} C")
        time.sleep(5)

