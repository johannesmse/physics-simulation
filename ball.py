class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

        self.vel_x = 0
        self.vel_y = 0

    def update_position(self, dt):
        self.x += self.vel_x * dt
        self.y += self.vel_y * dt

    def update_velocity(self, dt):
        self.vel_y += 500 * dt
