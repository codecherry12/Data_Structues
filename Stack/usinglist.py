#stack using list
class stack:
    def __init__(self):
        self.data=[]
    def length(self):
        return len(self.data)
    def push(self,ele):
        self.data.append(ele)
    def isempty(self):
        return len(self.data)==0
    def display(self):
        if self.isempty():
            print("stack is empty")
        else:
            for val in self.data[::-1]:
                print("^")
                print(val)
    def pop(self):
        if st.isempty():
            print('stack is empty')
            return
        else:
            return self.data.pop()
    def peek(self):
        if self.isempty():
            print("stack is empty")
            return
        return self.data[-1]
    def __len__(self):
        return len(self.data)
st=stack()
il=[int(i) for i in input().split()]
for val in il:
    st.push(val)
print("length of stack is :",st.length())
for val in range(st.length()):
    print(st.pop())
print(st.pop())
print(len(st))
st.push(100)
st.push(70)
st.display()
print(st.peek())
