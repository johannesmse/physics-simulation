from region import Region
from ball import Ball
import time

class World:
    def __init__(self):
        self.regions = [Region(5)]
        self.balls = [Ball(400, 30, 20)]

        self.last_update = time.perf_counter()


    def update_world(self):
        dt = time.perf_counter() - self.last_update
        self.last_update = time.perf_counter()

        for ball in self.balls:
            ball.update_position(dt)
            ball.update_velocity(dt)