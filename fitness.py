from heapq import heappush, heappop
from sim import *
from player_bot import *
from math import pow

ipr = 0.6

def level_metrices(level, player_pop):
    success = 0
    for player in player_pop:
        player_behavior = player_behavior_tree(player.chromosome)
        distance_travelled = simulation(level, player_behavior.execute, verbose=False)
        if distance_travelled > map_width - 4:
            success +=1
    pass_rate = success / len(player_pop)
    return 1 * has_valid_path(level) + 10 * abs(ipr - pass_rate) 

def player_metrices(player, level_pop):
    overall_travel_dis = 0
    player_behavior = player_behavior_tree(player.chromosome)
    for level in level_pop:
        distance_travelled = simulation(level.init_level(), player_behavior.execute, verbose=False)
        overall_travel_dis += distance_travelled
    
    pass_cap = overall_travel_dis / ( map_width * len(level_pop) ) 
    return pass_cap


def has_valid_path(level):
    game_width = len(level[0])
    for w in range(game_width):
        if not passable(level, 1, w):
            return 999.0
    return 0.0

def passable(level, h, w):
    while h < len(level)-1:
        if level[h][w] is "x":
            h+=1
        else:
            return True
    return False
        
        
# def get_neighbors(level, pos):
#     neighbors = []
#     for move in [-1, 0, 1]:
#         neighbor = level[pos[0] + move][pos[1] + 1]
#         if neighbor is " ":
#             neighbors.append((pos[0] + move, pos[1] + 1 ))
#     return neighbors 


# def has_valid_path(level, pos):
#     game_width = len(level[pos[0]])
#     queue = []
#     visited = []
#     heappush(queue, (0, pos)) #[[5, 3],]
#     while queue:
#         current = heappop(queue)
#         visited.append(current)
#         current_pos_x = current[1][1]
#         if current_pos_x > game_width -2:
#             return 1.0
#         for next_pos in get_neighbors(level, current[1]):
#             heu = game_width - current_pos_x
#             next = (heu, next_pos)
#             if next not in visited:
#                 heappush(queue, next)   
#     return 0.0
