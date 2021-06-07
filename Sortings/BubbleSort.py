def Bubblesort(a):
    n=len(a)
    for i in range(n):#iterating through the list
        print("for index i=",i)
        print('iteration_number ==>',i+1)
        for j in range(n-1-i):#iterating for bringing the biggest element at last el
            if a[j]>a[j+1]:#(n-1-i)is written for getting the upper bonded index for unsorted order
                t=a[j]
                a[j]=a[j+1]
                a[j+1]=t
            print(a)
        print()

seq=[20,14,28,42,18,24,12]
Bubblesort(seq)
print(seq)
