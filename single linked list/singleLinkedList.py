class Node:
    def __init__(self,x,next):
        self.data=x
        self.link=next
class SLinkedList:
    def __init__(self):
        self.header=None
        self.tail=None
        self.size=0
    def length(self):
        return self.size
    def isEmpty(self):
         return self.size==0
    def display(self):
        if self.isEmpty():
            print("List is empty")
        else:
            p=self.header
            while(p):
                print(p.data,"==>",end=" ")
                p=p.link
            print()
    def insertFirst(self,data):
        nn=Node(data,None)
        if self.isEmpty():
            self.header=nn
            self.tail=nn
            self.size=self.size+1
        else:
            nn.link=self.header
            self.header=nn
            self.size=self.size+1
    def insertLast(self,data):
        nn=Node(data,None)
        if self.isEmpty():
            self.header=nn
            self.tail=nn
            self.size=self.size+1
        else:
            self.tail.link=nn
            self.tail=nn
            self.size+=1
    def insertAtPos(self,pos,data):
        nn=Node(data,None)
        if pos<=0:
            self.insertFirst(data)
        elif pos>=self.size:
            self.insertLast(data)
        else:
            p=self.header
            index=0
            while index<pos-1:
                p=p.link
                index+=1
            nn.link=p.link
            p.link=nn
            self.size+=1
                
    def deleteFirst(self):
        if self.isEmpty():
            return "List is Empty"
        elif self.header==self.tail:
            t=self.header.data
            self.header=None
            self.tail=None
            self.size=self.size-1
            return t
        else:
            t=self.header.data
            p=self.header
            self.header=self.header.link
            p.link=None
            self.size=self.size-1
            return t
    def deleteLast(self):
        if self.isEmpty():
            return "List Is Empty"
        elif self.header==self.tail:
            d=self.header.data
            self.header=None
            self.tail=None
            self.size-=1
            return d
        else:
            cn=self.header
            pn=self.header
            while cn.link!=None:
                pn=cn
                cn=cn.link
            d=self.tail.data
            pn.link=None
            self.tail=pn
            self.size-=1
            return d
    def deleteAtPos(self,pos):
        if self.isEmpty():
            print("List is Empty")
        elif pos==0:
             return deleteFirst()
        elif pos==self.size:
             return deleteLast()
        elif pos<0 or pos>self.size:
            return "Invalid Position"
        else:
            index=0
            pn=self.header
            cn=self.header
            while index<pos:
                pn=cn
                cn=cn.link
                index+=1
            d=cn.data
            pn.link=cn.link
            cn.link=None
            self.size-=1
            return d
    def search(self,key):
        if self.isEmpty():
            return "List Is Empty"
        else:
            p=self.header
            while p:
                if p.data==key:
                    return "SUCCESS"
                p=p.link
            return "FAILED"

    
sll=SLinkedList()
'''
print(sll.isEmpty())
print(sll.length())
sll.display()
sll.insertFirst(10)
sll.display()
sll.insertFirst(14)
sll.display()
sll.insertFirst(20)
sll.display()
print(sll.deleteFirst())
display()
print(sll.deleteFirst())
display()
print(sll.deleteFirst())
display()'''
sll.display()
sll.insertLast(10)
sll.insertLast(20)
sll.insertLast(30)
sll.display()
sll.insertAtPos(0,5)
sll.display()
sll.insertAtPos(2,15)
sll.display()
print(sll.deleteLast())
sll.display()
print(sll.deleteAtPos(2))
sll.display()
print(sll.search(200))
print(sll.search(15))
print(sll.search(10))