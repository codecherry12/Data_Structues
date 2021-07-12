class queuelist:
    def __init__(self):
        self.data=[]
    def isempty(self):
        return len(self.data)==0
    def __len__(self):
        return len(self.data)
    def enque(self,ele):
        self.data.append(ele)
    def display(self):
        if self.isempty():
            print("queue is empty")
        else:
            for var in self.data:
                print(var,end=" ")
                print("<=",end=" ")
            print()
    def deque(self):
        if self.isempty():
            print("Q is empty")
        else:
            return self.data.pop(0)
    def front(self):
        if self.isempty():
            print("Q is empty")
        else:
            return self.data[0]
Q=queuelist()
print(Q.isempty())
Q.display()
Q.enque(100)
Q.enque(200)
Q.enque(300)
print(Q.isempty())
Q.display()
print(len(Q))
print(Q.deque())
Q.display()
print(Q.front())
