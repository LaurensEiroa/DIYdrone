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

    udp_data_sender = UDPSender(sender_ip=Config.IPs[sender], receiver_ip=Config.IPs[receiver], port=Config.UDP_DATA_PORT,obj=drone)
    #udp_frame_sender = UDPSender(sender_ip=Config.IPs[sender], receiver_ip=Config.IPs[receiver], port=Config.UDP_DATA_PORT)

    
    await asyncio.gather(
            #udp_frame_sender.send_data(frame,data_type="frame"),
            udp_data_sender.send_data(data_type="data"),
            drone.start_drone()
        )

if __name__=="__main__":
    asyncio.get_event_loop().run_until_complete(run())


