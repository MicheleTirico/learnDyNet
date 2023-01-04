import csv

from matplotlib import pyplot as plt


class PlotRewardPerAgent:
    def __init__(self,config,agents):
        self.__config=config
        self.__agents=agents

    def getPlot(self):
        print ("plot image")
        fields=[]

        rows=[]

        with open (self.__config.path_agentsReward,"r") as f:
            csvreader=csv.reader(f)
            fields=next(csvreader)

            for r in csvreader:rows.append(r)

            x=[float(_) for _ in range(len(rows[0]))]
            plt.xlabel("x")
            plt.ylabel("y")
            plt.legend()
        #    plt.xticks([_ for _ in range(0,len(rows[0]),10) ])
            plt.title("reward per agent")
            for y in rows:
                y=[float(_) for _ in y]
                plt.plot(x,y)



            plt.show()

