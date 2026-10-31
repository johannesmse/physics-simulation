class Region:
    def __init__(self, gravity):
        self.gravity = gravity

        self.x = 200
        self.y = 10
        self.width = 400
        self.height = 750

        self.floor = self.y + self.height