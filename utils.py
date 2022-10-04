from random import randint as rand

def randbool (r, max_r):
    t = rand(0, max_r)
    return (t <= r)

def randcell(w, h):
    tw = rand(0, w-1)
    th = rand(0, h-1)
    return (th, tw)

# 0 - вверх, 1 - направо, 2 - вниз, 3 - влево
def randcell2(x, y):
    moves = [(-1,0), (0,1), (1,0), (0, -1)]
    direction = rand(0,3)
    dx, dy = moves[direction][0], moves[direction][1]
    return (x + dx, y + dy)