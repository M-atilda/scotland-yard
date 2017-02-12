#file      : climinal.py
#date      : 17/02/12
#author    : mi-na
#rational  : climinal's action


#my module
import src.params as params
from src.Field import *
from src.Player import *
from src.Logger import *


def do_climinal_turn(turn_num, players_data, map_data, logger):
    my_pos = players_data[0].pos
    my_arrounds = map_data.getNode(my_pos).next_nodes
    dest = my_arrounds[0]
    players_data[0].move(dest)
    players_data[0].useTransportation("")
    return players_data[0], {"command": "", "destination": dest}
