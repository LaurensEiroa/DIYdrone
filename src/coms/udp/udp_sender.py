import socket
import cv2
from config import Config
import asyncio

class UDPSender:
    def __init__(self, sender_ip, receiver_ip, port,obj):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.server_socket.bind((sender_ip, port))
        self.receiver_address = (receiver_ip, port)

        self.object = obj

    async def send_data(self, data_type="data"):
        if data_type == "frame":
            data = self.object.get_frame()
            encoded, buffer = cv2.imencode('.jpg', data)
            buffer = buffer.tobytes()
            MAX_DGRAM = Config.MAX_DGRAM_FRAME
        elif data_type == "data":
            data = self.object.get_data()
            buffer = data.encode('utf-8')
            MAX_DGRAM = Config.MAX_DGRAM_DATA
        size = len(buffer)
        print(f"sending {data_type} buffer length: {size}\t\t{data}")
        for i in range(0, size, MAX_DGRAM):
            self.server_socket.sendto(buffer[i:i+MAX_DGRAM], self.receiver_address)
        # Send a delimiter to indicate the end of the frame
        self.server_socket.sendto(b'END', self.receiver_address)

    async def run_udp(self):
        while True:
            await self.send_data(data_type="data")