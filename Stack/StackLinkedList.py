class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

class Stack:
    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        return " ".join([str(x.value) for x in self.linkedlist])
    
    def isEmpty(self):
        if self.linkedlist.head == None:
            return True
        else:
            return False
        
    def push(self,item):
        node = Node(item)
        node.next = self.linkedlist.head
        self.linkedlist.head = node

    def pop(self):
        if self.isEmpty():
            return "UnderFlow"
        else:
            nodeValue = self.linkedlist.head.value
            self.linkedlist.head = self.linkedlist.head.next
            return nodeValue
    def peep(self):
        if self.isEmpty():
            return "Empty"
        else:
            nodeValue = self.linkedlist.head.value
            return nodeValue
        
    def delete(self):
        self.linkedlist.head = None
stk = Stack()
stk.push(12)
stk.push(11)
stk.push(13)
stk.push(14)
print(stk)
stk.pop()
print(stk)