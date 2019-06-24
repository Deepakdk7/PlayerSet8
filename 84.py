ax=int(input())
c=0
d=[]
a=list(map(int,input().split()))
for i in a:
    c=c | i
    d.append(c)
print(max(d))
