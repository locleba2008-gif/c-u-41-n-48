k=int(input(''))
n=list(map(int, input('').split()))
tong=0
co_so_chan=False
for i in range(k):
    if n[i]%2==0:
        tong+=n[i]
        co_so_chan=True
if co_so_chan:
    print(tong)
else:
    print('-')            

        
