from pico2d import *

import game_framework
import game_world
import play_mode


def init():
    global image
    image = load_image('item_select.png')


def finish():
    global image
    del image


def pause():
    pass


def resume():
    pass


def update():
    # 아이템 창이 열려 있어도 게임은 계속 진행한다.
    play_mode.update()


def render():
    clear_canvas()

    # 게임 화면을 먼저 그린다.
    game_world.render()

    # 게임 화면 위에 아이템 선택 창을 그린다.
    image.draw(
        get_canvas_width() // 2,
        get_canvas_height() // 2
    )

    update_canvas()


def handle_events():
    close_requested = False

    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return

        if event.type == SDL_KEYDOWN:
            if event.key in (SDLK_0, SDLK_1, SDLK_2, SDLK_i):
                # 키를 누르고 있을 때 발생하는 반복 입력 무시
                if getattr(event, 'repeat', 0):
                    continue

                # 이번 입력 목록에서 첫 선택만 적용한다.
                if not close_requested:
                    if event.key == SDLK_0:
                        play_mode.boy.select_ball(0)

                    elif event.key == SDLK_1:
                        play_mode.boy.select_ball(1)

                    elif event.key == SDLK_2:
                        play_mode.boy.select_ball(2)

                    # I는 선택을 유지하고 창만 닫는다.
                    close_requested = True

                continue

        # 창을 닫기로 했더라도 남은 이동·발사 입력을 처리한다.
        # 특히 방향키를 놓는 입력이 누락되지 않도록 한다.
        play_mode.boy.handle_event(event)

    # 입력을 모두 처리한 뒤 기존 플레이 모드로 돌아간다.
    if close_requested:
        game_framework.pop_mode()