class StackUsingArray:
    def __init__(self):
        self.data = []

    def insert(self, data):
        self.data.append(data)

    def pop(self):
        temp  = self.data[len(self.data) - 1]
        del(self.data[len(self.data ) -1])
        return temp

    def peek(self):
        return self.data[len(self.data) -1]

st = StackUsingArray()
st.insert(3)
st.insert(4)
st.insert(5)
st.insert(6)
st.insert(7)
print(st.peek())
print(st.pop())
print(st.pop())
print(st.pop())
print(st.pop())
print(st.pop())
