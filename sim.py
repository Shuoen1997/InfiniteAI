OKGREEN = '\033[92m'
ENDC = '\033[0m'
SLEEP_TIME = 0.2
map_height = 20
map_width = 240
game_height = 20
game_width = 120
player_x = 3
player_y = 9
from time import sleep

# xxxx
# xxxx
# xxxx

def simulation(level, player, verbose):
    #run fast simulation
    #set verbose to True to print out the process
    #return the distance it has travelled
    player_pos = [player_y, level, 0]
    scroll_offset = 0
    while scroll_offset < map_width - 4:
        #check if the player has hit obstacle, end game accordingly
        scroll_offset+=1
        player(player_pos)
        player_pos[2] = scroll_offset
        if level[player_pos[0]][player_x + scroll_offset] is "x":
            return scroll_offset
        if verbose:
            str = ""
            for i in range(game_height):
                for j in range(game_width):
                    if scroll_offset < game_width:
                        if i!=player_pos[0] or j!=player_x:
                            str+=level[i][j+scroll_offset]
                        else:
                            str+=OKGREEN+"o"+ENDC
                    else:
                        if i!=player_pos[0] or j!=scroll_offset - game_width:
                            str+=level[i][j+game_width]
                        else:
                            str+=OKGREEN+"o"+ENDC
                str+="\n"
            print(str)
            sleep(SLEEP_TIME)

    #if successfully complete the map
    return map_width

