from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)

tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True

x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0

# 오른쪽 방향키를 누르고 있는지 저장
right_pressed = False


def handle_events():
    global running, right_pressed

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

            # 오른쪽 키를 누르면 이동 시작
            elif event.key == SDLK_RIGHT:
                right_pressed = True

        elif event.type == SDL_KEYUP:
            # 오른쪽 키를 떼면 이동 중지
            if event.key == SDLK_RIGHT:
                right_pressed = False


while running:
    handle_events()

    if not running:
        break

    # 오른쪽 키를 누르는 동안 위치 변경
    if right_pressed:
        x += 5

    clear_canvas()

    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100, 100, 100, x, y)

    update_canvas()
    delay(0.05)

close_canvas()