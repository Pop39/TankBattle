import arcade
from model import World
 
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
 
        super().__init__(*args, **kwargs)
 
    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
 
    def draw(self):
        self.sync_with_model()
        super().draw() 

class TankBattleWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)
        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.tank_sprite = ModelSprite('images/tank.png', model=self.world.tank)
        self.bird_sprite = arcade.Sprite('images/bird.png')
        self.bird_sprite.set_position(300,20)
        self.wall_sprite = arcade.Sprite('images/stonewall.png')
        self.wall_sprite.set_position(240,20)

    def update(self, delta):
        self.world.update(delta)

    def on_draw(self):
        arcade.start_render()
 
        self.tank_sprite.draw()
        self.bird_sprite.draw()
        self.wall_sprite.draw()

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def on_key_release(self, key, key_modifiers):
        self.world.on_key_release(key, key_modifiers)
 
def main():
    window = TankBattleWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()
