n=int(input(''))
a=list(map(int, input('').split()))
count_duong=0
count_am=0
duong=False
am=False
for i in range(n):
    if a[i]>0:
        count_duong+=1
        duong=True
for j in range(n):
    if a[j]<0:
        count_am+=1
        am=True    
print(count_duong,count_am)
if count_duong>0:
    for i in range(n):
        if a[i]>0:
            print(a[i],end=' ')
else :
    print('-')
print()    

if count_am>0:
    for j in range(n):
        if a[j]<0:
            print(a[j],end=' ')
else:
    print('-')  
print()              


       