
from time import sleep
from sys import argv
from player_bot import *

OKGREEN = "\033[92m"
ENDC = "\033[0m"
SLEEP_TIME = 0.08
map_height = 20
map_width = 240
game_height = 20
game_width = 120
player_x = 3
player_y = 9
# xxxx
# xxxx
# xxxx

def simulation(level, player, verbose):
    #run fast simulation
    #set verbose to True to print out the process
    #return the distance it has travelled
    player_pos = [player_y, level, 0]
    scroll_offset = -1
    while scroll_offset < map_width -1:
        #check if the player has hit obstacle, end game accordingly
        
        player_pos[2] = scroll_offset
        scroll_offset+=1
        player(player_pos)
        if level[player_pos[0]][scroll_offset] is "x":
            return scroll_offset
        
        
        
        
        if verbose:
            str = ""
            for i in range(game_height):
                for j in range(game_width):
                    if scroll_offset < game_width:
                        if i!=player_pos[0] or j!=0:
                            str+=level[i][j+scroll_offset]
                        else:
                            str+="o"
                    else:
                        if i!=player_pos[0] or j!=scroll_offset - game_width:
                            str+=level[i][j+game_width]
                        else:
                            str+="o"
                str+="\n"
            print(str)
            sleep(SLEEP_TIME)

    #if successfully complete the map
    return map_width

if __name__ == "__main__":
    text_file = open(argv[1], "r")
    levels = [[" " for col in range(map_width)] for row in range(map_height)]
    i, j = 0, 0
    while True:
        c = text_file.read(1)
        if c is "\n":
           continue
        if j == 240:
            i+=1           
            j=0
        print(i)
        print(j)
        if i == game_height:
            break
        
        levels[i][j] = c
        j+=1
    text_file.close()
       
    player_behavior = player_behavior_tree([(is_5obstacle_in_way,"smart_selection")])
    print(levels)
    d = simulation(levels, player_behavior.execute, verbose=True)
    print(d)
    # levels = text_file.read().split(',')
    # print(lines)
    