import arcade

class Rocket(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.center_x=game.width//2
        self.center_y=35
        self.change_x=0
        self.change_y=0
        self.width=50
        self.height=10
        self.speed=4
        self.score=0

    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, arcade.color.GRAY)

    def move(self):
        self.center_x += self.change_x*self.speed

        
