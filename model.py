class Tank:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
 
    def update(self, delta):
        if self.x > self.world.width:
            self.x = 0
        self.x += 5

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
        self.tank = Tank(self, 50, 50)
 
 
    def update(self, delta):
        self.tank.update(delta)
