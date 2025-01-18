import board
import busio
import adafruit_bmp280

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_bmp280.Adafruit_BMP280_I2C(i2c)

# Set the sea level pressure (hPa) at your location for accurate altitude readings
sensor.sea_level_pressure = 1013.25

while True:
    temperature = sensor.temperature
    pressure = sensor.pressure
    altitude = sensor.altitude
    
    print(f"Temperature: {temperature:.2f} C")
    print(f"Pressure: {pressure:.2f} hPa")
    print(f"Altitude: {altitude:.2f} m")
