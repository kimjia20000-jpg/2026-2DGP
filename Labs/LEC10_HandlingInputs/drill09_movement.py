from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)

running = True


def handle_events():
    global running

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False


while running:
    handle_events()

    if not running:
        break

    clear_canvas()
    update_canvas()
    delay(0.05)

close_canvas()