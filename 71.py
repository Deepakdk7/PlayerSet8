ax=int(input())
a=list(map(int,input().split()))
for i in range(0,len(a)-1):
    print(max(a[i],a[i+1]),end=' ')
