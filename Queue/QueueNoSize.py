class Queue:
    def __init__(self) -> None:
        self.item = []

    def __str__(self):
        values = [str(x) for x in self.item]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.item == []:
            return True
        else:
            return False
    
    def enqueue(self,value):
        self.item.append(value)
        return "The Element is inserted at the end of Queue"
    
    def dequeue(self):
        if self.isEmpty == True:
            return "There is not any element in Queue"
        else:
            return self.item.pop(0)
    
    def delete(self):
        self.item = None

customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.enqueue(4)
print(customQueue)
print(customQueue.dequeue())
print(customQueue)
customQueue.delete()
print(customQueue)