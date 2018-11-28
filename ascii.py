from os import system, name
from time import sleep
from colorama import Fore, Style
from msvcrt import getch
import random
import keyboard


OKGREEN = '\033[92m'
ENDC = '\033[0m'
SLEEP_TIME = 0.5
_height = 20
_width = 120
elt_num = 15
# xxxx
# xxxx
# xxxx 

def clear():
    if name == 'nt':
        _ = system('cls')

def random_obstacles(items, prob, amount):
    return random.choices(population=items, weights=prob, k=amount)

def generate_obstacles():
    #(type, width, height, posX)

    go = [random.choice([("low_wall", random.randint(1, 3), random.randint(2, 9), random.randint(10, _width-5)), 
                         ("up_wall", random.randint(1, 3), random.randint(2, 9), random.randint(10, _width-5))]) for i in range(elt_num)]
    return go
def transform_levels(go, levels):
    for item in go:
        pos = item[3]
        # print("pos", pos)
        height = item[2]
        width = item[1]
        if item[0] is "low_wall":
            print("True")
            for h in range(len(levels)-height, len(levels)-1):
                for w in range(pos, pos+width):
                    levels[h][w] = "x"
        else:
            for h in range(1, height):
                for w in range(pos, pos+width):
                    levels[h][w] = "x"
                   
def init_levels():
        levels = [random_obstacles([" ", "^", "x"], [1.0, 0.0, 0.0], _width) for row in range(_height)]
        levels[_height-1][:] = "-" * _width
        levels[0][:] = "-" * _width
        return levels

def update_levels(levels, next_levels):       
        for i in range(1, _height-1):
            for j in range(_width):
                # print(self.levels[i][j])
                levels[i][j-1] = levels[i][j]
                if j==_width-1:
                    levels[i][j] = next_levels[i].pop()
    

if __name__ == "__main__":
    clear()
    obstacles = generate_obstacles()
    next_obstacles = generate_obstacles()
    levels = init_levels()
    next_levels = init_levels()
    transform_levels(next_obstacles, next_levels)
    transform_levels(obstacles, levels)    
    scroll = _width
    player_pos = [5, 3]
    while True:
        update_levels(levels, next_levels)
        player_pos[0] += random.randint(-1, 1)
        #check if the player has hit obstacle, end game accordingly 
        if levels[player_pos[0]][player_pos[1]] is "x":
            print("GAME OVER")
            break
        #print out the current state of the game
        str = ""
        for i in range(_height):  
            for j in range(_width):
                if i!=player_pos[0] or j!=player_pos[1]:
                    str+=levels[i][j]
                else:
                    str+=OKGREEN+"o"+ENDC
            str+="\n"
        print(str)
        #update scroll value and when it's 0, create a new set of obstacles 
        scroll -= 1
        if scroll == 0:
            next_levels = init_levels()
            next_obstacles = generate_obstacles()
            transform_levels(next_obstacles, next_levels)
            scroll = _width
        #sleep interval 
        sleep(SLEEP_TIME)
        

    
