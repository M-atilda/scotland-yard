#file      : init.py
#date      : 17/02/11
#author    : mi-na
#rational  : this file provides interfaces for initialization of map and players


#my module
from src.Field import *
from src.Player import *
import src.params as params


#public module
import random


#interfaces
# (Map, [Player])
def initialize():
    return get_game_map(), get_players(get_game_map())

_is_map_initialized = False
_g_map = None
_is_players_initialized = False
_g_players = []

# Map
def get_game_map():
    global _g_map
    global _is_map_initialized
    if not _is_map_initialized:
        _g_map = Map(get_init_data())
        _is_map_initialized = True
        dump_game_map(_g_map)
        #dump_game_map_simple(_g_map)
    else:
        pass
    return _g_map

# [Player]
def get_players(map_data):
    global _g_players
    global _is_players_initialized
    if not _is_map_initialized:
        raise "ERROR [INITIALIZE]"
    if not _is_players_initialized:
        initial_positions = decide_players_pos(map_data)
        _g_players.append(Climinal(initial_positions[0]))
        for i in range(params.police_amount()):
            _g_players.append(Police(i+1, initial_positions[i+1]))
        _is_players_initialized = True
    else:
        pass
    return _g_players

#helper functions
# [Edge]
def get_init_data():
    init_data_origin = get_init_data_origin()
    init_data_modified = remove_island(init_data_origin)
    return arrign_init_data(init_data_modified)

# Edge -> Edge -> Bool
def is_same_edge(first, second):
    if first.attribute != second.attribute:
        return False

    if first.tips[0] == second.tips[0]:
        if first.tips[1] == second.tips[1]:
            return True
    elif first.tips[0] == second.tips[1]:
        if first.tips[1] == second.tips[0]:
            return True
    return False

# String
def decide_attr():
    attr = ""
    randval = random.randint(0, 99)
    if randval < params.airport_prob():
        attr = "AIRPORT"
    elif randval < params.station_prob() + params.airport_prob():
        attr = "STATION"
    return attr

# [Edge]
def get_init_data_origin():
    init_data = []
    for i in range(params.nodes_amount()):
        end_pos = random.randint(1, params.nodes_amount())
        while (i+1) == end_pos:
            end_pos = random.randint(1, params.nodes_amount())
        init_data.append(Edge([i+1, end_pos], decide_attr()))

    extra_edge_amount = (params.nodes_amount() // 2) + random.randint(1, params.nodes_amount())
    for i in range(extra_edge_amount):

        first_pos = random.randint(1, params.nodes_amount())
        second_pos = random.randint(1, params.nodes_amount())
        while first_pos == second_pos:
            second_pos = random.randint(1, params.nodes_amount())
        temp_tips = [first_pos, second_pos]

        init_data.append(Edge(temp_tips, decide_attr()))
    return init_data

# [Edge] -> [Edge]
def remove_island(init_data_origin):
    # get the graph include the node_1
    node_1_arrounds = []
    for e in init_data_origin:
        if e.tips[0] == 1:
            node_1_arrounds.append(e.tips[1])
        elif e.tips[1] == 1:
            node_1_arrounds.append(e.tips[0])
    node_1_graph_member = get_connected_nodes(node_1_arrounds, [], init_data_origin)

    init_data_remaked = init_data_origin
    while not len(node_1_graph_member) == params.nodes_amount():
        #TODO: more efficient
        #serch the node unreached from node_1
        for i in range (params.nodes_amount()):
            if not (i+1) in node_1_graph_member:
                nth = random.randint(1, len(node_1_graph_member))
                init_data_remaked.append(Edge([i+1, node_1_graph_member[nth-1]], ""))
                node_1_graph_member = get_connected_nodes(node_1_arrounds, [], init_data_remaked)
                break
    return init_data_remaked

def get_connected_nodes(remaining_targets, reached_places, init_data_origin):
    # there is no nodes remaining you can reach from node_1
    if remaining_targets == []:
        return reached_places

    if remaining_targets[0] in reached_places:
        return get_connected_nodes(remaining_targets[1:], reached_places, init_data_origin)
    else:
        nexts = []
        for e in init_data_origin:
            if e.tips[0] == remaining_targets[0]:
                nexts.append(e.tips[1])
            elif e.tips[1] == remaining_targets[0]:
                nexts.append(e.tips[0])
        reached_places.append(remaining_targets[0])
        remaining_targets = remaining_targets[1:]
        remaining_targets.extend(nexts)
        return get_connected_nodes(remaining_targets, reached_places, init_data_origin)

# [Edge] -> [[Edge]]
def arrign_init_data(modified_init_data):
    comp_init_data = []
    for i in range(params.nodes_amount()):
        temp_arrounds = []
        for e in modified_init_data:
            if e.tips[0] == (i+1) or e.tips[1] == (i+1):
                temp_arrounds.append(e)
        comp_init_data.append(temp_arrounds)
    return comp_init_data

# Map -> [Int]
def decide_players_pos(map_data):
    positions = []
    positions.append(random.randint(1, params.nodes_amount()))

    #TODO: too nesting
    for i in range(params.police_amount()):
        candidate_pos = random.randint(1, params.nodes_amount())

        #search other candidate if the suggested pos is too near with other positions already decided
        suitable_pos_flag = False
        while not suitable_pos_flag:
            too_near = False
            for pos in positions:
                if pos in map_data.getNode(candidate_pos).all_nexts:
                    too_near = True
            if too_near:
                candidate_pos = random.randint(1, params.nodes_amount())
            else:
                suitable_pos_flag = True

        positions.append(candidate_pos)
    return positions

def dump_game_map(map_data):
    with open('resource/map_data.txt', 'w') as f:
        f.write(map_data.makePrintMap().replace(" ", "").replace("],", "]").replace("),(", ")*("))

def dump_game_map_simple(map_data):
    with open('resource/map_data_simple.txt', 'w') as f:
        f.write(map_data.makePrintMapSimple())
