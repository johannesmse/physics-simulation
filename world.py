from region import Region
from ball import Ball

class World:
    def __init__(self):
        self.regions = [Region(5)]
        self.balls = [Ball(300, 300, 20)]