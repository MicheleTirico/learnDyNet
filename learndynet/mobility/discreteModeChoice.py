from learnDyNet.learndynet.setup.config import Config


class DiscreteModeChoice:
    def __init__(self,config,network,individuals):
        self.__config=config
        self.__network=network
        self.__individuals=individuals

def __test(run):
    if run:
        url="/media/mtirico/DATA/project/learnDyNet/learnDyNet/scenarios/grid_01/config.xml"
        c=Config(url)


__test(False)