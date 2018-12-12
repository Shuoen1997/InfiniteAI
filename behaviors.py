import random 
map_height = 20
def move_random_vert(player_pos):
    # return random.randint(-1, 1)
    player_pos[0] = max(min(map_height-2, player_pos[0] + random.randint(-4, 4)), 1)
    # print("in_move_random")
    return True

def move_alittle(player_pos):
    player_pos[0] = max(min(map_height-2, player_pos[0] + random.randint(-1, 1)), 1)
    # print("in_move_alittle")
    return True
