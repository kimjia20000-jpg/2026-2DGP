# world = [] 1차원 리스트

world = [ [], [] ] # 0번, 1번 레이어를 가지는 2차원 리스트

# 게임 월드에 객체 추가, layer를 지정해야 한다.
def add_object(o, depth = 0): # 기본 depth = 0, 즉 0번 레이어에 추가
    world[depth].append(o)


# 게임 월드에서 객체 제거
def remove_object(o):
    for layer in world:
        if o in layer:
           layer.remove(o)
           return # 더 이상 찾을 필요가 없으므로 return 종료, 최적화

# game logic
def update():
    for layer in world:
        for o in layer: # layer를 순회하면서 객체를 제거할 수도 있으므로 복사본을 만들어서 순회한다.
            o.update()


# game rendering
def render():
    for layer in world:
        for o in layer:
            o.draw()