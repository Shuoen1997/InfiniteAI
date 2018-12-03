from heapq import heappush, heappop

def metrices(level, pos):
    # solvability = 0.0
    # if has_valid_path(level, pos):
    #     solvability = 1.0
    return 1.0 if has_valid_path(level, pos) else 0.0

def get_neighbors(level, pos):
    neighbors = []
    for move in [-1, 0, 1]:
        # print(move)
        # print(pos[0] + move)
        # print(pos[1] + 1)
        # print(level[4][4])
        neighbor = level[pos[0] + move][pos[1] + 1]
        if neighbor is " ":
            neighbors.append((pos[0] + move, pos[1] + 1 ))
    return neighbors 


def has_valid_path(level, pos):
    game_width = len(level[pos[0]])
    queue = []
    visited = []
    heappush(queue, (0, pos)) #[[5, 3],]
    while queue:
        current = heappop(queue)
        visited.append(current)
        current_pos_x = current[1][1]
        if current_pos_x > game_width -2:
            return True
        for next_pos in get_neighbors(level, current[1]):
            heu = game_width - current_pos_x
            next = (heu, next_pos)
            if next not in visited:
                heappush(queue, next)
            # else:
            #     # print("WTF")
    
    return False


        
        

