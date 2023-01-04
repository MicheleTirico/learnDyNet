from random import random


class ActionSet:
    def __init__(self,config,stateSet):
        self.__config=config
        self.__stateSet=stateSet
        self.__actionStates={}
        self.__actions=[
                         "ed_1_mode_walk",
                         "ed_1_mode_bike",
                         "ed_1_mode_car",
                         "ed_2_mode_walk",
                         "ed_2_mode_bike",
                         "ed_2_mode_car", #5
                         "ed_1_direction_from-to",
                         "ed_1_direction_to-from",
                         "ed_2_direction_from-to",
                         "ed_2_direction_to-from",
                         "add_1_ed_walk_from-to", #10
                         "add_1_ed_walk_to-from",
                         "add_1_ed_bike_from-to",
                         "add_1_ed_bike_to-from",
                         "add_1_ed_car_from-to",
                         "add_1_ed_car_to-from", #15
                         "rem_1_ed_walk_from-to",
                         "rem_1_ed_walk_to-from",
                         "rem_1_ed_bike_from-to",
                         "rem_1_ed_bike_to-from",
                         "rem_1_ed_car_from-to", #20
                         "rem_1_ed_car_to-from",
                        "rem_2_ed_walk_from-to",
                        "rem_2_ed_walk_to-from",
                        "rem_2_ed_bike_from-to",
                        "rem_2_ed_bike_to-from", #25
                        "rem_2_ed_car_from-to",
                        "rem_2_ed_car_to-from",
                         ]
        self.__config.numActions=len(self.__actions)

    def getAction(self,pos): return self.__actions[pos]
    def getActions(self):       return self.__actions

    def getActionPos(self,action):  return self.__actions.index(action)




