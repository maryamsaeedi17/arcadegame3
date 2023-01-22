import arcade
import time

from ball import Ball
from rocket import Rocket
from brick import Brick
from heart import Heart


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=510, height=600, title= "breakout 2023")
        arcade.set_background_color(arcade.color.DARK_BLUE)
        self.rocket=Rocket(self)
        self.ball=Ball(self)
        self.brick_list=[]
        self.color_list=[arcade.color.GRAY, arcade.color.RED, arcade.color.ORANGE, arcade.color.YELLOW]
        self.heart_list = []

        for i in range(4):
            for j in range(17):
                brick=Brick(15+30*j, 500-20*i, self.color_list[i])
                self.brick_list.append(brick)

        for i in range(3):
            heart = Heart(i+1)
            self.heart_list.append(heart)


    def on_draw(self):
        arcade.start_render()
        for brick in self.brick_list:
            brick.draw()

        self.rocket.draw()
        self.ball.draw()

        for heart in self.heart_list:
            heart.draw()

        arcade.draw_text(f"Score: {self.rocket.score}", self.width//10, 580 , arcade.color.WHITE  , bold=True)

        if len(self.heart_list)==0:
            arcade.draw_lrtb_rectangle_filled(0,self.width,self.height,0,arcade.color.BLACK)
            arcade.draw_text("GAME OVER!", self.width//9 , self.height//2 , arcade.color.RED , 40)
            a=time.time()
            if (time.time()-a)>10:
                del self.ball
                del self.rocket

        if len(self.brick_list)==0:
            arcade.draw_text("YOU WIN!!!", self.width//9 , self.height//2 , arcade.color.RED , 40)
            a=time.time()
            if (time.time()-a)>10:
                del self.ball
                del self.rocket



        arcade.finish_render()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if 25 < x < self.width-25:
            self.rocket.center_x=x

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol==arcade.key.RIGHT:
            self.rocket.change_x=1

        if symbol==arcade.key.LEFT:
            self.rocket.change_x=-1

    def on_update(self, delta_time: float):

        self.ball.move()
        self.rocket.move()

        if self.ball.center_x<0 or self.ball.center_x > self.width:
            self.ball.change_x *= -1

        if arcade.check_for_collision(self.ball, self.rocket):
            self.ball.change_y *= -1

        #if arcade.check_for_collision_with_list()

        for brick in self.brick_list:
            if arcade.check_for_collision(self.ball, brick):
                self.ball.change_y *= -1
                self.brick_list.remove(brick)
                self.rocket.score +=10
        

        if self.ball.center_y < 0:
            if len (self.heart_list)>0:
                self.heart_list.pop(-1)
                del self.ball
                self.ball=Ball(self)



game=Game()
arcade.run()