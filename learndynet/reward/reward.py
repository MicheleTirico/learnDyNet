import networkx as nx


class Reward:
    def __init__(self,config,network,individuals,agents):
        self.__config=config
        self.__network=network
        self.__individuals=individuals
        self.__agents=agents

    def computeReward(self,step):
        G=self.__network.getGraph()
        list_ed_state=[]
        num_ind=[]
        mapEdges={}
        # compute reward and set vals
        for id , individual in self.__individuals.getIndividuals().items():
            utilities=individual.getUtilities()
            utility,posMode=self.__getMaxMode(utilities)
            if type(utility)!=str:
                sp=individual.getSp()[posMode]
                for t in sp:
                    i=1
                    while i < len(t):
                        edge=(t[i-1],t[i])
                        agent=self.__agents.getAgent(edge[0],edge[1])

                        old_num_ind=agent.get_num_ind_pos(step)
                        new_num_ind=old_num_ind+1
                        agent.set_num_ind(step,new_num_ind)

                        old_sum_utility=agent.get_sum_utility_pos(step)
                        new_sum_utility=round(old_sum_utility+utility,2)
                        agent.set_sum_utility(step,new_sum_utility)
                    #    print (agent.get_num_ind(),agent.get_sum_utility())
                        i+=1

        self.__agents.updateReward(step)
#        for id,agent in self.__agents.getAgents().items():print (id,agent.get_reward(),agent.get_num_ind(),agent.get_sum_utility())



    def computeRewardold2(self,step):
        G=self.__network.getGraph()
        list_ed_state=[]
        num_ind=[]
        mapEdges={}
        # compute reward and set vals
        for id , individual in self.__individuals.getIndividuals().items():
            utilities=individual.getUtilities()
            utility,posMode=self.__getMaxMode(utilities)
            if type(utility)!=str:
                sp=individual.getSp()[posMode]
                for t in sp:
                    i=1
                    while i < len(t):
                        edge=(t[i-1],t[i])
                        try:
                            num_ind_old=mapEdges[edge]["num_ind"][step]
                            sum_utility_old=mapEdges[edge]["sum_utility"][step]
                            num_ind_new=num_ind_old+1
                            sum_utility_new=sum_utility_old+utility

                            mapEdges[edge]["num_ind"]=[num_ind_new]
                            mapEdges[edge]["sum_utility"]=[sum_utility_new]
                            mapEdges[edge]["reward"]=[round(sum_utility_new/num_ind_new,3)]

                        except KeyError:
                            mapEdges[edge]={"num_ind":[1],"sum_utility":[utility],"reward":[utility]}
                        except IndexError:
                            num_ind_old=mapEdges[edge]["num_ind"]
                            sum_utility_old=mapEdges[edge]["sum_utility"]
                            reward_old=mapEdges[edge]["reward"]
                            num_ind_old.append(1)
                            sum_utility_old.append(utility)

                            print (reward_old)
                            mapEdges[edge]["num_ind"]=num_ind_old
                            mapEdges[edge]["sum_utility"]=sum_utility_old
                            mapEdges[edge]["reward"]=reward_old.append(round(utility,3))
                        i+=1

        # set vals in edges
        for edge in G.edges:
           # print (edge)
            try:
                vals=mapEdges[(edge[0],edge[1])]
            #    print (vals)
                G.edges[edge]["num_ind"]=vals["num_ind"]
                G.edges[edge]["sum_utility"]=vals["sum_utility"]
                G.edges[edge]["reward"]=vals["reward"]
            except KeyError:        pass#    print ("no edge")


    def computeRewardold(self,step):
        G=self.__network.getGraph()
        list_ed_state=[]
        num_ind=[]
        for id , individual in self.__individuals.getIndividuals().items():
            utilities=individual.getUtilities()
            reward,posMode=self.__getMaxMode(utilities)

            if type(reward)!=str:
                sp=individual.getSp()[posMode]
                for trip in sp:
                    i=1
                    while i < len(trip):
                        e_state=0
                        e=(trip[i-1],trip[i])
                        e0=G.adj[trip[i-1]][trip[i]].items()
                        #                        e0=list(G.adj[trip[i-1]][trip[i]].items())
                        fun="sim"
                        for ed in e0:
                            function_edge=ed[1]["edge_function"]
                            if function_edge=="state":
                                e_state=ed
                                fun="state"
                        if fun=="sim":
                            e1=G.adj[trip[i]][trip[i-1]].items()
                            #                            e1=list(G.adj[trip[i]][trip[i-1]].items())
                            for ed in e1:
                                function_edge=ed[1]["edge_function"]
                                if function_edge=="state":
                                    e_state=ed


                        #print ("e state",e_state,type(e_state))
                        list_ed_state.append(e_state)
                        num_ind.append(1)
                        print (e_state,type(e_state))
                        G[e_state]["ciao"]=3

                        i+=1

        for e in list(G.edges):
            print (e)
            l=G.edges[e]
            print (l)




    def __getMaxMode(self,utilities):    #    print (utilities)

        valNull= -10000
        listVals=[]
        if utilities[0][0]==0 or utilities[0][1]==0:    listVals.append(valNull)
        else: listVals.append( utilities[0][0]+ utilities[0][1])
        if utilities[1][0]==0 or utilities[1][1]==0:    listVals.append(valNull)
        else: listVals.append( utilities[1][0]+ utilities[1][1])
        if utilities[2][0]==0 or utilities[2][1]==0:    listVals.append(valNull)
        else: listVals.append( utilities[2][0]+ utilities[2][1])    #    print (listVals)

        maxVal=max(listVals)
        posMaxVal=listVals.index(max(listVals))

        if maxVal < -100:   return "noval","nopos"
        else:               return maxVal,posMaxVal







