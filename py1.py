n,k=map(int,input())
d=list()
c=0
for i in range(2,n/2):
    if n%i==0:
        d.append(i)
if k>d:
    print(-1)
else:
    print(d[k])


