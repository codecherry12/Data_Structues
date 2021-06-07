#by reducing the number of comparisions
def LinearSearch(seq,key):
    for i in range(len(seq)):
        if seq[i]==key:
            return i
        if seq[i]>key:
            return -1
    return -1

seq=[12,16,36,44,55,68,76]
key=15
res=LinearSearch(seq,key)
if res==-1:
    print("Search is UN-Success")
else:
    print("Search is success",res)
