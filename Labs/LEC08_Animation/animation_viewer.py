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


# 각 프레임은 (left, bottom, width, height) 형식으로 저장
# 프레임마다 width, height가 달라도 사용할 수 있음
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
    (22, 209, 162, 178),
    (203, 209, 173, 174),
    (390, 209, 177, 177),
    (578, 207, 165, 177),
    (757, 201, 163, 183),
    (944, 201, 173, 180),
    (1137, 204, 193, 181),
    (1345, 202, 202, 177),
    (1563, 201, 182, 179)
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


# Attack은 다른 애니메이션과 달리 8프레임
ATTACK_FRAMES = (
    (24, 10, 193, 165),
    (222, 10, 172, 183),
    (401, 10, 198, 187),
    (619, 9, 186, 188),
    (864, 8, 260, 169),
    (1130, 8, 200, 162),
    (1330, 8, 212, 164),
    (1552, 8, 195, 161)
)


# 애니메이션마다 서로 다른 개수의 프레임을 가질 수 있음
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

ACTION_SEQUENCE = (
    WALK,
    RUN,
    JUMP,
    ATTACK
)


def draw_frame(action, frame_data):
    clear_canvas()

    grass.draw(400, GROUND_Y)

    # 현재 프레임마다 다른 위치와 크기를 그대로 사용
    left, bottom, width, height = frame_data

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
    # 현재 애니메이션의 프레임 목록
    frames = ACTIONS[action]

    for repeat in range(ACTION_REPEAT):

        # 프레임 개수를 고정하지 않고
        # 현재 애니메이션에 들어 있는 프레임만큼 반복
        for frame_data in frames:
            draw_frame(action, frame_data)

    delay(ACTION_PAUSE)


while True:
    for action in ACTION_SEQUENCE:
        play_action(action)

close_canvas()