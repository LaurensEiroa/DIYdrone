import asyncio
import websockets

try:
    from config import Config
    from src.picamera.picamera import Camera
    from src.sensors.mpu6050.mpu6050 import read_rata as read_mpu
    from src.sensors.bmp280.bmp280 import read_rata as read_bmp
except ModuleNotFoundError:
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from config import Config
    from src.picamera.picamera import Camera
    from src.sensors.mpu6050.mpu6050 import read_rata as read_mpu
    from src.sensors.bmp280.bmp280 import read_rata as read_bmp


class Client:
    def __init__(self, address="0.0.0.0", port=Config.WEBSOCKET_PORT):
        self.address = address
        self.port = port

        # TODO
        # self.cam = Camera()

        
    async def start_server(self):
        server = await websockets.serve(lambda ws: self.handler(ws), self.address, self.port)
        print(f"WebSocket server on pi Zero is running on ws://{self.address}:{self.port}")
        await asyncio.Future()  # Run forever

    async def handler(self, websocket):
        print("Client connected")
        async for message in websocket:
            print(f"Received message: {message}")
            answer = await self.message_processor(message)
            await websocket.send(f"{answer}")

    async def message_processor(self, message):
        match message:
            # Sensor Readings
            case "read_bmp":
                temperature, pressure, altitude = read_bmp()
                return f"{temperature} - {pressure} - {altitude}"
            
            case "read_mpu":
                acceleration, gyro, temperature = read_mpu()
                return f"{acceleration} - {gyro} - {temperature}"
            

if __name__ == "__main__":
    cli = Client()
    asyncio.run(cli.start_server())
