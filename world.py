from region import Region
from ball import Ball
import time

class World:
    def __init__(self):
        self.regions = [Region(5)]
        self.balls = [Ball(400, 30, 20)]

        self.last_update = time.perf_counter()


    def update_world(self):
        current_time = time.perf_counter()
        dt = current_time - self.last_update
        self.last_update = current_time

        for ball in self.balls:
            if ball.edge_down <= self.regions[0].floor:
                ball.apply_gravity(dt)
                ball.update_position(dt)
            elif ball.vel_y > 10:
                ball.collide_floor()
                ball.update_position(dt)
            elif ball.vel_y > 10 or ball.vel_y < -10:
                ball.update_position(dt)

            