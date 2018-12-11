from heapq import heappush, heappop

def metrices(level):
    return has_valid_path(level)

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
def has_valid_path(level):
    game_width = len(level[0])
    for w in range(game_width):
        if not passable(level, 1, w):
            return 0.0
    return 1.0

def passable(level, h, w):
    while h < len(level)-1:
        if level[h][w] is "x":
            h+=1
        else:
            return True
    return False
        
        
