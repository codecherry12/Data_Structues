#stack using node structure
class Node:
    def __init__(self,d,l):
        self.data=d
        self.link=l

class Stack:
    def __init__(self):
        self.top=None
        self.size=0
    def isEmpty(self):
        return self.size==0
    def length(self):
        return self.size
    def push(self,element):
        nn=Node(element,None)
        if self.isEmpty():
            self.top=nn
            self.size=self.size+1
        else:
            nn.link=self.top
            self.top=nn
            self.size=self.size+1
    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        else:
            p=self.top
            t=self.top.data
            self.top=self.top.link
            p.link=None
            self.size=self.size-1
            return t
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.top.data
    def display(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            p=self.top
            while p:
                print(p.data,"-->",end='')
                p=p.link
            print()

st=Stack()
print(st.isEmpty())
print(st.length())
st.push(10)
st.push(2)
st.push(20)
st.push(30)
print("Stack elements are:")
st.display()
print(st.peek())
print("Deleted element is:",st.pop())
st.display()
