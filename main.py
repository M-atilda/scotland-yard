##
# @file      : main.py
# @date      : 17/02/12
# @author    : mi-na


# my module
from src.init import initialize
import src.params as params
import src.operate as ope
from src.Logger import Logger

# public module
# nothing


##! main process
if __name__ == '__main__':
    ## @brief initialize
    g_map, g_players = initialize()
    g_map.printMap()
    print("turn 0")
    for p in g_players:
        p.printPlayer()
    g_logger = Logger(g_players)

    ## @brief routine
    status_code = "NEXT"
    for i in range(params.max_turn()):
        status_code, g_players, g_logger = ope.routine(i+1, g_players, g_map, g_logger)
        if not status_code == "NEXT":
            break
    print(status_code)
