class Node:
    def __init__(self,data):
        self.data = data
        self.parent = None
        self.leftChild = None
        self.rightChild = None

class SplayTree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self,data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insert(data,self.root)
    
    def insert(self,data,node):

        if data < node.data:
            if node.leftChild:
                self.insert(data,node.leftChild)
            else:
                node.leftChild = Node(data,node)
        else:
            if node.rightChild:
                self.insert(data,node.rightChild)
            else:
                node.rightChild = Node(data,node)
            
    def find(self,data):
        node = self.root
        while node is not None:
            if data < node.data:
                node = node.leftChild
            elif data > node.data:
                node = node.rightChild
            else:
                self.splay(node)
                return node.data
            
    def rightRotation(self,disbalancedNode):
        temp = disbalancedNode.leftChild 
        t = temp.rightChild
        temp.rightChild = disbalancedNode
        disbalancedNode.leftChild = t 

        if t is not None:
            t.parent = disbalancedNode

        temp_parent = disbalancedNode.parent
        disbalancedNode.parent = temp

        temp.parent = temp_parent

        if temp.parent is not None and temp.parent.leftChild == disbalancedNode:
            temp.parent.leftChild = temp
        if temp.parent is not None and temp.parent.rightChild == disbalancedNode:
            temp.parent.rightChild = temp
        if disbalancedNode == self.root:
            self.root = temp

    def leftRotation(self,disbalancedNode):
        temp = disbalancedNode.rightChild 
        t = temp.leftChild
        temp.leftChild = disbalancedNode
        disbalancedNode.rightChild = t 

        if t is not None:
            t.parent = disbalancedNode

        temp_parent = disbalancedNode.parent
        disbalancedNode.parent = temp

        temp.parent = temp_parent

        if temp.parent is not None and temp.parent.leftChild == disbalancedNode:
            temp.parent.leftChild = temp
        if temp.parent is not None and temp.parent.rightChild == disbalancedNode:
            temp.parent.rightChild = temp
        if disbalancedNode == self.root:
            self.root = temp
