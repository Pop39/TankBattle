import arcade

DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4

DIR_KEYSET = { arcade.key.UP:DIR_UP,
               arcade.key.RIGHT:DIR_RIGHT,
               arcade.key.DOWN:DIR_DOWN,
               arcade.key.LEFT:DIR_LEFT}

DIR_KEYSET2 = { arcade.key.W:DIR_UP,
                arcade.key.D:DIR_RIGHT,
                arcade.key.S:DIR_DOWN,
                arcade.key.A:DIR_LEFT}
 
DIR_OFFSET = { DIR_UP: (0,1),
               DIR_RIGHT: (1,0),
               DIR_DOWN: (0,-1),
               DIR_LEFT: (-1,0) }

class Tank:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.direction = 0
        self.wait_time = 0
        self.dir_x = 0
        self.dir_y = 0
        self.current_direction = 0 

    def update(self, delta):
        self.wait_time = 0
        if (self.direction != 0):
            self.dir_x = DIR_OFFSET[self.direction][0]
            self.dir_y = DIR_OFFSET[self.direction][1]
            self.x += self.dir_x
            self.y += self.dir_y
            self.current_direction = self.direction

        elif (self.direction == 0):
            self.dir_x = 0
            self.dir_y = 0
            self.x += self.dir_x
            self.y += self.dir_y

class Tank2:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.direction = 0
        self.wait_time = 0
        self.dir_x = 0
        self.dir_y = 0
        self.current_direction = 0 

    def update(self, delta):
        self.wait_time = 0
        if (self.direction != 0):
            self.dir_x = DIR_OFFSET[self.direction][0]
            self.dir_y = DIR_OFFSET[self.direction][1]
            self.x += self.dir_x
            self.y += self.dir_y
            self.current_direction = self.direction

        elif (self.direction == 0):
            self.dir_x = 0
            self.dir_y = 0
            self.x += self.dir_x
            self.y += self.dir_y

class Bullet:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.list = []
        self.dir_x = 0
        self.dir_y = 0
        self.b_speed = 3
        self.create_bullet = False

    def update(self, delta):
        self.wait_time = 0
        self.createbullet(self.world.tank.current_direction, self.world.tank.x, self.world.tank.y)

    def createbullet(self, tankCurDi, tankX, tankY):
        if self.create_bullet==True:
           self.list.insert(len(self.list),(tankX,tankY))
           while self.dir_x < 600 and self.dir_y < 600: 
                 self.dir_x = self.b_speed * DIR_OFFSET[tankCurDi][0]
                 self.dir_y = self.b_speed * DIR_OFFSET[tankCurDi][1]
                 self.x += self.dir_x
                 self.y += self.dir_y

WallSize = 50

class Wall:
    def __init__(self, world):
        self.world = world
        self.x = 0
        self.y = 0
        self.list = []
        self.createmap()

    def update(self, delta):
        self.wait_time = 0

    def createmap(self):
        for x in range(WallSize//2*3, self.world.width-(WallSize//2), WallSize):
            for y in range(WallSize//2*3, self.world.height-(WallSize//2), WallSize):
                if ((x > WallSize//2*5) or (y > WallSize//2*5)) and ((x < self.world.width-(WallSize//2*5)) or (y < self.world.width-(WallSize//2*5))):
                    self.list.insert(len(self.list),(x,y))

class Bird:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.list = []

    def update(self, delta):
        self.wait_time = 0

class Bird2:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.list = []

    def update(self, delta):
        self.wait_time = 0

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
        self.tank = Tank(self, 100, 100)
        self.tank2 = Tank2(self, 500, 500)
        self.bullet = Bullet(self, self.tank.x, self.tank.y)
        self.wall = Wall(self)
        self.bird = Bird(self, 30, 30)
        self.bird2 = Bird2(self, 570, 570)
 
    def update(self, delta):
        self.tank.update(delta)
        self.tank2.update(delta)
        self.bullet.update(delta)
        self.wall.update(delta)
        self.bird.update(delta)
        self.bird2.update(delta)


    def on_key_press(self, key, key_modifiers):
        if key in DIR_KEYSET:
            self.tank.direction = DIR_KEYSET[key]
        if key in DIR_KEYSET2:
            self.tank2.direction = DIR_KEYSET2[key]
        #if key == arcade.key.Z and self.bullet.create_bullet == False:
            #self.bullet.create_bullet = True
            

    def on_key_release(self, key, key_modifiers):
        if key in DIR_KEYSET:
            self.tank.direction = 0
        if key in DIR_KEYSET2:
            self.tank2.direction = 0
            self.tank2.direction = 0
