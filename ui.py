import pygame
from world import World

class UI:
    def __init__(self, screen, world):
        self.screen = screen
        self.world = world
        

        self.region_rectangles = []
        self.init_regions()

        self.grey = (54, 69, 79)
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.purple = (128, 0, 128)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)

        self.color_array = [self.white, self.black, self.purple, self.red, self.green, self.blue]

    def add_region_rect(self, region):
        """
        Creates a rectangle object that corresponds to a Region object that can be drawn
        """
        self.region_rectangles.append(
            pygame.Rect(region.x, 
                        region.y, 
                        region.width,
                        region.height))

    def init_regions(self):
        for region in self.world.regions:
            self.add_region_rect(region)

    def draw_regions(self):
        for rect in self.region_rectangles:
            pygame.draw.rect(self.screen, self.grey, rect)

    def draw_balls(self):
        for ball in self.world.balls:
            pygame.draw.circle(self.screen, self.color_array[ball.color], (ball.x, ball.y), ball.radius)



    def draw(self):
        self.screen.fill(self.black)
        self.draw_regions()
        self.draw_balls()

