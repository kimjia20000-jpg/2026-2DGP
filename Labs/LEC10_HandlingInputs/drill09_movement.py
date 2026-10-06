from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

# 캐릭터 프레임 크기
CHARACTER_WIDTH, CHARACTER_HEIGHT = 100, 100

open_canvas(TUK_WIDTH, TUK_HEIGHT)

tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True

x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
direction = 1

previous_action_row = None

right_pressed = False
left_pressed = False
up_pressed = False
down_pressed = False


def handle_events():
    global running
    global right_pressed, left_pressed, up_pressed, down_pressed

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

            elif event.key == SDLK_RIGHT:
                right_pressed = True

            elif event.key == SDLK_LEFT:
                left_pressed = True

            elif event.key == SDLK_UP:
                up_pressed = True

            elif event.key == SDLK_DOWN:
                down_pressed = True

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                right_pressed = False

            elif event.key == SDLK_LEFT:
                left_pressed = False

            elif event.key == SDLK_UP:
                up_pressed = False

            elif event.key == SDLK_DOWN:
                down_pressed = False


while running:
    handle_events()

    if not running:
        break

    dir_x = int(right_pressed) - int(left_pressed)
    dir_y = int(up_pressed) - int(down_pressed)

    x += dir_x * 5
    y += dir_y * 5

    # 캐릭터 전체가 화면 안에 있도록 좌표 제한
    x = max(
        CHARACTER_WIDTH // 2,
        min(TUK_WIDTH - CHARACTER_WIDTH // 2, x)
    )
    y = max(
        CHARACTER_HEIGHT // 2,
        min(TUK_HEIGHT - CHARACTER_HEIGHT // 2, y)
    )

    moving = dir_x != 0 or dir_y != 0

    if dir_x > 0:
        direction = 1
    elif dir_x < 0:
        direction = -1

    if moving:
        frame_count = 8

        if direction == 1:
            action_row = 1
        else:
            action_row = 0

    else:
        frame_count = 5

        if direction == 1:
            action_row = 3
        else:
            action_row = 2

    if action_row != previous_action_row:
        frame = 0
        previous_action_row = action_row

    clear_canvas()

    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    character.clip_draw(
        frame * CHARACTER_WIDTH,
        action_row * CHARACTER_HEIGHT,
        CHARACTER_WIDTH,
        CHARACTER_HEIGHT,
        x,
        y
    )

    update_canvas()

    frame = (frame + 1) % frame_count

    delay(0.05)

close_canvas()