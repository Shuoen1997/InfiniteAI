def move_random_vert(pos):
    return max(min(map_height-2, pos+random.randint(-1, 1)), 1)

def move_forward(pos):
    return pos
