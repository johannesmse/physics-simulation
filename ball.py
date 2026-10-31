import random

class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

        self.vel_x = 300
        self.vel_y = 100
        self.resting = False

        self.color = random.randint(1, 5)
        

    @property
    def edge_down(self):
        return self.y + self.radius

    @property
    def edge_left(self):
        return self.x - self.radius

    @property
    def edge_right(self):
        return self.x + self.radius

    @property
    def edge_up(self):
        return self.y - self.radius

    def in_air(self, floor):
        return self.edge_down <= floor

    def update_position(self, dt):
        self.x += self.vel_x * dt
        if not self.resting:
            self.y += self.vel_y * dt


    def apply_gravity(self, gravity, dt):
        self.vel_y += gravity * dt

    def collide_floor(self):
        self.vel_y = -0.7 * self.vel_y
        self.change_color()

    def collide_wall(self):
        self.vel_x = -1 * self.vel_x
        self.change_color()

    def change_color(self):
        new_color = random.randint(1, 5)
        while new_color == self.color:
            new_color = random.randint(1, 5)

        self.color = new_color

