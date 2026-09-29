from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('run_animation.png')

frame = 0

while True:
    clear_canvas()

    grass.draw(400, 30)

    character.clip_draw(
        frame * 100, 0,
        100, 100,
        400, 160,
        100 * 3, 100 * 3
    )

    update_canvas()

    frame = (frame + 1) % 8
    delay(0.05)

close_canvas()