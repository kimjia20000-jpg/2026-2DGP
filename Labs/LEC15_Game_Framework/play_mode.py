from types import SimpleNamespace

from pico2d import *

import game_framework
import game_world
import title_mode
import pause_mode

from boy import Boy
from grass import Grass


def init():
    global boy

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)


def finish():
    game_world.clear()


def pause():
    global pause_started_at

    # 정지 중 키를 놓더라도 이동 입력이 남지 않도록 처리한다.
    boy.handle_event(
        SimpleNamespace(type=SDL_KEYUP, key=SDLK_LEFT)
    )
    boy.handle_event(
        SimpleNamespace(type=SDL_KEYUP, key=SDLK_RIGHT)
    )

    pause_started_at = get_time()


def resume():
    # 정지한 시간은 IDLE의 잠들기 대기 시간에서 제외한다.
    paused_duration = get_time() - pause_started_at
    boy.idle_started_at += paused_duration


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
            return

        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            if getattr(event, 'repeat', 0):
                continue

            game_framework.push_mode(pause_mode)
            return

        else:
            boy.handle_event(event)


def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    update_canvas()