from behaviors.py import *

def player_behavior_tree():

    root = Sequence(name='Root')

    move_strategy = Selector(name = 'Move Strategy')
    move_forward = Action(move_forward)

    obstacle_check = Check(is_obstacle_in_way)
    random_move = Acrion(move_random_vert)

    move_strategy.child_nodes = [obstacle_check, random_move]
    root.child_nodes = [move_strategy, move_forward]

    return root
