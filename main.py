import asyncio
from src.websocket.websocket_client import run
from src.Engine.pwm import test as test_motor
from src.sensors.mpu6050.mpu6050 import test as test_mpu

if __name__=="__main__":

    #run()
    #print("starting test")
    test_mpu()
