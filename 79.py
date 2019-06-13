ax=int(input())
m=0
a=list(map(int,input().split()))
for i in range(0,len(a)-1):
    for j in range(i+1,len(a)):
        if abs(a[i]-a[j])>m:
            m=abs(a[i]-a[j])          
print(m)
