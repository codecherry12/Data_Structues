#1)From the input sequence let me know first repeating number
#printing the array neglecting the duplicate elements
def findDuplicate2(a):#time complexity is O(n)
    mx=max(a)
    nfa=[0]*(mx+1)#Number frequency array
    for i in a:
        if nfa[i]==0:
            nfa[i]=1
            print(i,end="")

seq=[8,4,3,2,4,8,7,4,9]
findDuplicate2(seq)
#print(d)
"""
def findDuplicate2(a):#time complexity is O(n)
    mx=max(a)
    nfa=[0]*(mx+1)#Number frequency array
    for i in a:
        if nfa[i]==0:
            nfa[i]=1
        else:
            return i
seq=[8,4,3,2,4,8,7,4,9]
d=findDuplicate2(seq)
print(d)
"""
"""def findDuplicate1(a):#time complexity is O(n**2)
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]==a[j]:
                return a[i]
seq=[8,4,3,2,4,8,7,4,9]
d=findDuplicate1(seq)
print(d)
"""

"""
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
