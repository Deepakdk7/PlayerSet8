n,r=list(map(int,input().split()))
a=b=1
for i in range(1,n+1):
    a=a*i
for i in range(1,(n-r)+1):
    b=b*i
print(a//b)
