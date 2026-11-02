from pico2d import *

from boy import Boy
from grass import Grass
from grass import Grass2

import game_world


def handle_events():
    global running

    for event in get_events():
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

        else:
            boy.handle_event(event)


def reset_world():
    global boy

    boy = Boy()
    game_world.add_object(boy, 1)

    grass = Grass()
    game_world.add_object(grass)

    grass = Grass2()
    game_world.add_object(grass, 1)

   


def update_world():
    game_world.update()


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


running = True

open_canvas()
reset_world()

while running:
    handle_events()

    if not running:
        break

    update_world()
    render_world()
    delay(0.01)

close_canvas()