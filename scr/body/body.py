import time

def get_current_time():
    return time.time()

class Body:
    def __init__(self,a = (0,0,0),vr = (0,0,0)):
        t = get_current_time()
        self.accel_hist = [(a[0],a[1],a[2],t)] #(ax,ay,az,t)
        self.gyro_hist = [(vr[0],vr[1],vr[2],t)] #(vx,vy,vz,t)
        self.r = [(0,0,0,t)]
        self.v = [(0,0,0,t)]
        self.orientation = [(0,0,0,t)]

    def set_sensor_readings(self,a,vr):
        t = get_current_time()
        self.accel_hist.append((a[0],a[1],a[2],t))
        self.gyro_hist.append((vr[0],vr[1],vr[2],t))

    def set_position(self):
        #r(t) = r0 + v(t)*t +0.5*a(t)*t*r
        r0 = self.r[-1][:3]
        a_current = self.accel_hist[-1][:3]
        delta_t = self.accel_hist[-1][-1] - self.accel_hist[-2][-1]
        v_current = self.v[-1][:3] + a_current*delta_t
        r_current = r0 + v_current * delta_t + 0.5 * a_current * delta_t * delta_t

        self.r.append((r_current[0],r_current[1],r_current[2],self.accel_hist[-1][-1]))
        self.v.append((v_current[0],v_current[1],v_current[2],self.accel_hist[-1][-1]))

    def set_orientation(self):
        delta_t = self.gyro_hist[-1][-1] - self.gyro_hist[-2][-1]
        current_orientation = self.orientation[-1][:3] + self.gyro_hist[-1][:3]*delta_t
        self.orientation.append((current_orientation[0],current_orientation[1],current_orientation[2],self.gyro_hist[-1][-1]))


if __name__=="__main__":
    print("Hello world")