import csv

class StoreAgents:
    def __init__(self,config,agents):
        self.__config=config
        self.__agents=agents

    def compute(self):
        print ("compute store agents")
        with open(self.__config.path_agentsReward,"w") as csvfile:
            csvwriter=csv.writer(csvfile)
            csvwriter.writerow(["id"]+[str(i) for i in range(self.__config.numStep)])
            for id,agent in self.__agents.getAgents().items():
                rewards=agent.get_reward()
                line =[str(id)]+[_ for _ in rewards]
                csvwriter.writerow(line)
