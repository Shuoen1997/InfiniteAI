import random
map_height = 20

#randomly move up or down by up to 4 units
def move_random_vert(player_pos):
    # return random.randint(-1, 1)
    player_pos[0] = max(min(map_height-2, player_pos[0] + random.randint(-4, 4)), 1)
    print("in_move_random")
    return True

#randomly move up or down by up to 1 unit
def move_alittle(player_pos):
    player_pos[0] = max(min(map_height-2, player_pos[0] + random.randint(-1, 1)), 1)
    print("in_move_alittle")
    return True

#randomly going up or down by a fixed amount, within boundary limit
def fixed_oscillate(player_pos):
    print("in_fixed_oscillate")
    if player_pos[0] is map_height-2: #if at the top, just go down
        player_pos[0] = player_pos[0] - 1
    elif player_pos[0] is 1: #if at the bottom, just go up
        player_pos = player_pos[0] + 1
    else:
        flip = random.randint(0,1)
        if flip == 1:
            player_pos[0] = player_pos[0] - 1
        elif flip == 0:
            player_pos[0] = player_pos[0] + 1
    return True

#randomly going up or down by a variable amount
def variable_oscillate(player_pos):
    print("in_variable_oscillate")
    top = map_height - 2
    bottom = 1
    distance_from_top = top-player_pos[0]
    distance_from_bottom = player_pos[0] - bottom
    if distance_from_top > distance_from_bottom: #distance from top is greater, so go up random amount within allowed distance
        player_pos[0] = player_pos[0] + random.randint(0,distance_from_top)
    if distance_from_top < distance_from_bottom: #distance from top is lower, so go down random amount within allowed distance
        player_pos[0] = player_pos[0] - random.randint(0, distance_from_bottom)
    return True

def do_nothing(player_pos):
    print("in_do_nothing")
    return True
