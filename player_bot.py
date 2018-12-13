from behaviors import *
from checks import *
from bt_nodes import Selector, Sequence, Action, Check

def player_behavior_tree(genome):
    root = Selector(name='Root')

    for ge in genome:
        this_sequence = Sequence(name="sequence")
        stay_action = Action(do_nothing)
        this_sequence.child_nodes = [Check(ge[0]), Action(ge[1])]
        root.child_nodes = [this_sequence, stay_action]


    #print("in player behavior tree")
    return root
