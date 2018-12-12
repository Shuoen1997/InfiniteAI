from behaviors import *
from checks import *
from bt_nodes import Selector, Sequence, Action, Check

def player_behavior_tree(genome):
    print(genome)
    root = Sequence(name='Root')
    move_strategy = Sequence(name = 'Move Strategy')
    

    obstacle_check = Check(genome[0][0])
    random_move = Action(genome[0][1])

    move_strategy.child_nodes = [obstacle_check, random_move]
    root.child_nodes = [move_strategy]
    print("in player behavior tree")

    return root
