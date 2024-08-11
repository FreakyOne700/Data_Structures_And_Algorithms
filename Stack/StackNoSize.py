class Stack:
    def __init__(self):
        self.list = []
    
    def __str__(self):
        values = self.list
        values = values[::-1]
        return " ".join([str(x) for x in values])
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
    
    def push(self,item):
        self.list.append(item)
        return "Successfully Inserted"
    
    def pop(self):
        if self.isEmpty():
            return "Underflow"
        else:  
            value = self.list[len(self.list)-1]  
            return value
    def peek(self):
        if self.isEmpty():
            return "Stack Empty"
        else:
            return self.list[-1]
    
    def delete(self):
        self.list = None
    
stk = Stack()
stk.push(12)
stk.push(13)
stk.push(14)
stk.push(11)
print(stk)
stk.pop()
print(stk)
print(stk.peek())
