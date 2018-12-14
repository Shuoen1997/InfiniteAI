from os import system, name
from colorama import Fore, Style
from msvcrt import getch
from sys import argv
from time import sleep
import random
import time
from PlayerGA import *
from levelGA import *
from player_bot import *




def init_players():
    return Individual(Individual.create_gnome())

def init_levels():
    return Level(Level.create_genome())

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

        

        # if the individual having lowest fitness score ie.
        # 0 then we know that we have reached to the target
        # and break the loop
       
        level_population = sorted(level_population, key=lambda x: x.cal_fitness(player_population))
        player_population = sorted(player_population, key=lambda x: x.cal_fitness(level_population))
        for level in level_population:
            print(level.fitness)
        print(level_population[0].fitness)
        print(level_population[0].chromosome)
        print(player_population[-1].fitness)
        print(player_population[-1].chromosome)
        if level_population[0].fitness < 0.1 and generation > 50:
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
            p_parent1 = random.choice(player_population[:-5])
            p_parent2 = random.choice(player_population[:-5])
            p_child = p_parent1.mate(p_parent2)
            new_player_generation.append(p_child)

        for _ in range(s):
            l_parent1 = random.choice(level_population[:5])
            l_parent2 = random.choice(level_population[:5])
            l_child = l_parent1.mate(l_parent2)
            new_level_generation.append(l_child)


        player_population = new_player_generation
        level_population = new_level_generation
        generation += 1
    
    if len(argv) > 1: #(print)
        with open("levels/" + now + "_" + "best_level" + ".txt", 'w') as f:
            level_to_file(level_population[0].init_level(), f)
