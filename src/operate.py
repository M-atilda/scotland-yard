#file      : operate.py
#date      : 17/02/11
#author    : mi-na
#rational  : this file provides game operate functions


#my module
import src.params as params
from src.Field import *
from src.Player import *
import src.parse_input as pi
from src.climinal import do_climinal_turn
from src.Logger import *


#public module
import os


#interfaces
#turn routine
def routine(turn_num, players_data, map_data, logger):
    new_players_data = []

    new_climinal, climinal_action = do_climinal_turn(turn_num, players_data, map_data, logger)
    new_players_data.append(new_climinal)
    #this check is needed for surrounded situation
    players_data[0] = new_climinal
    if check_game_result(players_data) == "WIN":
        return "WIN", players_data, logger
    logger.updateCliminal(turn_num, players_data, climinal_action)

    logger.dump(turn_num)
    print("turn " + turn_num.__str__())
    for p in players_data:
        p.printPlayer()

    #XXX: execute outer(police) program
    input()
    os.system(params.shell_command())

    next_action_str = ""
    with open('resource/nextAction.txt', 'r') as f:
        next_action_str = f.read()

    try:
        next_action = pi.parse(next_action_str)
        for (i, arg) in enumerate(next_action):
            new_players_data.append(do_police_turn(players_data[1+i], arg, map_data))
        logger.updatePolice(turn_num, new_players_data, next_action)
    except:
        print("ERROR[INVALID INPUT]")
        return "LOSE", [], logger

    #check current game status
    status_code = check_game_result(new_players_data)
    if turn_num == params.max_turn() and status_code == "NEXT":
        status_code == "LOSE"
    return status_code, new_players_data, logger


#helper
# [Player] -> String
def check_game_result(players_data):
    status_code = "NEXT"
    climinal_pos = players_data[0].pos
    for i in range(params.police_amount()):
        if players_data[i+1].pos == climinal_pos:
            status_code == "WIN"
    return status_code

#TODO?: use too many raise sentense
# Player -> {"command": String, "destination": Int} -> Map -> Player
def do_police_turn(police_data, arg, map_data):
    current_node = map_data.getNode(police_data.pos)
    com = arg['command']
    dest = arg['destination']
    if com == "":
        if dest in current_node.next_nodes:
            police_data.useTransportation("")
            police_data.move(dest)
        else:
            raise
    elif com == "STATION":
        if dest in current_node.next_stations:
            police_data.useTransportation("STATION")
            police_data.move(dest)
        else:
            raise
    elif com == "AIRPORT":
        if dest in current_node.next_airports:
            police_data.useTransportation("AIRPORT")
            police_data.move(dest)
        else:
            raise
    else:
        raise
    return police_data

def dump_status(turn_num, players_data):
    if turn_num in params.shown_turn():
        players_data[0].printPlayer()
    for i in range(params.police_amount()):
        players_data[i+1].printPlayer()
