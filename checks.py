
def is_obstacle_in_way(player_pos):
    for i in range(0,10):
        if level[player_pos[0]][player_x + i] is "x":
            print("obstacle detected!")
            return True
    #print("no obstacle detected")
    return False
