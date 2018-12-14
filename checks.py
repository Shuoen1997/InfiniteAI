import behaviors

map_width = 240
map_height = 20
top = map_height-2
bottom = 1
opening_pos = 0

#check 10 units ahead
def is_10obstacle_in_way(player_pos):
    # print("in_is_10obstacle_in_way")
    level = player_pos[1]
    if map_width - player_pos[2] > 10:
        for i in range(0,10):
            if level[player_pos[0]][player_pos[2] + i] is "x":
                # print("obstacle detected!")
                return True
    else:
        for i in range(0,map_width-player_pos[2]):
            if level[player_pos[0]][player_pos[2] + i] is "x":
                # print("obstacle detected!")
                return True
    return False

#check 20 units ahead
def is_20obstacle_in_way(player_pos):
    # print("in_is_20obstacle_in_way")
    level = player_pos[1]
    if map_width - player_pos[2] > 20:
        for i in range(0,20):
            if level[player_pos[0]][player_pos[2] + i] is "x":
                # print("obstacle detected!")
                return True
    else:
        for i in range(0,map_width-player_pos[2]):
            if level[player_pos[0]][player_pos[2] + i] is "x":
                # print("obstacle detected!")
                return True
    return False

#check 15 units ahead
def is_15obstacle_in_way(player_pos):
    # print("in_is_15obstacle_in_way")
    level = player_pos[1]
    if map_width - player_pos[2] > 15:
        for i in range(0,15):
            if level[player_pos[0]][player_pos[2] + i] is "x":
                # print("obstacle detected!")
                return True
    else:
        for i in range(0,map_width-player_pos[2]):
            if level[player_pos[0]][player_pos[2] + i] is "x":
                # print("obstacle detected!")
                return True
    return False

#check 5 units ahead
def is_5obstacle_in_way(player_pos):
    # print("in_is_5obstacle_in_way")
    level = player_pos[1]
    if map_width - player_pos[2] > 5:
        for i in range(0,5):
            if level[player_pos[0]][player_pos[2] + i] is "x":
                # print("obstacle detected!")

                return True
    else:
        for i in range(0,map_width-player_pos[2]):
            if level[player_pos[0]][player_pos[2] + i] is "x":
                # print("obstacle detected!")
                return True
    return False

#check if there is a top opening
def is_top_opening(player_pos):
    # print("in__is_top_opening")
    level = player_pos[1]
    if map_width - player_pos[2] > 10:
        for i in range(0,10):
            if level[player_pos[0]][player_pos[2] + i] is "x":
                # print("obstacle detected at:", player_pos[0],player_pos[2] + i)
                # print("player_pos at:", player_pos[0])
                for j in range(0, top-player_pos[0]):
                    if level[player_pos[0]+j][player_pos[2] + i] is not "x":
                        behaviors.opening_pos = player_pos[0]+j,player_pos[2] + i
                        # print("opening detected at",behaviors.opening_pos)
                        return True
    else:
        for i in range(0,map_width-player_pos[2]):
            if level[player_pos[0]][player_pos[2] + i] is "x":
                # print("obstacle detected!")
                for j in range(0, top-player_pos[0]):
                    if level[player_pos[0]+j][player_pos[2] + i] is not "x":
                        behaviors.opening_pos = player_pos[0]+j,player_pos[2] + i
                        # print("opening detected at",behaviors.opening_pos)
                        return True
    # print("returning false -> no top opening")
    return False

#check if there is a top opening
def is_bottom_opening(player_pos):
    print("in__is_bottom_opening")
    level = player_pos[1]
    if map_width - player_pos[2] > 10:
        for i in range(0,10):
            if level[player_pos[0]][player_pos[2] + i] is "x":
                print("obstacle detected at:", player_pos[0],player_pos[2] + i)
                print("player_pos at:", player_pos[0])
                for j in range(0, player_pos[0]-bottom):
                    if level[player_pos[0]-j][player_pos[2] + i] is not "x":
                        behaviors.opening_pos = player_pos[0]-j,player_pos[2] + i
                        print("opening detected at",behaviors.opening_pos)
                        return True
    else:
        for i in range(0,map_width-player_pos[2]):
            if level[player_pos[0]][player_pos[2] + i] is "x":
                print("obstacle detected!")
                for j in range(0, player_pos[0]-bottom):
                    if level[player_pos[0]-j][player_pos[2] + i] is not "x":
                        behaviors.opening_pos = player_pos[0]+j,player_pos[2] + i
                        print("opening detected at",behaviors.opening_pos)
                        return True
    print("returning false -> no bottom opening")
    return False
