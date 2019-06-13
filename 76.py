ax=int(input())
bx=list(map(int,input().split()))
c=[]
d=[]
for i in bx:
    if i%2==0:
        c.append(i)
    else:
        d.append(i)
if len(c)>len(d):
    print(*d)
else:
    print(*c)
