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
from levelGA import *

OKGREEN = '\033[92m'
ENDC = '\033[0m'
SLEEP_TIME = 0.5
map_height = 20
map_width = 240
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




def init_players():
    return Individual(Individual.create_gnome())

def init_levels():
    return Level()

def random_behavior(pos):
    #just a placeholder for player behavior, should be replaced by Tyler's BT
    return random.randint(-2, 2)


def simulation(level, player, verbose):
    #run fast simulation 
    #set verbose to True to print out the process
    #return the distance it has travelled
    player_pos = [player_y]
    scroll_offset = 0
    while scroll_offset < game_width - 1:
        #check if the player has hit obstacle, end game accordingly 
        scroll_offset+=1
        print(player(player_pos))
        # player_pos = max(min(map_height-2, player_pos + random.randint(-2, 2)), 1)
        # player_pos = player(player_pos)
        if level[player_pos[0]][player_x + scroll_offset] is "x":
            return scroll_offset
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
    return map_width

def level_to_file(level, file):
    for row in level:
        file.write("".join(row) + "\n")



if __name__ == "__main__":
    clear()
    sample_size = 20
    results = []
    level_population = [init_levels() for i in range(sample_size)]
    level_population = sorted(level_population, key=lambda x: x.fitness)
    player_population = [init_players() for i in range(sample_size)]
    generation = 0
    now = time.strftime("%m_%d_%H_%M_%S")
    while True:
        for level in level_population:
            for player in player_population:
                player_behavior = player_behavior_tree(player.chromosome)
                print(player_behavior)
                travel_distance = simulation(level.chromosome, player_behavior.execute, verbose=True)
                # if len(argv) > 1: #(print)
                #     with open("levels/" + now + "_" + str(level_population.index(level)) + ".txt", 'w') as f:
                #         level_to_file(level, f)
                results.append((level_population.index(level), travel_distance, solvability))
    print(results)

        

    
