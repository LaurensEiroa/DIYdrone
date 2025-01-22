import asyncio
from src.coms.websocket.websocket_client import run
from src.coms.udp.udp_sender import UDPSender
from src.Drone import Drone
from config import Config


def data_to_string(data):
    return "//".join(map(str,data))


async def run():

    drone = Drone()
    
    sender = Config.SENDER  # Replace with your sender IP address
    receiver = Config.RECIEVER  # Replace with your receiver IP address

    udp_data_sender = UDPSender(sender_ip=Config.IPs[sender], receiver_ip=Config.IPs[receiver], port=Config.UDP_DATA_PORT, obj=drone)
    udp_frame_sender = UDPSender(sender_ip=Config.IPs[sender], receiver_ip=Config.IPs[receiver], port=Config.UDP_FRAME_PORT, obj=drone)

    
    await asyncio.gather(
            drone.start_drone(),
            udp_data_sender.run_udp("data"),
            udp_frame_sender.run_udp("frame"),
        )

if __name__=="__main__":
    asyncio.run(run())


