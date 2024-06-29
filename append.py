n=int(input('enter an element'))
t=[]
for i in range(n):
    t.append(int(input('enter an element')))
while True:
    print("\n1-append\n 2-extend\n 3-insert\n 4-index\n 5-sort\n")
    ch=int(input('enter your choice'))
    if ch==1:
        a=int(input('enter element to append'))
        t.append(a)
        print(t)
    elif ch==2:
        t2=[]
        n=int(input('enter no.of element'))
        for i in range(n):
            t2.append(int(input('enter an element')))
        t.extend(t2)
        print(t)
    elif ch==3:
        x=int(input('enter index'))
        y=int(input('enter element'))
        t.insert(x,y)
        print(t)
    elif ch==4:
        z=int(input('enter an element'))
        print(t.index(z))
    elif ch==5:
        t.sort()
        print(t)
    else:
        break 
        
        
        
        
