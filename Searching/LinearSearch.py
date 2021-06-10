#O(n)-time complexity
def LinearSearch(seq,key):
    for i in range(len(seq)):
        if seq[i]==key:
            return i
    return -1

seq=[12,56,36,14,25,78,46]
key=78
res=LinearSearch(seq,key)
if res==-1:
    print("Search is UN-Success")
else:
    print("Search is success",res)
