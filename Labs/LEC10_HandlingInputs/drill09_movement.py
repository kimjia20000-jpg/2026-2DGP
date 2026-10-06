from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)

tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True

x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0

right_pressed = False
left_pressed = False  # 왼쪽 키 상태 추가


def handle_events():
    global running, right_pressed, left_pressed

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

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                right_pressed = False

            elif event.key == SDLK_LEFT:
                left_pressed = False


while running:
    handle_events()

    if not running:
        break

    # 오른쪽만 누르면 +1, 왼쪽만 누르면 -1
    # 둘 다 누르거나 아무것도 누르지 않으면 0
    dir_x = int(right_pressed) - int(left_pressed)
    x += dir_x * 5

    clear_canvas()

    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100, 100, 100, x, y)

    update_canvas()
    delay(0.05)

close_canvas()