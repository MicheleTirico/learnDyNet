


def getCombinationsList(list):
    combinations=[]
    # create list combinations alpha
    for a in range(0,len(list)):
        l1=[]
        for i in range (a,a+3):l1.append((list[i%len(list)]))
        combinations.append(l1)
    return  combinations


def castFloatElementOfList (l):
    return [float(l[i]) for i in range(len(l))]
