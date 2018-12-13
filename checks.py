map_width = 240
map_height = 20

#check 10 units ahead
def is_10obstacle_in_way(player_pos):
    print("in_is_10obstacle_in_way")
    level = player_pos[1]
    if map_width - player_pos[2] > 10:
        for i in range(0,10):
            if level[player_pos[0]][player_pos[2] + i] is "x":
                print("obstacle detected!")
                return True
    else:
        for i in range(0,map_width-player_pos[2]):
            if level[player_pos[0]][player_pos[2] + i] is "x":
                print("obstacle detected!")
                return True
    return False

#check 20 units ahead
def is_20obstacle_in_way(player_pos):
    print("in_is_20obstacle_in_way")
    level = player_pos[1]
    if map_width - player_pos[2] > 20:
        for i in range(0,20):
            if level[player_pos[0]][player_pos[2] + i] is "x":
                print("obstacle detected!")
                return True
    else:
        for i in range(0,map_width-player_pos[2]):
            if level[player_pos[0]][player_pos[2] + i] is "x":
                print("obstacle detected!")
                return True
    return False

#check 15 units ahead
def is_15obstacle_in_way(player_pos):
    print("in_is_15obstacle_in_way")
    level = player_pos[1]
    if map_width - player_pos[2] > 15:
        for i in range(0,15):
            if level[player_pos[0]][player_pos[2] + i] is "x":
                print("obstacle detected!")
                return True
    else:
        for i in range(0,map_width-player_pos[2]):
            if level[player_pos[0]][player_pos[2] + i] is "x":
                print("obstacle detected!")
                return True
    return False

#check 5 units ahead
def is_5obstacle_in_way(player_pos):
    print("in_is_5obstacle_in_way")
    level = player_pos[1]
    if map_width - player_pos[2] > 5:
        for i in range(0,5):
            if level[player_pos[0]][player_pos[2] + i] is "x":
                print("obstacle detected!")
                return True
    else:
        for i in range(0,map_width-player_pos[2]):
            if level[player_pos[0]][player_pos[2] + i] is "x":
                print("obstacle detected!")
                return True
    return False
