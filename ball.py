class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

        self.vel_x = 0
        self.vel_y = 0

    def update_position(self):
        self.x += self.vel_x
        self.y += self.vel_y

    def update_velocity(self):
        self.vel_y += 0.03
