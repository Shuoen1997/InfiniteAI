
#check 10 units ahead
def is_10obstacle_in_way(player_pos):
    print("in_is_10obstacle_in_way")
    for i in range(0,10):
        level = player_pos[1]
        if level[player_pos[0]][player_pos[2] + i] is "x":
            print("obstacle detected!")
            return True
    return False

#check 20 units ahead
def is_20obstacle_in_way(player_pos):
    print("in_is_20obstacle_in_way")
    for i in range(0,20):
        level = player_pos[1]
        if level[player_pos[0]][player_pos[2] + i] is "x":
            print("obstacle detected!")
            return True
    return False

#check 15 units ahead
def is_15obstacle_in_way(player_pos):
    print("in_is_15obstacle_in_way")
    for i in range(0,15):
        level = player_pos[1]
        if level[player_pos[0]][player_pos[2] + i] is "x":
            print("obstacle detected!")
            return True
    return False

#check 5 units ahead
def is_5obstacle_in_way(player_pos):
    print("in_is_5obstacle_in_way")
    for i in range(0,5):
        level = player_pos[1]
        if level[player_pos[0]][player_pos[2] + i] is "x":
            print("obstacle detected!")
            return True
    return False
