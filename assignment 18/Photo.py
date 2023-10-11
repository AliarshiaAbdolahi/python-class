import arcade
from random import randrange

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

arcade.open_window(SCREEN_HEIGHT,SCREEN_WIDTH,"Nature")
arcade.set_background_color(arcade.color.BLUE_YONDER)
arcade.start_render()
arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0,arcade.color.GREEN_YELLOW)
arcade.draw_circle_filled(200, SCREEN_HEIGHT - 100, 80, arcade.color.SUNSET)
arcade.draw_circle_outline(200, SCREEN_HEIGHT - 100, 80, arcade.color.BLACK)

def draw_tree(x,y):
    arcade.draw_rectangle_filled(x, y, 15, 75, arcade.color.DARK_BROWN)
    arcade.draw_circle_filled(x, y + 20, 35, arcade.color.DARK_GREEN)
    
for i in range(25, SCREEN_WIDTH - 25, 70):
    max_y = SCREEN_HEIGHT / 3
    draw_tree(randrange(i - 25, i + 25),randrange(max_y))

arcade.finish_render()
arcade.run()