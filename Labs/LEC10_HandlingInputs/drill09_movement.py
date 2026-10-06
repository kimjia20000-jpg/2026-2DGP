from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)

tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True

x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0

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

    # 가로 또는 세로 이동 입력이 있는지 확인
    moving = dir_x != 0 or dir_y != 0

    clear_canvas()

    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100, 100, 100, x, y)

    update_canvas()

    # 이동 중에만 0~7번 프레임을 순환
    if moving:
        frame = (frame + 1) % 8

    delay(0.05)

close_canvas()