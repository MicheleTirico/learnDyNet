l=[1,0.5,0]

print (l[0:3])
l3=[]
for a in range(0,3):
    l2=[]
    for i in range(0+a,3+a):
        l2.append(l[i%3])
    print (l2)
    l3.append(l2)
print (l3)


l=["1","3","5"]
print (l)
#for i in range(len(l)): l[i]=int (l[i])

l2 =[x+33 for x in range (len (l))]
print (l2)


l=[int(l[i]) for i in range(len(l))]


print (l)

