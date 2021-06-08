def CountSort(a):
    maximum=max(a)
    count_array=[0]*(maximum+1)
    for i in a:
        count_array[i]=count_array[i]+1
        print(i,"==>",count_array)
    k=0
    for i in range(len(count_array)):
        if count_array[i]!=0:
            for j in range(count_array[i]):
                a[k]=i
                k=k+1

#seq=[20,40,18,23,73,15,12,33]
seq=[10,2,14,11,14,8,7,8]
print(seq)
CountSort(seq)
print(seq)
"""
1)From the input sequence let me know first repeating number
2)s1 and s2 are two sets;i,j where i+j=k
3)eleminate the duplicate numbers from the input and
4)s1 and s2 are two sets are given then check these two arrays are equal or not
5)3 people were contested in voting system 3==>1,2,3
   1,2,3,2,3,2,2,2,2,2,2,3,3,3,1 find the winner"""
