from pico2d import *
import math

open_canvas(800, 600)

# 캐릭터 이미지
character = load_image('character.png')

# 캐릭터 크기
CHAR_WIDTH = 50
CHAR_HEIGHT = 50


# -----------------------------------
# 캐릭터 그리기
# -----------------------------------
def draw_character(x, y):
    clear_canvas()

    character.draw(x, y, CHAR_WIDTH, CHAR_HEIGHT)

    update_canvas()
    delay(0.01)


# -----------------------------------
# 1. 원 운동
# -----------------------------------
def move_circle():

    center_x = 400
    center_y = 300
    radius = 150

    for degree in range(360):
        radian = math.radians(degree)

        x = center_x + radius * math.cos(radian)
        y = center_y + radius * math.sin(radian)

        draw_character(x, y)


# -----------------------------------
# 2. 사각 운동
# -----------------------------------

# 아래쪽 : 왼쪽 → 오른쪽
def move_square_bottom():

    for x in range(250, 551):
        y = 150

        draw_character(x, y)


# 오른쪽 : 아래 → 위
def move_square_right():

    for y in range(150, 451):
        x = 550

        draw_character(x, y)


# 위쪽 : 오른쪽 → 왼쪽
def move_square_top():

    for x in range(550, 249, -1):
        y = 450

        draw_character(x, y)


# 왼쪽 : 위 → 아래
def move_square_left():

    for y in range(450, 149, -1):
        x = 250

        draw_character(x, y)


def move_square():

    move_square_bottom()
    move_square_right()
    move_square_top()
    move_square_left()


# -----------------------------------
# 3. 삼각 운동
# -----------------------------------

# 꼭짓점
# 왼쪽 아래  = (250, 150)
# 오른쪽 아래 = (550, 150)
# 위         = (400, 450)


# 아래쪽 : 왼쪽 아래 → 오른쪽 아래
def move_triangle_bottom():

    for i in range(301):

        t = i / 300

        x = 250 + (550 - 250) * t
        y = 150

        draw_character(x, y)


# 오른쪽 : 오른쪽 아래 → 위
def move_triangle_right():

    for i in range(301):

        t = i / 300

        x = 550 + (400 - 550) * t
        y = 150 + (450 - 150) * t

        draw_character(x, y)


# 왼쪽 : 위 → 왼쪽 아래
def move_triangle_left():

    for i in range(301):

        t = i / 300

        x = 400 + (250 - 400) * t
        y = 450 + (150 - 450) * t

        draw_character(x, y)


def move_triangle():

    move_triangle_bottom()
    move_triangle_right()
    move_triangle_left()


# -----------------------------------
# 전체 운동 반복
# -----------------------------------
while True:

    # 원 운동
    move_circle()

    # 사각 운동
    move_square()

    # 삼각 운동
    move_triangle()


close_canvas()