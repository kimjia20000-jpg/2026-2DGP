from types import SimpleNamespace

from pico2d import *

import game_framework
import game_world
import title_mode
import pause_mode
import item_mode

from boy import Boy
from grass import Grass


def init():
    global boy
    global pause_started_at

    pause_started_at = None

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)


def finish():
    game_world.clear()


def pause():
    # 모드를 올리는 것만으로 게임을 정지시키지는 않는다.
    pass


def resume():
    global pause_started_at

    # P로 일시정지한 경우에만 타이머를 보정한다.
    if pause_started_at is not None:
        paused_duration = get_time() - pause_started_at
        boy.idle_started_at += paused_duration
        pause_started_at = None


def handle_events():
    global pause_started_at

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

            # 실제 일시정지는 P를 눌렀을 때만 처리한다.
            boy.handle_event(
                SimpleNamespace(type=SDL_KEYUP, key=SDLK_LEFT)
            )
            boy.handle_event(
                SimpleNamespace(type=SDL_KEYUP, key=SDLK_RIGHT)
            )

            pause_started_at = get_time()
            game_framework.push_mode(pause_mode)
            return

        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            if getattr(event, 'repeat', 0):
                continue

            # 이동 입력과 타이머를 유지한 채 아이템 창을 연다.
            game_framework.push_mode(item_mode)
            return

        else:
            boy.handle_event(event)


def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    update_canvas()