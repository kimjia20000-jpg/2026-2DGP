from pico2d import load_image, get_canvas_width

import game_world


class Ball:
    image = None

    def __init__(self, x, y, direction):
        # 모든 공이 하나의 이미지를 공유한다.
        if Ball.image is None:
            Ball.image = load_image('ball21x21.png')

        self.x = x
        self.y = y
        self.direction = direction
        self.speed = 10

    def update(self):
        # 발사 당시의 방향으로 직선 이동한다.
        self.x += self.direction * self.speed

        # 공이 화면 밖으로 완전히 나가면 제거한다.
        if self.x < -11 or self.x > get_canvas_width() + 11:
            game_world.remove_object(self)

    def draw(self):
        Ball.image.draw(self.x, self.y)