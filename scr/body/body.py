import time

def get_current_time():
    return time.time()

class Body:
    def __init__(self,a = (0,0,0),vr = (0,0,0)):
        t = get_current_time()
        self.accel_hist = [(a[0],a[1],a[2],t)] #(ax,ay,az,t)
        self.gyro_hist = [(vr[0],vr[1],vr[2],t)] #(vx,vy,vz,t)
        self.r = None

    def set_sensor_readings(self,a,vr):
        t = get_current_time()
        self.accel_hist.append((a[0],a[1],a[2],t))
        self.accel_hist.append((vr[0],vr[1],vr[2],t))
