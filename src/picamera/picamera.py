import cv2
from picamera2 import Picamera2
from libcamera import Transform

class Camera:
    def __init__(self,resolution=(180,101), format='XRGB8888'):
        # Initialize Picamera2
        self.picam2 = Picamera2()
        self.picam2.configure(self.picam2.create_video_configuration(main={"format": format, "size": resolution})), transform=Transform(rotation=90)
        self.picam2.start()

    def get_frame(self):
        # Capture a frame
        frame = self.picam2.capture_array()
        return frame

    def release(self):
        # Stop the camera
        self.picam2.stop()

if __name__ == "__main__":
    camera = Camera()

    try:
        while True:
            frame = camera.get_frame()
            # Display the frame (optional)
            cv2.imshow("Frame", frame)

            # Exit on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        camera.release()
        cv2.destroyAllWindows()
