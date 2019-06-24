ax=int(input())
c=1
a=list(map(int,input().split()))
for i in a:
    c=c & i
print(c)
