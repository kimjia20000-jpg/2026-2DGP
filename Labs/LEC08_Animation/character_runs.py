from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('samuriSheet.png')

# 애니메이션 설정값
ACTION_REPEAT = 5
ACTION_PAUSE = 1.0
FRAME_DELAY = 0.05
DRAW_SCALE = 1.5

CHARACTER_X = 400
GROUND_Y = 30
JUMP_BASE_BOTTOM = 630


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

ATTACK_FRAMES = (
    (24, 10, 173, 165),
    (197, 9, 197, 184),
    (394, 10, 197, 187),
    (591, 8, 197, 189),
    (788, 8, 198, 178),
    (986, 8, 197, 169),
    (1183, 8, 197, 163),
    (1380, 8, 197, 165),
    (1577, 8, 170, 161)
)

ACTIONS = (
    WALK_FRAMES,
    RUN_FRAMES,
    JUMP_FRAMES,
    ATTACK_FRAMES
)

WALK = 0
RUN = 1
JUMP = 2
ATTACK = 3


def draw_frame(action, frame):
    clear_canvas()

    grass.draw(400, GROUND_Y)

    left, bottom, width, height = ACTIONS[action][frame]

    draw_width = width * DRAW_SCALE
    draw_height = height * DRAW_SCALE

    y = GROUND_Y + draw_height / 2

    if action == JUMP:
        jump_height = (bottom - JUMP_BASE_BOTTOM) * DRAW_SCALE
        y += jump_height

    character.clip_draw(
        left, bottom,
        width, height,
        CHARACTER_X, y,
        draw_width, draw_height
    )

    update_canvas()
    delay(FRAME_DELAY)


def play_action(action):
    for repeat in range(ACTION_REPEAT):
        for frame in range(len(ACTIONS[action])):
            draw_frame(action, frame)

    delay(ACTION_PAUSE)


while True:
    play_action(WALK)
    play_action(RUN)
    play_action(JUMP)
    play_action(ATTACK)

close_canvas()