import arcade
import arcade.key
 
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

 
class TankBattleWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.BLACK)

        self.tank_sprite = arcade.Sprite('images/tank.png')
        self.tank_sprite.set_position(50,50)
        self.bird_sprite = arcade.Sprite('images/bird.png')
        self.bird_sprite.set_position(300,20)
        self.wall_sprite = arcade.Sprite('images/stonewall.png')
        self.wall_sprite.set_position(240,20)


    def on_draw(self):
        arcade.start_render()
 
        self.tank_sprite.draw()
        self.bird_sprite.draw()
        self.wall_sprite.draw()
 
def main():
    window = TankBattleWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()
 
if __name__ == '__main__':
    main()
