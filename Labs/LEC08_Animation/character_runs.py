from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('run_animation.png')

frame = 0

while True:
    for x in range(0, 800, 5):
        clear_canvas()

        grass.draw(400, 30)

        character.clip_draw(
            frame * 100, 0,
            100, 100,
            x, 160,
            100 * 3, 100 * 3
        )

        update_canvas()

        frame = (frame + 1) % 8
        delay(0.05)

    for x in range(800, 0, -5):
        clear_canvas()

        grass.draw(400, 30)

        character.clip_composite_draw(
            frame * 100, 0,
            100, 100,
            0, 'h',
            x, 160,
            100 * 3, 100 * 3
        )

        update_canvas()

        frame = (frame + 1) % 8
        delay(0.05)

close_canvas()