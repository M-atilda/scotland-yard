#file      : Field.py
#date      : 17/02/11
#author    : mi-na
#rational  : this file provides the classes which express game_map and its factors


#my module


#public module


#data class
#   __tips          : [start node's id (Int), end node's id (Int)]
#   __attribute     : "" | "STATION" | "AIRPORT"
class Edge:
    # (Int, Int) -> String
    def __init__(self, tips, attribute):
        self.__tips = tips
        self.__attribute = attribute

    #TODO: bit inefficient?
    # (Int, Int)
    @property
    def tips(self):
        return self.__tips
    # String
    @property
    def attribute(self):
        return self.__attribute

    def inverseTip(self, tip_num):
        if tip_num == self.__tips[0]:
            return self.__tips[1]
        else:
            return self.__tips[0]

#data class
#   __id            : id number (Int)
#   __arround_edges : [Edge]
class Node:
    # Int -> [Edge]
    def __init__(self, my_id, arround_edges):
        self.__id = my_id
        self.__arround_edges = arround_edges

    # [Edge]
    @property
    def all_nexts(self):
        return [e.inverseTip(self.__id) for e in self.__arround_edges]
    @property
    def next_nodes(self):
        return [e.inverseTip(self.__id) for e in self.__arround_edges if e.attribute == ""]
    @property
    def next_stations(self):
        return [e.inverseTip(self.__id) for e in self.__arround_edges if e.attribute == "STATION"]
    @property
    def next_airports(self):
        return [e.inverseTip(self.__id) for e in self.__arround_edges if e.attribute == "AIRPORT"]

    #String -> Bool
    def isAttribute(self, kind):
        result = True
        if kind == "":
            if self.next_nodes == []:
                result = False
        elif kind == "STATION":
            if self.next_stations == []:
                result = False
        elif kind == "AIRPORT":
            if self.next_airports == []:
                result = False
        else:
            result = False
        return result

    #FIXME:
    def printNode(self):
        print(self.__id)
        print([(e.tips, e.attribute) for e in self.__arround_edges])

    def makePrintNode(self):
        sentense = self.__id.__str__()
        sentense = sentense + [(e.tips, e.attribute) for e in self.__arround_edges].__str__()
        return sentense

#data class
#   __graph         : [Node]
class Map:
    #[[Edge]]
    def __init__(self, init_data):
        self.__graph = []
        for (i, factor) in enumerate(init_data):
            self.__graph.append(Node(i+1, factor))

    # Int -> Node
    def getNode(self, index):
        return self.__graph[index-1]

    #FIXME:
    def printMap(self):
        for n in self.__graph:
            n.printNode()

    def makePrintMap(self):
        sentense = ""
        for n in self.__graph:
            sentense = sentense + n.makePrintNode() + "\n"
        return sentense

    def makePrintMapSimple(self):
        sentense = ""
        for n in self.__graph:
            sentense = sentense + n.all_nexts.__str__() + "\n"
        return sentense
