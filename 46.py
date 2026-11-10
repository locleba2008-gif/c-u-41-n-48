n,x=map(int, input('').split())
a=list(map(int, input('').split()))
kiem_tra=False
for i in range(n):
    if a[i]==x:
        kiem_tra=True
        break
if kiem_tra:
    print('Yes')
    print(i)
else:
    print('No')            