def BinarySearch(seq,key):
    L=0
    U=len(seq)-1
    while L<=U:
        M=(L+U)//2
        if seq[M]==key:
            return M
        elif key<seq[M]:
            U=M-1
        elif key>seq[M]:
            L=M+1
    return -1

seq=[12,16,36,44,55,68,76]
key=76
res=BinarySearch(seq,key)
if res==-1:
    print("Search is UN-Success")
else:
    print("Search is success",res)
