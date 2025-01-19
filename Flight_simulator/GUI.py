import pygame
import math

class FlightSimulator:
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True

        # Colors
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)

    def draw_axes(self):
        center = (400, 300)
        length = 200

        # Draw X axis (red)
        pygame.draw.line(self.screen, self.red, center, (center[0] + length, center[1]), 2)
        #pygame.draw.line(self.screen, self.red, center, (center[0] - length, center[1]), 2)
        pygame.draw.line(self.screen, self.red, (center[0] + length, center[1]), (center[0] + length - 10, center[1] - 10), 2)
        pygame.draw.line(self.screen, self.red, (center[0] + length, center[1]), (center[0] + length - 10, center[1] + 10), 2)

        # Draw Y axis (green)
        pygame.draw.line(self.screen, self.green, center, (center[0], center[1] - length), 2)
        #pygame.draw.line(self.screen, self.green, center, (center[0], center[1] + length), 2)
        pygame.draw.line(self.screen, self.green, (center[0], center[1] - length), (center[0] - 10, center[1] - length + 10), 2)
        pygame.draw.line(self.screen, self.green, (center[0], center[1] - length), (center[0] + 10, center[1] - length + 10), 2)

        # Draw Z axis (blue)
        #pygame.draw.line(self.screen, self.blue, center, (center[0] + length // 2, center[1] - length // 2), 2)
        pygame.draw.line(self.screen, self.blue, center, (center[0] - length // 2, center[1] + length // 2), 2)
        pygame.draw.line(self.screen, self.blue, (center[0] - length // 2, center[1] - length // 2), (center[0] - length // 2 - 10, center[1] - length // 2 + 10), 2)
        pygame.draw.line(self.screen, self.blue, (center[0] - length // 2, center[1] - length // 2), (center[0] - length // 2 + 10, center[1] - length // 2 - 10), 2)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Clear screen
            self.screen.fill((0, 0, 0))

            # Draw axes
            self.draw_axes()

            # Update display
            pygame.display.flip()

            # Control frame rate
            self.clock.tick(60)  # Run at 60 frames per second

        pygame.quit()
if __name__=="__main__":
    # Create an instance of the FlightSimulator class and run it
    simulator = FlightSimulator()
    simulator.run()
