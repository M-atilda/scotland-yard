#file      : Logger.py
#date      : 17/02/12
#author    : mi-na
#rational  : Logger class


#my module
import src.params as params


#data class
class Logger:
    def __init__(self, init_players):
        self.__players = {"0": init_players}
        self.__police_meta = {}
        self.__climinal_meta = {}

    def updatePolice(self, turn_num, players, meta):
        self.__players[turn_num.__str__()] = players
        self.__police_meta[turn_num.__str__()] = meta

    def updateCliminal(self, turn_num, players, meta):
        self.__players[turn_num.__str__()] = players
        self.__climinal_meta[turn_num.__str__()] = meta

    def dump(self, turn_num):
        with open('resource/status.txt', 'w') as f:
            output_contents = self.arrangePlayers(turn_num)
            output_contents = output_contents + "@" + self.__climinal_meta[turn_num.__str__()]['command']
            output_contents = output_contents.replace(" ", "")
            f.write(output_contents)

    #function for the climinal
    def getLog(self):
        return self.__players, self.__climinal_meta, self.__police_meta

    #helper
    def arrangePlayers(self, turn_num):
        str = turn_num.__str__() + "\n"
        if turn_num in params.shown_turn():
            str = str + self.__players[turn_num.__str__()][0].makePrintSentense() + "\n"
        for (i, p) in enumerate(self.__players[turn_num.__str__()][1:]):
            str = str + "[n]" + i.__str__() + p.makePrintSentense() + "\n"
        return str
