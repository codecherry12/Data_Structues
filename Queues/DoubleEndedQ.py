#double ended queue
class deq:
    def __init__(self):
        self.data=[]
    def isempty(self):
        return len(self.data)==0
    def __len__(self):
        return len(self.data)
    def enquerear(self,ele):
        self.data.append(ele)
    def dequerear(self):
        if self.isempty():
            print('Q is empty')
        else:
            return self.data.pop()
    def enquefront(self,ele):
        self.data.insert(0,ele)
    def dequefront(self):
        if self.isempty():
            print("Q is empty")
        else:
            return self.data.pop(0)
    def display(self):
        if self.isempty():
            print("Q is empty")
        else:
            for var in self.data:
                print(var," == " ,end=' ')
            print()
DEQ=deq()
print(DEQ.isempty())
DEQ.display()
DEQ.dequefront()
DEQ.enquefront(10)
DEQ.enquefront(11)
DEQ.display()
DEQ.enquerear(100)
DEQ.enquerear(101)
DEQ.display()
print(DEQ.dequerear())
DEQ.display()
print(DEQ.dequefront())
DEQ.display()
