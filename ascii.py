from os import system, name
from colorama import Fore, Style
from msvcrt import getch
from sys import argv 
from time import sleep
import random
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

def init_players():
    return Individual(Individual.create_gnome())

def init_levels():
    return Level()


def simulation(level, player, verbose):
    #run fast simulation 
    #set verbose to True to print out the process
    #return the distance it has travelled
    player_pos = [player_y]
    scroll_offset = 0
    while scroll_offset < game_width - 1:
        #check if the player has hit obstacle, end game accordingly 
        scroll_offset+=1
        player(player_pos)
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
    
    #if successfully complete the map
    return map_width

def level_to_file(level, file):
    for row in level:
        file.write("".join(row) + "\n")

def clear():
    if name == 'nt':
        _ = system('cls')


if __name__ == "__main__":
    clear()
    sample_size = 20
    level_population = [init_levels() for i in range(sample_size)] 
    player_population = [init_players() for i in range(sample_size)]
    generation = 0
    now = time.strftime("%m_%d_%H_%M_%S")
    while True:
        #run through the simulation to get the fitness score 
        for level in level_population:
            for player in player_population:
                player_behavior = player_behavior_tree(player.chromosome)
                # print(player_behavior)
                travel_distance = simulation(level.chromosome, player_behavior.execute, verbose=False)
                # calculate the fitness 
                player.fitness += ( travel_distance / map_width ) / sample_size
                level.fitness += ( travel_distance / map_width ) / sample_size
         

        level_population = sorted(level_population, key=lambda x: x.fitness)
        player_population = sorted(player_population, key=lambda x: x.fitness)
        
        # if the individual having lowest fitness score ie.
        # 0 then we know that we have reached to the target
        # and break the loop
        if player_population[0].fitness >= 0.8:
            break

        # if the individual having lowest fitness score ie.
        # 0 then we know that we have reached to the target
        # and break the loop
        # if population[0].fitness <= 0:
        #     found = True
        #     break

        # Otherwise generate new offsprings for new generation
        new_player_generation, new_level_generation = [], []

        # Perform Elitism, that mean 10% of fittest population
        # goes to the next generation
        s = int((10 * sample_size ) / 100)
        new_player_generation.extend(player_population[:s])
        new_level_generation.extend(level_population[:s])

        # From 50% of fittest population, Individuals
        # will mate to produce offspring
        s = int((90 * sample_size) / 100)
        for _ in range(s):
            parent1 = random.choice(player_population[:50])
            parent2 = random.choice(player_population[:50])
            child = parent1.mate(parent2)
            new_player_generation.append(child)

        player_population = new_player_generation
        generation += 1

        

    # # if len(argv) > 1: #(print)
    # #     with open("levels/" + now + "_" + str(level_population.index(level)) + ".txt", 'w') as f:
    # #         level_to_file(level, f)
    # results.append((level_population.index(level), travel_distance))
    # print(results)

        

    
