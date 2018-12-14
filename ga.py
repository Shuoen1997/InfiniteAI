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
    return Level()

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
        if generation > 0:
            break
        level_population = sorted(level_population, key=lambda x: x.cal_fitness(player_population))
        player_population = sorted(player_population, key=lambda x: x.cal_fitness(level_population))
        print(level_population[-1].fitness)
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
