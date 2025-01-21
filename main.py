import asyncio
from src.coms.websocket.websocket_client import run
from src.Engine.pwm import test as test_motor
from src.sensors.mpu6050.mpu6050 import read_rata as read_data_mpu
from src.picamera.picamera import Camera
from src.coms.udp.udp_sender import UDPSender
from config import Config


def data_to_string(data):
    return "//".join(data)


async def run():
    camera = Camera()
    
    sender = 'piZero4'  # Replace with your sender IP address
    receiver = 'ubuntu_laptop'  # Replace with your receiver IP address

    udp_data_sender = UDPSender(sender_ip=Config.IPs[sender], receiver_ip=Config.IPs[receiver], port=Config.UDP_DATA_PORT)
    udp_frame_sender = UDPSender(sender_ip=Config.IPs[sender], receiver_ip=Config.IPs[receiver], port=Config.UDP_DATA_PORT)

    while True:
        frame = camera.get_frame()
        a,g,t = read_data_mpu()
        data = data_to_string(g)
        await asyncio.gather(
            udp_frame_sender.send_data(frame,data_type="frame"),
            udp_data_sender.send_data(data,data_type="data")
        )

if __name__=="__main__":
    asyncio.get_event_loop().run_until_complete(run())


