class BLMotor:
    def __init__(self, channel, frequency=50):
        self.channel = channel
        self.current_frequency = frequency
        self.current_duty_cycle = 0        

    # Getter for channel
    def get_channel(self):
        return self.channel

    # Setter for current_frequency
    def set_frequency(self, frequency):
        self.current_frequency = frequency
    # Setter for current_duty_cycle
    def set_duty_cycle(self, duty_cycle):
        self.current_duty_cycle = duty_cycle
        
    # Getter for current_frequency
    def get_frequency(self):
        return self.current_frequency
    # Getter for current_duty_cycle
    def get_duty_cycle(self):
        return self.current_duty_cycle

