from os import system, name
from colorama import Fore, Style
from msvcrt import getch
from sys import argv 
from time import sleep
import random
import keyboard
import time
import level_fitness
from player_bot import *
from PlayerGA import *

OKGREEN = '\033[92m'
ENDC = '\033[0m'
SLEEP_TIME = 0.5
map_height = 20
map_width = 200
game_height = 20
game_width = 120
player_x = 3
player_y = 0


# xxxx
# xxxx 
# xxxx 

def clear():
    if name == 'nt':
        _ = system('cls')

def random_obstacles(items, prob, amount):
    return random.choices(population=items, weights=prob, k=amount)

# def init_designer():
#     #create designer genome, can add more parameters
#     designer_genome = { "ge": [],
#                         "prob_floating_wall": random.randint(1, 20) }
#     for i in range(random.randint(20, 100)):
#         designer_genome["ge"].append(( random.choice(["1_lo_wall", "2_hi_wall"]), random.randint(3, 5), random.randint(7, 14) ) )
#     return designer_genome


def generate_obstacles():
    elt_num = random.randint(20, 100)
    ge = [random.choice([("1_lo_wall", random.randint(1, 4), random.randint(5, 12), random.randint(10, map_width-5)), 
                         ("2_hi_wall", random.randint(1, 4), random.randint(5, 12), random.randint(10, map_width-5)),
                         ("3_lo_short_wall", random.randint(1, 4), random.randint(2, 5), random.randint(10, map_width-5)),
                         ("4_hi_short_wall", random.randint(1, 4), random.randint(2, 5), random.randint(10, map_width-5)),
                         ("5_dust", random.randint(1, 3), random.randint(1, 3), (random.randint(1, 16), random.randint(10, map_width - 5)))]) for i in range(elt_num)]
    return ge

def level_metrices():
    pass


def transform_levels(ge, levels):
    #transform the DE into actual array elements
    for item in ge:
        pos = item[3]
        height = item[2]
        width = item[1]
        if item[0][0] in ["1", "3"]:
            for h in range(len(levels)-height, len(levels)-1):
                for w in range(pos, pos+width):
                    levels[h][w] = "x"
        elif item[0][0] in ["2", "4"]:
            for h in range(1, height):
                for w in range(pos, pos+width):
                    levels[h][w] = "x"
        else:
            for h in range( height ):
                for w in range( width ):
                    levels[pos[0] + h][pos[1] + w] = "x"
                   
def init_levels():
    levels = [[" " for col in range(map_width)] for row in range(map_height)]
    levels[map_height-1][:] = "-" * map_width
    levels[0][:] = "-" * map_width
    ge = generate_obstacles()
    transform_levels(ge, levels)
    #print(ge)
    return levels

def init_players():
    return Individual(Individual.create_gnome())

def random_behavior(pos):
    #just a placeholder for player behavior, should be replaced by Tyler's BT
    return random.randint(-2, 2)


def simulation(level, player, verbose):
    #run fast simulation 
    #set verbose to True to print out the process
    #return the distance it has travelled
    player_pos = [player_y]
    scroll_offset = 0
    success, failure = 1.0, 0.0
    while scroll_offset < game_width - 1:
        #check if the player has hit obstacle, end game accordingly 
        scroll_offset+=1
        print(player(player_pos))
        # player_pos = max(min(map_height-2, player_pos + random.randint(-2, 2)), 1)
        # player_pos = player(player_pos)
        if level[player_pos[0]][player_x + scroll_offset] is "x":
            return failure, scroll_offset
        if verbose:
            str = ""
            for i in range(game_height):  
                for j in range(game_width):
                    if i!=player_pos[0] or j!=player_x:
                        str+=level[i][j+scroll_offset]
                    else:
                        str+=OKGREEN+"o"+ENDC
                str+="\n"
            print(str)
            sleep(SLEEP_TIME)
    #if successfully complete the map, return a large number
    return success, map_width

def level_to_file(level, file):
    for row in level:
        file.write("".join(row) + "\n")



if __name__ == "__main__":
    clear()
    sample_size = 2
    results = []
    levels = [init_levels() for i in range(sample_size)]
    players = [init_players() for i in range(sample_size)]
    now = time.strftime("%m_%d_%H_%M_%S")
    success_rate = 0
    for level in levels:
        for player in players:
            player_behavior = player_behavior_tree(player.chromosome)
            print(player_behavior)
            success, travel_distance = simulation(level, player_behavior.execute, verbose=True)
            success_rate += success
            solvability = level_fitness.metrices(level)
            if len(argv) > 1: #(print)
                with open("levels/" + now + "_" + str(levels.index(level)) + ".txt", 'w') as f:
                    level_to_file(level, f)
            results.append((levels.index(level), travel_distance, solvability))
    print(results)

        

    
