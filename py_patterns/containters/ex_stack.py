class Stack:
    def __init__(self):
        self._data = []

    def push(self, data):
        self._data.append(data)

    def pop(self):
        return self._data.pop()



stack = Stack()
stack.push(10)

test = stack.pop()
print(test)

