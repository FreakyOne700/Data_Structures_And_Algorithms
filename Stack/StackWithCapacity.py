class Stack:
    def __init__(self,maxSize):
        self.list = []
        self.maxSize = maxSize
    
    def __str__(self):
        values = self.list
        values = values[::-1]
        return " ".join([str(x) for x in values])
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
        
    def push(self,item):
        if self.isFull():
            return "Stack is Full"
        else:
            self.list.append(item)
    def pop(self):
        if self.isEmpty():
            return "Stack is Full"
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "Underflow"
        else:
            return self.list[len(self.list)-1]
        
    

        
stk = Stack(5)
print(stk.isEmpty())
stk.push(12)
stk.push(18)
stk.push(16)
stk.push(13)
stk.push(11)
print(stk)
print(stk.isEmpty())
print(stk.pop())
print(stk.isFull())
print(stk)
