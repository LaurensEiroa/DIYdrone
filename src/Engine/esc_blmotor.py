import time
from adafruit_pca9685 import PCA9685
import board
import busio

# Initialize PCA9685
i2c = busio.I2C(board.SCL, board.SDA)
pca = PCA9685(i2c)
pca.frequency = 50  # 50Hz PWM (critical for ESCs)

# Assign ESC to a PCA9685 channel (e.g., channel 0)
esc_channel = pca.channels[0]





def throttle_to_pulse(throttle_percent):
    throttle = max(0, min(100, throttle_percent))
    return int(1000 + (throttle / 100) * 1000)

def pulse_to_duty(pulse_us):
    return int((pulse_us / 20000) * 0xFFFF)

def set_motor_speed(channel, throttle_percent):
    pulse_us = throttle_to_pulse(throttle_percent)
    duty = pulse_to_duty(pulse_us)
    channel.duty_cycle = duty
    print(f"Throttle: {throttle_percent}% → Pulse: {pulse_us}µs → Duty: {duty}")

try:
    # Arm the ESC (send 0% throttle for 2 seconds)
    set_motor_speed(esc_channel, 0)
    print("Arming ESC...")
    time.sleep(2)

    # Test motor control
    for throttle in [0, 25, 50, 75, 100]:
        set_motor_speed(esc_channel, throttle)
        time.sleep(3)

    # Stop motor
    set_motor_speed(esc_channel, 0)

except KeyboardInterrupt:
    set_motor_speed(esc_channel, 0)
    pca.deinit()








########## ADVANCED 

def ramp_throttle(channel, start, end, duration=5):
    for throttle in range(start, end + 1):
        set_motor_speed(channel, throttle)
        time.sleep(duration / (end - start))

ramp_throttle(esc_channel, 0, 50, duration=5)  # Smoothly ramp to 50% over 5 seconds