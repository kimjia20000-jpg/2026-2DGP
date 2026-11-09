from pico2d import *

import game_framework
import play_mode


def init():
    pass


def finish():
    pass


def pause():
    pass


def resume():
    pass


def update():
    # 소년과 공의 움직임을 업데이트하지 않는다.
    pass


def render():
    # 멈춘 플레이 화면을 그대로 표시한다.
    play_mode.render()


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_p:
                if getattr(event, 'repeat', 0):
                    continue

                game_framework.pop_mode()
                return