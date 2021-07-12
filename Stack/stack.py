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
            print(self.data)
    def pop(self):
        if st.isempty():
            print('stack is empty')
        else:
            return self.pop()
    def peek(self):
        if self.isempty():
            print("stack is empty")
            return
        return self.data[-1]
st=stack()
print(st.length())
print(st.isempty())
st.display()
st.push(10)
st.push(20)
st.push(30)
print(st.isempty())
st.display()
print(st.length())
print(st.data.pop())
st.display()
print(st.peek())
st.display()
