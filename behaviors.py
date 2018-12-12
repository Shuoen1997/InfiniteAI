import random 
map_height = 20
def move_random_vert(player_pos):
    # return random.randint(-1, 1)
    player_pos[0] = max(min(map_height-2, player_pos[0] + random.randint(-4, 4)), 1)
    return True

def stay(player_pos):
    player_pos = player_pos
    print("in stay")
    return True
