from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('samuriSheet.png')

WALK_FRAMES = (
    (26, 404, 135, 208),
    (213, 403, 141, 209),
    (402, 403, 136, 210),
    (585, 405, 139, 208),
    (763, 405, 138, 207),
    (939, 405, 155, 208),
    (1123, 405, 150, 207),
    (1308, 405, 160, 207),
    (1509, 409, 149, 203)
)

frame = 0

while True:
    clear_canvas()

    grass.draw(400, 30)

    left, bottom, width, height = WALK_FRAMES[frame]

    draw_width = width * 1.5
    draw_height = height * 1.5

    character.clip_draw(
        left, bottom,
        width, height,
        400, 30 + draw_height / 2,
        draw_width, draw_height
    )

    update_canvas()

    frame = (frame + 1) % len(WALK_FRAMES)
    delay(0.05)

close_canvas()