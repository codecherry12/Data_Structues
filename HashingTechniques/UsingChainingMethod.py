class Chaining:
    def __init__(self,hts):
        self.size=hts
        self.ht=[0]*self.size
        for i in range(self.size):
            self.ht[i]=LL()
    def hashFun(self,key):
        return key%self.size
    def insert(self,key):
        i=self.hashFun(key)
        self.ht[i].insertSort(key)
    def display(self):
        for i in range(self.size):
            print('[',i,']',end='')
            self.ht[i].display()
        print()
    def search(self,key):
        i=self.hashFun(key)
        result=self.ht[i].search(key)
        if result==1:
            print("element found")
        else:
            print("Not found")

class Node:
    def __init__(self,element,next):
        self.data=element
        self.next=next
class LL:
    def __init__(self):
        self.head=None
        self.size=0
    def insertSort(self,data):
        nn=Node(data,None)
        if self.size==0:
            self.head=nn
            self.size+=1
        elif data < self.head.data:
            nn.next=self.head
            self.head=nn
            self.size+=1
        else:
            p=self.head
            q=self.head
            while q and q.data<data:
                p=q
                q=q.next
            nn.next=q
            p.next=nn
            self.size+=1
    def display(self):
        if self.size==0:
            #print("List is empty")
            print()
        else:
            p=self.head
            while p:
                print("-->",p.data,end="")
                p=p.next
            print()
    def search(self,element):
        if self.size==0:
            return -1
        else:
            p=self.head
            while p:
                if p.data==element:
                    return 1
                p=p.next
            return -1

ob=Chaining(10)
'''
ob.insert(10)
ob.display()
ob.insert(23)
ob.display()
ob.insert(40)
ob.display()
ob.insert(13)
ob.display()
'''
Lkeys=[54,78,64,92,34,86,28]
for i in Lkeys:
    ob.insert(i)
ob.display()
ob.search(64)

"""
Applications:
file is there with certain sentences .i wants to know frequency count of word "xyz"
To check the loop or cycle in linkedlist
s1 and s2 are two lists/sentences/files/sets then check they are equal.
      ex:- s1=bread and butter
           s2=bread and butter
To find the unique words or numbers from the given input
plugarism checker
"""
