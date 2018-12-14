from behaviors import *
from checks import *
from bt_nodes import Selector, Sequence, Action, Check

def player_behavior_tree(genome):
    root = Selector(name='Root')

    for ge in genome:
        this_sequence = Sequence(name="sequence")
        stay_action = Action(do_nothing)
        root.child_nodes = [this_sequence, stay_action]

        #smart_selection
        if ge[1] == "smart_selection":
            print("smart_select")
            smart_selection = Selector(name="smart_select")
            top_check_sequence= Sequence(name="top_sequence")
            bot_check_sequence= Sequence(name="bot_sequence")
            top_opening_check = Check(is_top_opening)
            top_move_action = Action(move_top_opening)
            top_check_sequence.child_nodes = [top_opening_check,top_move_action]
            bot_opening_check= Check(is_bottom_opening)
            bot_move_action = Action(move_bottom_opening)
            bot_check_sequence.child_nodes = [bot_opening_check,bot_move_action]
            smart_selection.child_nodes = [top_check_sequence, bot_check_sequence]
            this_sequence.child_nodes = [Check(ge[0]), smart_selection]
        #random_selection
        else:
            this_sequence.child_nodes = [Check(ge[0]), Action(ge[1])]



    #print("in player behavior tree")
    return root
