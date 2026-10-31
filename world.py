from region import Region
from ball import Ball
import time
import random

class World:
    def __init__(self):
        self.regions = [Region(5)]
        self.balls = [Ball(400, 50, 13)]

        self.last_update = time.perf_counter()
        self.resting_threshold = 5


    def update_world(self):
        current_time = time.perf_counter()
        dt = current_time - self.last_update
        self.last_update = current_time

        for ball in self.balls:
            # Check for collision with left wall
            if ball.edge_left <= self.regions[0].left_wall:
                ball.collide_wall()
                ball.x = self.regions[0].left_wall + ball.radius

            # Check for collision with right wall
            elif ball.edge_right >= self.regions[0].right_wall:
                ball.collide_wall()
                ball.x = self.regions[0].right_wall - ball.radius

            # Check for collision with top wall
            elif ball.edge_up <= self.regions[0].roof:
                ball.collide_floor()
                ball.y = self.regions[0].roof + ball.radius

            if not ball.resting:
                if ball.in_air(self.regions[0].floor):
                    ball.apply_gravity(700, dt)

                # Check for collision with floor
                elif ball.vel_y > self.resting_threshold:
                    ball.collide_floor()
                    self.spawn_new_ball()
                    ball.y = self.regions[0].floor - ball.radius
                    

                # Ball is on floor with low velocity
                elif ball.vel_y > -self.resting_threshold:
                    ball.resting = True
                    continue 


            ball.update_position(dt)

    def spawn_new_ball(self):
        if len(self.balls) < 10:
            self.balls.append(Ball(random.randint(self.regions[0].left_wall + 50, self.regions[0].right_wall - 50), random.randint(30, 500), 
                                              random.randint(12, 15)))
