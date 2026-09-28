# 실습 과제 진행
from pico2d import *

# 맨처음 해야할 일은.
open_canvas(800, 600)
character = load_image('character.png')

def move_circle():
    print('CIRCLE')
    # 캐릭터 이미지 표시
    for degree in range(360):
       theta = math.radians(degree)
       x = 400 + 200 * math.cos(theta)
       y = 300 + 200 * math.sin(theta)

       clear_canvas()
       character.draw(x, y)
       update_canvas()
       delay(0.01)
    pass

def move_top():
    print('TOP')
    for x in range(50, 750, 5):
        clear_canvas()
        character.draw(x, 550)
        update_canvas()
        delay(0.01)
    pass

def move_left():
    print('LEFT')
    pass

def move_bottom():
    print('BOTTOM')
    pass

def move_right():
    print('RIGHT')
    pass

def move_rectangle():
    print('RECTANGLE')
    move_top()
    move_left()
    move_bottom()
    move_right()
    pass

def move_triangle():
    print('TRIANGLE')
    pass

while True:
    move_circle()
    move_rectangle()
    move_triangle()
    pass

close_canvas()
