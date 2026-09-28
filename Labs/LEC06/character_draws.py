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
       move_character_circle(x, y)
    pass

def move_character_circle(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)

def move_top():
    print('TOP')
    for x in range(50, 750, 5):
        move_character_top(x)
    pass

def move_character_top(x):
    clear_canvas()
    character.draw(x, 550)
    update_canvas()
    delay(0.01)

def move_right():
    print('RIGHT')
    for y in range(550, 50, -5):
       move_character_right(y)
    pass

def move_character_right(y):
    clear_canvas()
    character.draw(750, y)
    update_canvas()
    delay(0.01)

def move_bottom():
    print('BOTTOM')
    for x in range(750, 50, -5):
        move_character_bottom(x)
    pass

def move_character_bottom(x):
    clear_canvas()
    character.draw(x, 50)
    update_canvas()
    delay(0.01)

def move_left():
    print('LEFT')
    for y in range(50, 550, 5):
        move_character_left(y)
    pass

def move_character_left(y):
    clear_canvas()
    character.draw(50, y)
    update_canvas()
    delay(0.01)

def move_rectangle():
    print('RECTANGLE')
    move_top()
    move_right()
    move_bottom()
    move_left()
    pass

def move_triangle_bottom():
    print('TRIANGLE BOTTOM')

    x0 = 100
    y0 = 100

    x1 = 700
    y1 = 100

    n = 100

    for step in range(n + 1):
        t = step / n

        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t

        move_character_triangle_bottom(x, y)
    pass

def move_character_triangle_bottom(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)

def move_triangle_right():
    print('TRIANGLE RIGHT')

    x0 = 700
    y0 = 100

    x1 = 400
    y1 = 500

    n = 100

    for step in range(n + 1):
        t = step / n

        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t

        move_character_triangle_right(x, y)
    pass

def move_character_triangle_right(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)

def move_triangle_left():
    print('TRIANGLE LEFT')

    x0 = 400
    y0 = 500

    x1 = 100
    y1 = 100

    n = 100

    for step in range(n + 1):
        t = step / n

        x = x0 + (x1 - x0) * t
        y = y0 + (y1 - y0) * t

        move_character_triangle_left(x, y)
    pass

def move_character_triangle_left(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)

def move_triangle():
    print('TRIANGLE')
    # move_triangle_bottom()
    # move_triangle_right()
    move_triangle_left()
    pass

while True:
    # move_circle()
    # move_rectangle()
    move_triangle()
    pass

close_canvas()
