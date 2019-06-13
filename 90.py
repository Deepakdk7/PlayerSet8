ax=list(map(int,input().split()))
a=b=1
for i in range(1,ax[1]+1):
    a=a*ax[0]
    print('a',a)
    b=b*i
    print('b',b)
    ax[0]=ax[0]-1
print(a//b)
