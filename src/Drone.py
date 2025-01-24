
import numpy as np
from config import Config

from src.picamera.picamera import Camera
from src.sensors.mpu6050.mpu6050 import read_rata as read_mpu
from src.sensors.bmp280.bmp280 import read_data as read_bmp

import asyncio

class Drone:
    def __init__(self,length_width_height = [90,60,20]):
        self.length_width_height = np.asarray(length_width_height)

        self.camera = Camera(resolution=(307,173))
        self.frame = self.set_frame()

        self.position = np.zeros((3))
        self.angle = np.zeros((3))
        self.initial_position = np.zeros((3))
        self.initial_angle = np.zeros((3))

        self.initialize_sensors()

        self.edges = np.asarray([[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], 
                                 [5, 6], [6, 7], [7, 4], [0, 4], [1, 5], 
                                 [2, 6], [3, 7], 
                                 [8, 9], [8, 10], [8, 11]])
        self.body_coordinates = self.set_body_coordinates()

    def initialize_sensors(self,steps = 20):
        print("initializing sensors")
        initial_angle = np.zeros((steps,3))
        initial_height = np.zeros(steps)
        for i in range(steps):
            acc, gyr, t  = read_mpu(angle=True)
            gyr_data_processed = self.drone_coords_to_3d_coords(gyr)
            initial_angle[i,:] = gyr_data_processed

            t, p, h = read_bmp()
            initial_height[i] = h

        self.initial_angle = np.mean(initial_angle,axis=0)
        self.initial_position[2] = np.mean(initial_height)
        print(f"initial angle {self.initial_angle}\t initial position {self.initial_position}")


    def set_frame(self):
        self.frame = self.camera.get_frame()

    def get_frame(self):
        return self.frame
    
    def get_data(self):
        text = f"{'//'.join(map(str, self.angle))}$$${'//'.join(map(str, self.position))}"
        return text


    def process_sensor_readings(self):
        # MPU
        #print(f"reading mpu")
        acc, gyr, t  = read_mpu(angle=True)
        gyr_data_processed = self.drone_coords_to_3d_coords(gyr)
        self.update_orientation(gyr_data_processed)
        
        #print(f"reading bmp")
        t, p, h = read_bmp()
        self.update_heigth(h)
        

    def drone_coords_to_3d_coords(self, gyro_readings):
        return np.asarray([-gyro_readings[1],gyro_readings[0],gyro_readings[2]])
    
    def update_orientation(self,rotation_3d_frame):
        self.angle += rotation_3d_frame-self.initial_angle # TODO += or = ??
        #print(f"new angle {self.angle}")

    def update_heigth(self,h):
        self.position[2] = h-self.initial_position[2]

    def apply_rotation(self,vectors):
        x_rotation = np.asarray([   [1,   0,                        0                     ],
                                    [0,   np.cos(self.angle[0]),    -np.sin(self.angle[0]) ],
                                    [0,   np.sin(self.angle[0]),    np.cos(self.angle[0]) ]
        ])
        y_rotation = np.asarray([   [np.cos(self.angle[1]), 0,  np.sin(self.angle[1]) ],
                                    [0,                     1,  0                     ],
                                    [-np.sin(self.angle[1]), 0,  np.cos(self.angle[1]) ]
        ])
        z_rotation = np.asarray([   [np.cos(self.angle[2]), -np.sin(self.angle[2]),    0],
                                    [np.sin(self.angle[2]), np.cos(self.angle[2]),    0],
                                    [0,                       0,                      1]
        ])
        rotated_vectors = []
        for vector in vectors:
            rotated_vector =  z_rotation @ y_rotation @ x_rotation @ vector
            rotated_vectors.append(rotated_vector)
        return np.asarray(rotated_vectors)


    def set_body_coordinates(self):
        axis_length = 30
        # vertices of object
        vertices = np.asarray([
            [-self.length_width_height[0],  -self.length_width_height[1],   self.position[2]],
            [-self.length_width_height[0],  self.length_width_height[1],    self.position[2]],
            [self.length_width_height[0],   self.length_width_height[1],    self.position[2]],
            [self.length_width_height[0],   -self.length_width_height[1],   self.position[2]],
            [-self.length_width_height[0],  -self.length_width_height[1],   self.position[2] + self.length_width_height[2]],
            [-self.length_width_height[0],  self.length_width_height[1],    self.position[2] + self.length_width_height[2]],
            [self.length_width_height[0],   self.length_width_height[1],    self.position[2] + self.length_width_height[2]],
            [self.length_width_height[0],   -self.length_width_height[1],   self.position[2] + self.length_width_height[2]],
            # Drone axes
            [0,             0,              self.position[2] + self.length_width_height[2]],
            [axis_length,   0,              self.position[2] + self.length_width_height[2]],
            [0,             axis_length,    self.position[2] + self.length_width_height[2]],
            [0,             0,              self.position[2] + self.length_width_height[2] + axis_length],
        ])

        self.body_coordinates = self.apply_rotation(vertices)

    async def start_drone(self):
        print("starting loop drone")
        while True:
            # Set drone status
            self.process_sensor_readings()
            #self.set_body_coordinates()

            # Set drone view
            self.set_frame()
            await asyncio.sleep(0)


if __name__=="__main__":
    bot = Drone()
    bot.start_drone()









