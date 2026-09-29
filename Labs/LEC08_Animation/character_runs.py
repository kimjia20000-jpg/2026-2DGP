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

RUN_FRAMES = (
    (20, 207, 173, 180),
    (201, 206, 189, 180),
    (398, 197, 189, 191),
    (595, 197, 189, 189),
    (792, 197, 190, 189),
    (990, 197, 189, 188),
    (1187, 199, 189, 188),
    (1384, 197, 189, 184),
    (1581, 197, 166, 188)
)

JUMP_FRAMES = (
    (36, 631, 152, 169),
    (220, 640, 148, 195),
    (412, 691, 158, 187),
    (605, 710, 173, 177),
    (808, 685, 160, 201),
    (999, 663, 162, 183),
    (1203, 642, 166, 180),
    (1386, 628, 162, 174),
    (1571, 630, 171, 155)
)

while True:

    # 걷기 5회 반복
    for repeat in range(5):
        for frame in range(len(WALK_FRAMES)):
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
            delay(0.05)

    # 걷기 종료 후 1초 정지
    delay(1.0)

    # 뛰기 5회 반복
    for repeat in range(5):
        for frame in range(len(RUN_FRAMES)):
            clear_canvas()

            grass.draw(400, 30)

            left, bottom, width, height = RUN_FRAMES[frame]

            draw_width = width * 1.5
            draw_height = height * 1.5

            character.clip_draw(
                left, bottom,
                width, height,
                400, 30 + draw_height / 2,
                draw_width, draw_height
            )

            update_canvas()
            delay(0.05)

    # 뛰기 종료 후 1초 정지
    delay(1.0)

    # 점프 5회 반복
    for repeat in range(5):
        for frame in range(len(JUMP_FRAMES)):
            clear_canvas()

            grass.draw(400, 30)

            left, bottom, width, height = JUMP_FRAMES[frame]

            draw_width = width * 1.5
            draw_height = height * 1.5

            jump_height = (bottom - 630) * 1.5

            character.clip_draw(
                left, bottom,
                width, height,
                400,
                30 + draw_height / 2 + jump_height,
                draw_width, draw_height
            )

            update_canvas()
            delay(0.05)

    # 점프 종료 후 1초 정지
    delay(1.0)

close_canvas()