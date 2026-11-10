n=int(input(''))
a=list(map(int,input('').split()))
for i in range(n-1):
    for k in range(n-2):
        if a[i]<a[i+1]:
            gtln=a[i+1]
print(gtln)
print(a.index(gtln))