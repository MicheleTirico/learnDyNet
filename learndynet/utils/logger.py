import datetime
import sys

class Logger:
    def __init__(self,IDsim):
        self.__IDsim=IDsim

    def setDisplay(self,displayLog,displayWarning,displayError,displayStateSim):
        self.__displayLog=displayLog
        self.__displayWarning=displayWarning
        self.__displayError=displayError
        self.__displayStateSim=displayStateSim

    def log (self,cl,method,message):
        if self.__displayLog:       self.__completeMessage("LOG",cl,method,message)
    #        try:
    #       except AttributeError:  self.error(cl=self,method=sys._getframe(),message="no config is set",error=AttributeError)

    def warning (self,cl,method,message):
        if self.__displayWarning:  self.__completeMessage("WAR",cl,method,message)

    def warningExc (self,cl,method,message,exception):
        message+=" (exception: "+str(exception.__name__)+ ")"
        if self.__displayWarning:  self.__completeMessage("WAR",cl,method,message)

    def error (self,cl,method,message,error):
        try: message+=" (error: "+str(error.__name__)+ ")"
        except AttributeError: message+=" (error: "+error+ ")"
        if self.__displayError:  self.__completeMessage("ERR",cl,method,message)

    def displayState (self,step,message):
        if self.__displayStateSim:
            print ("#--------------------------------------------",
                   str(datetime.datetime.now())+ " simulation "+self.__IDsim+" at step "+str(step),
                   message,
                   "#--------------------------------------------",
                   sep="\n")

    def __completeMessage (self,state,cl,method,message):
        time=str(datetime.datetime.now())

        if type(cl)==str: displayCl=cl
        elif cl==None:displayCl="no class"
        else:displayCl=cl.__class__.__name__

        if method==None or method=="":    displayMt="no method"
        else:   displayMt=method.f_code.co_name
        print(time,"{0:<4s}".format(state),message,"(class:",displayCl,", method:",displayMt+")")


    def displayProgress(self,nSnapshot,message):
        print ()

def __test(run):
    if run:
        print ("logger test")
        logger=Logger("test")

        for x in range (0,9000000):
            print (x,end=" ")


__test(False)