import arcade

DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4

DIR_KEYSET = { arcade.key.UP:DIR_UP,
               arcade.key.RIGHT:DIR_RIGHT,
               arcade.key.DOWN:DIR_DOWN,
               arcade.key.LEFT:DIR_LEFT}
 
DIR_OFFSET = { DIR_UP: (0,1),
               DIR_RIGHT: (1,0),
               DIR_DOWN: (0,-1),
               DIR_LEFT: (-1,0) }

MOVEMENT_SPEED = 2

class Tank:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.direction = 0
        self.wait_time = 0
        self.dir_x = 0
        self.dir_y = 0

    def update(self, delta):
        self.wait_time = 0
        if (self.direction != 0):
            self.dir_x = DIR_OFFSET[self.direction][0]
            self.dir_y = DIR_OFFSET[self.direction][1]
            self.x += self.dir_x
            self.y += self.dir_y
        elif (self.direction == 0):
            self.dir_x = 0
            self.dir_y = 0
            self.x += self.dir_x
            self.y += self.dir_y

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
        self.tank = Tank(self, 50, 50)
 
    def update(self, delta):
        self.tank.update(delta)



    def on_key_press(self, key, key_modifiers):
        if key in DIR_KEYSET:
            self.tank.direction = DIR_KEYSET[key]

    def on_key_release(self, key, key_modifiers):
        if key in DIR_KEYSET:
            self.tank.direction = 0
