ax=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if a[i]<a[j]:
            c=c+1
print(c)
