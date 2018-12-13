
def is_obstacle_in_way(player_pos):
    for i in range(0,10):
        level = player_pos[1]
        if level[player_pos[0]][player_pos[2] + i] is "x":
            print("obstacle detected!")
            return True
    #print("no obstacle detected")
    return False
