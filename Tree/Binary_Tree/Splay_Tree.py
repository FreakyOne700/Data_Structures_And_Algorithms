class Node:
    def __init__(self,data,parent):
        self.data = data
        self.parent = parent
        self.leftChild = None
        self.rightChild = None

class SplayTree:
    def __init__(self) -> None:
        self.root = None
    
    def insert(self,data):
        if not self.root:
            self.root = Node(data,None)
        else:
            self.insert_node(data,self.root)
    
    def insert_node(self,data,node):

        if data < node.data:
            if node.leftChild:
                self.insert_node(data,node.leftChild)
            else:
                node.leftChild = Node(data,node)
        else:
            if node.rightChild:
                self.insert_node(data,node.rightChild)
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
    
    def splay(self,node):
        while node.parent is not None:
            if node.parent.parent is None:
                # Zig Situation
                if node == node.parent.leftChild:
                    self.rightRotation(node.parent)
                else:
                    self.leftRotation(node.parent)
            # doubly heavy cases Zig-Zig Condtion
            elif node == node.parent.leftChild and node.parent == node.parent.parent.leftChild:
                self.rightRotation(node.parent.parent)
                self.rightRotation(node.parent)
            elif node == node.parent.rightChild and node.parent == node.parent.parent.rightChild:
                self.leftRotation(node.parent.parent)
                self.leftRotation(node.parent)
            # Zig-Zag Situation
            elif node == node.parent.leftChild and node.parent == node.parent.parent.rightChild:
                self.rightRotation(node.parent)
                self.leftRotation(node.parent)
            else:
                self.leftRotation(node.parent)
                self.rightRotation(node.parent)

sTree = SplayTree()
sTree.insert(10,)
sTree.insert(7)
sTree.insert(8)
sTree.insert(11)
sTree.find(11)
print(sTree.root.data)