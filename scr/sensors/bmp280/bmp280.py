import board
import busio
import adafruit_bmp280

def read_data():
    i2c = busio.I2C(board.SCL, board.SDA)
    # Specify the correct I2C address 
    sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)

    # Set the sea level pressure (hPa) at your location for accurate altitude readings
    sensor.sea_level_pressure = 1013.25

    temperature = sensor.temperature
    pressure = sensor.pressure
    altitude = sensor.altitude
    
    return temperature, pressure, altitude

if __name__=="__main__":
    while True:
        temperature, pressure, altitude= read_data()
    
        print(f"Temperature: {temperature:.2f} C")
        print(f"Pressure: {pressure:.2f} hPa")
        print(f"Altitude: {altitude:.2f} m")
