#file      : Player.py
#date      : 17/02/11
#author    : mi-na
#rational  : this file provides the classes to maintain players data


#my module
import src.params as params

#public module


#abstract class
#   __occupation    : "POLICE" | "CLIMINAL"
#   __card_set      : ["" | "STATION" | "AIRPORT"]
#   __position      : Int
class Player:
    # String -> [String] -> Int
    def __init__(self, occupation, first_card_set, first_pos):
        self.__occupation = occupation
        self.__card_set = first_card_set
        self.__position = first_pos

    # [String]
    @property
    def cards(self):
        return self.__card_set
    # Int
    @property
    def pos(self):
        return self.__position

    # Bool
    def isPolice(self):
        if self.__occupation == "POLICE":
            return True
        else:
            return False

    # Bool
    def isCliminal(self):
        return (not self.isPolice())

    #TODO: following two methods donot check the action's correctness
    # Int -> Nothing
    def move(self, next_pos):
        self.__position = next_pos

    # String -> Nothing
    def useTransportation(self, kind):
        if not kind in self.__card_set:
            raise

        for (i, card) in enumerate(self.__card_set):
            if kind == card:
                temp_following_cards = self.__card_set[i+1:]
                self.__card_set = self.__card_set[:i]
                self.__card_set.extend(temp_following_cards)
                break

    def makePrintSentense(self):
        sentense = "[r]" + self.__occupation
        sentense = sentense + "[p]" + self.__position.__str__()
        sentense = sentense + "[c]" + self.__card_set.__str__()
        return sentense

#data class
class Police(Player):
    def __init__(self, my_number, first_pos):
        super().__init__("POLICE", params.police_init_cards(), first_pos)
        self.__my_number = my_number

    @property
    def num(self):
        return self.__my_number

    def printPlayer(self):
        print("[n]" + self.__my_number.__str__() + self.makePrintSentense())

#data class
class Climinal(Player):
    def __init__(self, first_pos):
        super().__init__("CLIMINAL", params.climinal_init_cards(), first_pos)

    def printPlayer(self):
        print(self.makePrintSentense())
