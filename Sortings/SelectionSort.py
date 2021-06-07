def Selectionsort(a):
    n=len(a)
    for i in range(n): #for the current value
        index=i
        for j in range(i+1,n):#finding the minimum element
            if a[index]>a[j]:  #use < for getting in descending order
                index=j #getting the minimum element index
        #swapping the minimum element and current element
        t=a[index]
        a[index]=a[i]
        a[i]=t
        #print(a[i]) for getting top n elements after making in descending order or ascending order
        print(a[index],a[i],"are swapped")
        print("after",i+1,"swapping:")
        print("                ",a)
        print()
seq=[20,18,24,42,15,12,34,19]
print("Input Sequence:")
print("               ",seq)
print("-----------------------------------------------------")
Selectionsort(seq)
print(seq)
