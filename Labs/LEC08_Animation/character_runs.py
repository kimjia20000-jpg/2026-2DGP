from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('samuriSheet.png')

FRAME_WIDTH = 222
FRAME_HEIGHT = 222

IDLE_Y = 666
WALK_Y = 444
RUN_Y = 222
ATTACK_Y = 0

DRAW_WIDTH = 320
DRAW_HEIGHT = 320

frame = 0

while True:
    for x in range(160, 641, 5):
        clear_canvas()

        grass.draw(400, 30)

        character.clip_draw(
            frame * FRAME_WIDTH, RUN_Y,
            FRAME_WIDTH, FRAME_HEIGHT,
            x, 190,
            DRAW_WIDTH, DRAW_HEIGHT
        )

        update_canvas()

        frame = (frame + 1) % 8
        delay(0.05)

    for x in range(640, 159, -5):
        clear_canvas()

        grass.draw(400, 30)

        character.clip_composite_draw(
            frame * FRAME_WIDTH, RUN_Y,
            FRAME_WIDTH, FRAME_HEIGHT,
            0, 'h',
            x, 190,
            DRAW_WIDTH, DRAW_HEIGHT
        )

        update_canvas()

        frame = (frame + 1) % 8
        delay(0.05)

close_canvas()