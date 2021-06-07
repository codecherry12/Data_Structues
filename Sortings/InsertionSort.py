def Insertionsort(a):
    n=len(a)
    for i in range(1,n):
        CurrentValue=a[i]
        pos=i
        while pos>0 and CurrentValue<a[pos-1]:#for finding the appropriate position
            a[pos]=a[pos-1]
            pos=pos-1
        a[pos]=CurrentValue#storing the value in the found appropriate position
        print("After",i,"sorting")
        print(a)


seq=[20,18,24,42,15,12,34,19]
print("Input Sequence:")
print(seq)
print("--------------------------------")
Insertionsort(seq)
print(seq)
