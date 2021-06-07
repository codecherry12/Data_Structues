#using recursion
def BinarySearch(seq,key,L,U):
    if L>U:
        return -1
    M=(L+U)//2
    if seq[M]==key:
        return M
    elif key<seq[M]:
        return BinarySearch(seq,key,L,M-1)
    elif key>seq[M]:
        return BinarySearch(seq,key,M+1,U)


seq=[12,16,36,44,55,68,76]
key=76
low=0
upper=6
res=BinarySearch(seq,key,low,upper)
if res==-1:
    print("Search is Un-Success")
else:
    print("Search is success",res)
