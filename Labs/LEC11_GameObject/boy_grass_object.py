from pico2d import *
import random


# Game object class here

# 게임 객체를 파악.
# boy, grass 가 필요하다.

class Grass: # 클래스는 대문자로 시작한다.
    # 잔디 속성을 초기화
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass

class Boy:
    def __init__(self):
        self.x = random.randint(100, 700)
        self.y = 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        self.x = 400
        self.y = 30
        self.image = load_image('ball21x21.png')

    def draw(self):
        self.image.draw(400,300)

    def update(self):
        pass

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running
    running = True
    global world
    world = [] # 월드 전체를 나타내는 리스트, 즉 월드의 모든 객체들이 들어있다.

    # 잔디 객체를 찍어낸다.
    grass = Grass()
    world.append(grass) 

    team = [Boy() for i in range(11)] # 11명의 소년 객체를 생성하여 team 리스트에 넣는다.
    world += team # world 리스트에 team 리스트를 합친다.

    ball = Ball()
    world.append(ball)

def update_world():
    for o in world:
        o.update() 

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

open_canvas()

reset_world() # 세상을 구성하는 객체들을 초기화
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
