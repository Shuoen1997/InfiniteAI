from os import system, name
from time import sleep
from colorama import Fore, Style
from msvcrt import getch
import random
import keyboard


OKGREEN = '\033[92m'
ENDC = '\033[0m'
SLEEP_TIME = 0.5
map_height = 20
map_width = 480
game_height = 20
game_width = 120
initial_pos = [5, 3]


# xxxx
# xxxx
# xxxx 

def clear():
    if name == 'nt':
        _ = system('cls')

def random_obstacles(items, prob, amount):
    return random.choices(population=items, weights=prob, k=amount)

def generate_obstacles():
    #generate a list of random DE following the format (type, width, height, posX)
    #the list's length is within..
    elt_num = random.randint(50, 70)
    go = [random.choice([("1_lo_tall_wall", random.randint(1, 4), random.randint(5, 10), random.randint(10, map_width-5)), 
                         ("2_hi_tall_wall", random.randint(1, 4), random.randint(5, 10), random.randint(10, map_width-5)),
                         ("3_lo_short_wall", random.randint(1, 4), random.randint(2, 5), random.randint(10, map_width-5)),
                         ("4_hi_short_wall", random.randint(1, 4), random.randint(2, 5), random.randint(10, map_width-5))]) for i in range(elt_num)]
    return go

def transform_levels(go, levels):
    #transform the DE into actual array elements
    for item in go:
        pos = item[3]
        height = item[2]
        width = item[1]
        if item[0][0] in ["1", "3"]:
            for h in range(len(levels)-height, len(levels)-1):
                for w in range(pos, pos+width):
                    levels[h][w] = "x"
        else:
            for h in range(1, height):
                for w in range(pos, pos+width):
                    levels[h][w] = "x"
                   
def init_levels():
    levels = [random_obstacles([" ", "x"], [0.995, 0.005], map_width) for row in range(map_height)]
    levels[map_height-1][:] = "-" * map_width
    levels[0][:] = "-" * map_width
    transform_levels(generate_obstacles(), levels)
    return levels


def random_behavior(pos):
    #just a placeholder for player behavior, should be replaced by Tyler's BH 
    return max(min(map_height-2, pos+random.randint(-1, 1)), 1)


def simulation(level, verbose):
    #run fast simulation 
    #set verbose to True to print out the process
    #return the distance it has travelled
    player_pos = initial_pos
    scroll_offset = 0
    while scroll_offset < map_width - 1:
        #check if the player has hit obstacle, end game accordingly 
        scroll_offset+=1
        player_pos[0] = random_behavior(player_pos[0])
        if level[player_pos[0]][player_pos[1] + scroll_offset] is "x":
            return scroll_offset
        if verbose is True:
            str = ""
            for i in range(game_height):  
                for j in range(game_width):
                    if i!=player_pos[0] or j!=player_pos[1]:
                        str+=level[i][j+scroll_offset]
                    else:
                        str+=OKGREEN+"o"+ENDC
                str+="\n"
            print(str)
            sleep(SLEEP_TIME)
    #if successfully complete the map, return a large number
    return 10000




if __name__ == "__main__":
    clear()
    sample_size = 20
    levels = [init_levels() for i in range(sample_size)]
    results = []
    for level in levels:
        travel_distance = simulation(level, verbose=False)
        results.append(travel_distance)
    print(results)

        

    
