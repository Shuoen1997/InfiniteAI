from behaviors import *
from checks import *
from bt_nodes import Selector, Sequence, Action, Check

def player_behavior_tree(genome):
    print(genome)
    root = Sequence(name='Root')
    # move_strategy = Sequence(name = 'Move Strategy')
    for ge in genome:
        this_sequence = Sequence()
        this_sequence.child_nodes = [ Check(ge[0]), Action(ge[1])]
        root.child_nodes.append(this_sequence)

    
    print("in player behavior tree")

    return root
