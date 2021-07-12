# You are using Python
class Node:
    def __init__(self,x,left,right):
        self.data=x
        self.Lnode=left
        self.Rnode=right
class circularLinkedList():
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def insertLast(self,data):
        nn=Node(data,None,None)
        if self.size==0:
            self.head=nn
            self.tail=nn
            self.size+=1
        else:
            nn.Lnode=self.tail
            self.tail.Rnode=nn
            self.tail=nn
            self.tail.Rnode=self.head
            self.head.Lnode=self.tail
            self.size+=1
    def display(self,pos):
        p=self.head
        count=0
        i=0
        while i!=pos:
            p=p.Rnode
            i+=1
        while count!=self.size:
            print(p.data,end=" ")
            p=p.Rnode
            count+=1
        print()
n=int(input())
data=list(map(int,input().split()))
pos=int(input())-1
cll=circularLinkedList()
for i in data:
    cll.insertLast(i)
cll.display(pos)
    
