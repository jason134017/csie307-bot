def backtrack(n,N):
    if n==N:
        print (solution)
        return
    for i in range(0,N):
        if listcheck[i]==bool(0):
             listcheck[i]=bool(1)
             solution[n] =sortlist[i]
             backtrack(n+1,N)
             listcheck[i]=bool(0)
         
mylist = list()
listcheck=list()
solution=[0,0,0,0]
for i in range(0,4):
     x=int(input("input four number"))
     mylist.append(x)
     listcheck.append(bool(0))
     
sortlist=sorted(mylist)
backtrack(0,4)
