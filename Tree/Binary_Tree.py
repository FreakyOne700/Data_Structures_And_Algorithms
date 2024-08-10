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
    
def levelorder(root):
    if not root:
        return
    else:
        queue = QueueLL.Queue()
        queue.enqueue(root)
        while not (queue.isEmpty()):
            root = queue.dequeue()
            print(root.value.data)
            if (root.value.leftChild is not None):
                queue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                queue.enqueue(root.value.rightChild)

def searchBT(root,item):
    if not root:
        return
    else:
        queue = QueueLL.Queue()
        queue.enqueue(root)
        while not (queue.isEmpty()):
            root = queue.dequeue()
            if root.value.data == item:
                return "Found"
            if (root.value.leftChild is not None):
                queue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                queue.enqueue(root.value.rightChild)
        return "Not Found"

def insertBT(root,item):
    if not root:
        return
    else:
        queue = QueueLL.Queue()
        queue.enqueue(root)
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

tree = TreeNode(1)
tree.leftChild = TreeNode(2)
tree.rightChild = TreeNode(3)
tree.leftChild.rightChild = TreeNode(5)
tree.leftChild.leftChild = TreeNode(4)
tree.rightChild.leftChild = TreeNode(6)
tree.rightChild.rightChild = TreeNode(7)
print(insertBT(tree,TreeNode(10)))
levelorder(tree)
