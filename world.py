from region import Region
from ball import Ball

class World:
    def __init__(self):
        self.regions = [Region(5)]
        self.balls = [Ball(400, 30, 20)]


    def update_world(self):
        for ball in self.balls:
            ball.update_position()
            ball.update_velocity()