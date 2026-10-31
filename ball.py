class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

        self.vel_x = 0
        self.vel_y = 0

    @property
    def edge_down(self):
        return self.y + self.radius

    def update_position(self, dt):
        self.x += self.vel_x * dt
        self.y += self.vel_y * dt

    def apply_gravity(self, dt):
        self.vel_y += 700 * dt

    def collide_floor(self):
        if self.vel_y < 1:
            self.vel_y = 0
        else:
            self.vel_y = -0.6 * self.vel_y
