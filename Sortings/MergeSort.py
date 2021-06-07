def Mergesort(a,L,U):
    if L<U:
        M=(L+U)//2#floor division wont give fractional value
        Mergesort(a,L,M)
        Mergesort(a,M+1,U)
        merge(a,L,M,U)
def merge(a,L,M,U):
    i=L
    j=M+1
    k=L
    b=[0]*(U+1)#[0,0,0,0,0,0,0,0]
    while i<=M and j<=U:
        if a[i]<a[j]:
            b[k]=a[i]
            i+=1
            k=k+1
        else:
            b[k]=a[j]
            j+=1
            k=k+1
    while j<=U:
        b[k]=a[j]
        k=k+1
        j=j+1
    while i<=M:
        b[k]=a[i]
        i=i+1
        k=k+1
    for x in range(L,U+1):
        a[x]=b[x]
    #print(a)
seq=[20,18,24,42,15,12,34,19]
print("Input Sequence:")
print(seq)
print("--------------------------------")
U=len(seq)-1
Mergesort(seq,0,U)
print(seq)
