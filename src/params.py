#file      : params.py
#date      : 17/02/11
#author    : mi-na
#rational  : this file includes classes for providing parameters

#player
_police_init_cards = ["", "", "", "", "", "", "STATION", "STATION", "STATION", "AIRPORT", "AIRPORT"]
_climinal_init_cards = ["", "", "", "", "", "STATION", "STATION", "STATION", "STATION", "AIRPORT", "AIRPORT", "AIRPORT"]
def police_init_cards():
    global _police_init_cards
    return _police_init_cards
def climinal_init_cards():
    global _climinal_init_cards
    return _climinal_init_cards

#map
_nodes_amount = 60
_police_amount = 4
_station_prob = 20
_airport_prob = 5

def nodes_amount():
    global _nodes_amount
    return _nodes_amount
def police_amount():
    global _police_amount
    return _police_amount
def station_prob():
    global _station_prob
    return _station_prob
def airport_prob():
    global _airport_prob
    return _airport_prob

#meta
_max_turn = 12
_shown_turn = [3, 8, 14, 20, 24]
def max_turn():
    global _max_turn
    return _max_turn
def shown_turn():
    global _shown_turn
    return _shown_turn

_shell_command = "java Main"
def shell_command():
    global _shell_command
    return _shell_command
