#single ended queue using double linked list
class Node:
    def __init__(self,e,left,right):
        self.data=e
        self.Lnode=left
        self.Rnode=right

class QueueNode:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0
    def length(self):
        return self.size
    def isEmpty(self):
        return self.size==0
    def enque(self,e):
        nn=Node(e,None,None)
        if self.isEmpty():
            self.front=nn
            self.rear=nn
            self.size+=1
        else:
            nn.Lnode=self.rear
            self.rear.Rnode=nn
            self.rear=nn
            self.size+=1
    def display(self):
        if self.isEmpty():
            print("Q is empty")
        else:
            p=self.front
            while(p):
                print(p.data,"<==",end='')
                p=p.Rnode
            print()
    def deque(self):
        if self.isEmpty():
            return "Q is empty"
        elif self.rear==self.front:
            t=self.front.data
            self.front=None
            self.rear=None
            self.size-=1
            return t
        else:
            p=self.front
            t=p.data
            self.front=self.front.Rnode
            self.front.Lnode=None
            self.front.Lnode=None
            p.Rnode=None
            self.size-=1
            return t
    def rearNode(self):
        if self.isEmpty():
            return "Q is empty()"
        else:
            return self.rear.data
    def frontNode(self):
        pass
    def search(self):
        pass

Q=QueueNode()
print(Q.length())
print(Q.isEmpty())
Q.enque(10)
Q.enque(14)
Q.enque(7)
Q.enque(20)
print(Q.length())
print(Q.isEmpty())
Q.display()
print(Q.deque())
Q.display()
print(Q.rearNode())
