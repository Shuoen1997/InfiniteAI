from os import system, name
from colorama import Fore, Style
from msvcrt import getch
from sys import argv 
from time import sleep
import random
import keyboard
import time
import level_fitness


OKGREEN = '\033[92m'
ENDC = '\033[0m'
SLEEP_TIME = 0.5
map_height = 20
map_width = 480
game_height = 20
game_width = 120
initial_pos = [10, 3]


# xxxx
# xxxx
# xxxx 

def clear():
    if name == 'nt':
        _ = system('cls')

def random_obstacles(items, prob, amount):
    return random.choices(population=items, weights=prob, k=amount)

def init_designer():
    #create designer genome, can add more parameters
    designer_genome = { "element_number": random.randint(20, 100),
                        "walls_weight": [random.randint(1, 4), random.randint(1, 4), random.randint(1, 4), random.randint(1, 4)],
                        "prob_floating_wall": random.randint(1, 20) }
    return designer_genome


def generate_obstacles(designer):
    #the designer will generate a list of random DE following the format (type, width, height, posX)
    #still random so the levels the same designer creates still has variety 
    elt_num = designer["element_number"]
    ge = [random.choice([("1_lo_tall_wall", random.randint(1, 4), random.randint(5, 12), random.randint(10, map_width-5)), 
                         ("2_hi_tall_wall", random.randint(1, 4), random.randint(5, 12), random.randint(10, map_width-5)),
                         ("3_lo_short_wall", random.randint(1, 4), random.randint(2, 5), random.randint(10, map_width-5)),
                         ("4_hi_short_wall", random.randint(1, 4), random.randint(2, 5), random.randint(10, map_width-5))]) for i in range(elt_num)]
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
        else:
            for h in range(1, height):
                for w in range(pos, pos+width):
                    levels[h][w] = "x"
                   
def init_levels(designer):
    prob = designer["prob_floating_wall"] / 1000
    levels = [random_obstacles([" ", "x"], [1 - prob, prob], map_width) for row in range(map_height)]
    levels[map_height-1][:] = "-" * map_width
    levels[0][:] = "-" * map_width
    ge = generate_obstacles(designer)
    transform_levels(ge, levels)
    #print(ge)
    return levels


def random_behavior(pos):
    #just a placeholder for player behavior, should be replaced by Tyler's BT
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

def level_to_file(level, file):
    for row in level:
        file.write("".join(row) + "\n")



if __name__ == "__main__":
    clear()
    sample_size = 2
    designers = [init_designer() for i in range(sample_size)]
    results = []
    for designer in designers:
        levels = [init_levels(designer) for i in range(100)]
        
        now = time.strftime("%m_%d_%H_%M_%S")
        designer_result = ["designer" + str(designers.index(designer)) + ":"]
        # designer_result.append(designer)
        dis, sov = 0, 0
        for level in levels:
            travel_distance = simulation(level, verbose=False)
            solvability = level_fitness.metrices(level, initial_pos)
            # designer_result.append((travel_distance, solvability))
            dis += travel_distance
            sov += solvability
            if len(argv) > 1: #(print)
                with open("levels/" + now + "_" + str(levels.index(level)) + ".txt", 'w') as f:
                    level_to_file(level, f)
        
        designer_result.append("average distance: " + str(dis/10) + ", average sov: " + str(sov/10))
        results.append(designer_result)
    print(results)

        

    
