ax=int(input())
a=list(map(int,input().split()))
m=max(a)-min(a)
for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        if abs(a[i]-a[j])<m and a[i]!=a[j]:
            m=abs(a[i]-a[j])          
print(m)
