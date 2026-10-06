from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)

tuk_ground = load_image('TUK_GROUND.png')

# 캐릭터 스프라이트 이미지 불러오기
character = load_image('animation_sheet.png')

running = True

# 캐릭터의 초기 위치와 프레임
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0


def handle_events():
    global running

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False


while running:
    handle_events()

    if not running:
        break

    clear_canvas()

    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

    # 캐릭터 한 프레임을 배경 위에 출력
    character.clip_draw(frame * 100, 100, 100, 100, x, y)

    update_canvas()
    delay(0.05)

close_canvas()