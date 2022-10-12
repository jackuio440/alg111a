import random
m=0
c=[]
c.append(000)
c.append(000)
a = [1,2,3,4,5]
while(True):
    b = random.sample(a, 3)
    dz=b.sort()

    for i in range(0,len(c)):
        if(c[i]==(str(b[0])+str(b[1])+str(b[2]))):
            m+=1
    if(m==0):
        c.append(str(b[0])+str(b[1])+str(b[2]))
        print(b)
    m=0

            

