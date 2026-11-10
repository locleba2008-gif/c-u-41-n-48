n=int(input(''))
a=list(map(int, input('').split()))
dem=0
tong=0
for i in range(n):
    if a[i]%5==0:
        dem+=1
        tong+=a[i]
        print(a[i],end=' ')
if dem==0:
    print('-')
print()   
print(tong)      