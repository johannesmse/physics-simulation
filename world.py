from region import Region
from ball import Ball
import time

class World:
    def __init__(self):
        self.regions = [Region(5)]
        self.balls = [Ball(400, 30, 20), Ball(300, 100, 20), Ball(250, 80, 20), Ball(450, 200, 20), Ball(500, 50, 20)]

        self.last_update = time.perf_counter()
        self.resting_threshold = 5


    def update_world(self):
        current_time = time.perf_counter()
        dt = current_time - self.last_update
        self.last_update = current_time

        for ball in self.balls:
            if ball.edge_left <= self.regions[0].left_wall:
                ball.collide_wall()
                ball.x = self.regions[0].left_wall + ball.radius

            elif ball.edge_right >= self.regions[0].right_wall:
                ball.collide_wall()
                ball.x = self.regions[0].right_wall - ball.radius

            if not ball.resting:
                if ball.in_air(self.regions[0].floor):
                    ball.apply_gravity(700, dt)

                # Ball is colliding with floor
                elif ball.vel_y > self.resting_threshold:
                    ball.collide_floor()

                # Ball is on floor with low velocity
                elif ball.vel_y > -self.resting_threshold:
                    ball.resting = True
                    continue 


            ball.update_position(dt)