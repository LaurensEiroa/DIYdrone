import time
from adafruit_pca9685 import PCA9685
import board
import busio

# Initialize PCA9685
i2c = busio.I2C(board.SCL, board.SDA)
pca = PCA9685(i2c)
pca.frequency = 50  # Set PWM frequency to 50Hz (standard for ESCs)

# Define ESC channel (e.g., channel 0)
esc_channel = pca.channels[0]

def set_pulse(channel, pulse_us):
    # Convert microseconds to PCA9685 duty cycle (12-bit resolution)
    duty_cycle = int((pulse_us / 20000) * 0xFFFF)  # 20ms period (50Hz)
    channel.duty_cycle = duty_cycle

try:
    # Step 1: Send max throttle (2000µs)
    print("Disconnect battery, then press Enter.")
    input()
    set_pulse(esc_channel, 2000)
    print("Connect battery NOW. Wait for 2 beeps, then press Enter.")
    input()

    # Step 2: Send min throttle (1000µs)
    set_pulse(esc_channel, 1000)
    print("Wait for confirmation beeps (may take a few seconds).")
    time.sleep(5)

    # Test mid-throttle (1500µs)
    set_pulse(esc_channel, 1500)
    time.sleep(2)
    set_pulse(esc_channel, 1000)
    print("Calibration done!")

except KeyboardInterrupt:
    set_pulse(esc_channel, 0)
    pca.deinit()