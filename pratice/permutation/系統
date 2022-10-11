a = [1,2,3,4,5]
c=[]
b=[]
c.append(000)
c.append(000)

def search():
    b.extend([a[0],a[1],a[2]])
    dz=b.sort()
    mz=0
    for i in range(0,len(c)):
        if(c[i]==(str(b[0])+str(b[1])+str(b[2]))):
            mz+=1
    if(mz==0):
        c.append(str(b[0])+str(b[1])+str(b[2]))
        print(b)
        
    b.clear()
    mz=0
for i in range(1,10):
    if(i%2==1):
        for i in range(4,1,-1):
            n=i
            m=i-1
            a[m],a[n]=a[n],a[m]            
            search()
        a[-1],a[-2]=a[-2],a[-1]
        search()
    elif(i%2==0):
        for i in range(0,3,1):
            m=i
            n=i+1
            a[m],a[n]=a[n],a[m]
            search()
        a[0],a[1]=a[1],a[0]
        search()
