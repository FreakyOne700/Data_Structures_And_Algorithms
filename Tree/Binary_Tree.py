import QueueLinkedList as QueueLL

class TreeNode:
    def __init__(self,data):
        self.rightChild = None
        self.leftChild = None
        self.data = data
    
def preorder(root):
    if not root:
        return
    print(root.data)
    preorder(root.leftChild)
    preorder(root.rightChild)  

def postorder(root):
    if not root:
        return
    postorder(root.leftChild)
    postorder(root.rightChild)
    print(root.data)

def inorder(root):
    if not root:
        return
    inorder(root.leftChild)
    print(root.data)
    inorder(root.rightChild)
    
def levelorder(rootNode):
    if not rootNode:
        return
    else:
        queue = QueueLL.Queue()
        queue.enqueue(rootNode)
        while not (queue.isEmpty()):
            root = queue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                queue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                queue.enqueue(root.value.rightChild)

def searchBT(rootNode,item):
    if not rootNode:
        return
    else:
        queue = QueueLL.Queue()
        queue.enqueue(rootNode)
        while not (queue.isEmpty()):
            root = queue.dequeue()
            if root.value.data == item:
                return "Found"
            if (root.value.leftChild is not None):
                queue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                queue.enqueue(root.value.rightChild)
        return "Not Found"

def insertBT(rootNode,item):
    if not rootNode:
        return
    else:
        queue = QueueLL.Queue()
        queue.enqueue(rootNode)
        while not (queue.isEmpty()):
            root = queue.dequeue()
            if (root.value.leftChild is not None):
                queue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = item
                return "Successfully Inserted"
            if (root.value.rightChild is not None):
                queue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = item
                return "Successfully Inserted"
        return "Failed to add"   
    
def getDeepestNode(rootNode):
    if not rootNode:
        return 
    else:
        queue = QueueLL.Queue()
        queue.enqueue(rootNode)
        while not queue.isEmpty():
            root = queue.dequeue()
            if root.value.leftChild is not None:
                queue.enqueue(root.value.leftChild)
            
            if root.value.rightChild is not None:
                queue.enqueue(root.value.rightChild)
        deepestnode = root.value
        return deepestnode

def deleteDeepestNode(rootNode,dNode):
    if not rootNode:
        return
    else:
        queue = QueueLL.Queue()
        queue.enqueue(rootNode)
        while not queue.isEmpty():
            root = queue.dequeue()
            if root.value is dNode:
                root.value = None
                return 
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild = None
                    return
                else:
                    queue.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild = None
                    return
                else:
                    queue.enqueue(root.value.leftChild)
    
def deleteNodeBT(rootNode,item):
    if not rootNode:
        return 
    else:
        queue = QueueLL.Queue()
        queue.enqueue(rootNode)
        while not queue.isEmpty():
            root = queue.dequeue()
            if root.value.data == item:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode,dNode)
                return "Node Deleted"
            if (root.value.leftChild is not None):
                queue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                queue.enqueue(root.value.rightChild)
        return "Failed"

def deleteBT(root):
    root.value = None
    root.leftChild = None
    root.rightChild = None

tree = TreeNode(1)
tree.leftChild = TreeNode(2)
tree.rightChild = TreeNode(3)
tree.leftChild.rightChild = TreeNode(5)
tree.leftChild.leftChild = TreeNode(4)
tree.rightChild.leftChild = TreeNode(6)
tree.rightChild.rightChild = TreeNode(7)
levelorder(tree)
deleteNodeBT(tree,2)
levelorder(tree)
