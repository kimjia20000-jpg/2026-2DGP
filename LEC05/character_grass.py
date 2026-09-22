from pico2d import *

open_canvas()

character = load_image('character.png')

x = 100
y = 90

direction = 0
# 0 : 오른쪽
# 1 : 위G
# 2 : 왼쪽
# 3 : 아래

while True:
    clear_canvas()

    character.draw(x, y)

    update_canvas()

    if direction == 0:
        x += 2

        if x >= 700:
            direction = 1

    elif direction == 1:
        y += 2

        if y >= 500:
            direction = 2

    elif direction == 2:
        x -= 2

        if x <= 100:
            direction = 3

    elif direction == 3:
        y -= 2

        if y <= 90:
            direction = 0

    delay(0.01)

close_canvas()