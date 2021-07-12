#DOUBLE LINKED LIST
#need to check code!
class Node:
    def __init__(self,element,left,right):
        self.data=element
        self.Lnode=left
        self.Rnode=right
class DLLusingNode:
    def __init__(self):
        self.header=None
        self.tail=None
        self.size=0
    def isEmpty(self):
        return self.size==0
    def length(self):
        return self.size
    def display(self):
        if self.isEmpty():
            print("List is empty")
        else:
            p=self.header
            while(p):
                print(p.data,"==>",end=' ')
                p=p.Rnode
            print()
    def insertFirst(self,e):
        nn=Node(e,None,None)
        if self.isEmpty():
            self.header=nn
            self.tail=nn
            self.size=self.size+1
        else:
            nn.Rnode=self.header
            self.header.Lnode=nn
            self.header=nn
            self.size+=1
    def insertLast(self,e):
        nn=Node(e,None,None)
        if self.isEmpty():
            self.header=nn
            self.tail=nn
            self.size+=1
        else:
            nn.Lnode=self.tail
            self.tail.Rnode=nn
            self.tail=nn
            self.size+=1
    def insertAtPos(self,e,pos):
        nn=Node(e,None,None)
        if pos<=0:
            return self.insertFirst(e)
        elif pos>=self.length():
            return self.insertLast(e)
        else:
            p=self.header
            i=0
            while(i<pos):
                p=p.Rnode
                i=i+1
            nn.Rnode=p
            nn.Lnode=p.Lnode
            p.Lnode.Rnode=nn
            p.Lnode=nn
            self.size+=1
    def deleteFirst(self):
        if self.isEmpty():
            return "List is empty"
        elif self.header==self.tail:
            d=self.header.data
            self.header=None
            self.tail=None
            self.size-=1
            return d
        else:
            d=self.header.data
            self.header=self.header.Rnode
            self.header.Lnode.Rnode=None
            self.header.Lnode=None
            self.size-=1
            return d
    def deleteLast(self):
        if self.isEmpty():
            return "List is Empty"
        elif self.header==self.tail:
            d=self.header.data
            self.header=None
            self.tail=None
            self.size-=1
            return d
        else:
            d=self.tail.data
            self.tail=self.tail.Lnode
            self.tail.Rnode.Lnode=None
            self.tail.Rnode=None
            self.size-=1
            return d
    def deleteAtPos(self,pos):
        if self.isEmpty():
            print("List is Empty")
        elif pos<0 or pos>self.length():
            print("Invalid position")
        elif pos==0:
            return self.deleteFirst()
        elif pos==self.length():
            return self.deleteLast()
        else:
            i=0
            p=self.header
            while(i<pos):
                i=i+1
                p=p.Rnode
            t=p.data
            p.Lnode.Rnodet=p.Rnode
            p.Rnode.Lnode=p.Lnode
            p.Lnode=None
            p.Rnode=None
            self.size-=1
            return t
    def search(self,key):
        if self.isEmpty():
            print("List is empty")
        else:
            p=self.header
            while p:
                if p.data==key:
                    return "Success"
                p=p.Rnode
            return "Unsuccess"


dl=DLLusingNode()
#print(type(dl))
#print(dl.isEmpty())
#print(dl.length())
#dl.display()
dl.insertFirst(10)
dl.insertFirst(12)
dl.insertFirst(5)
#print(dl.isEmpty())
#print(dl.length())
#dl.display()
dl.insertLast(20)
#dl.display()
dl.insertAtPos(17,2)
#dl.display()
#print(dl.deleteFirst())
#dl.display()
#print(dl.deleteLast())
dl.display()
print(dl.deleteAtPos(2))
dl.display()
print(dl.search(100))
