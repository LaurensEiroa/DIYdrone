import socket
import cv2
from config import Config
import asyncio



class UDPSender:
    def __init__(self, sender_ip, receiver_ip, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.server_socket.bind((sender_ip, port))
        self.receiver_address = (receiver_ip, port)

    async def send_data(self,data,data_type="image"):
        print(f"sending {data_type}")
        if data_type=="frame": 
            encoded, buffer = cv2.imencode('.jpg', data)
            buffer = buffer.tobytes()
            MAX_DGRAM = Config.MAX_DGRAM_FRAME
        elif data_type=="data":
            buffer = data.encode('utf-8')
            MAX_DGRAM = Config.MAX_DGRAM_DATA        
        size = len(buffer)
        for i in range(0, size, MAX_DGRAM):
            self.server_socket.sendto(buffer[i:i+MAX_DGRAM], self.receiver_address)

async def run():
    # Capture video from the default camera
    sender = 'piZero4'  # Replace with your sender IP address
    receiver = 'ubuntu_laptop'  # Replace with your receiver IP address

    udp_data_sender = UDPSender(sender_ip=Config.IPs[sender], receiver_ip=Config.IPs[receiver], port=Config.UDP_DATA_PORT)
    #udp_frame_sender = UDPSender(sender_ip=Config.IPs[sender], receiver_ip=Config.IPs[receiver], port=Config.UDP_DATA_PORT)

    cap = cv2.VideoCapture(0)
    data = "Hello from the drone!"
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        data = data[::-1]
        await asyncio.gather(
            #udp_frame_sender.send_data(frame,data_type="frame"),
            udp_data_sender.send_data(data,data_type="data")
        )
    cap.release()

if __name__=="__main__":
    asyncio.get_event_loop().run_until_complete(run())
