import QueueLinkedList as QueueLL

class AVLNode:
    def __init__(self,data) -> None:
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

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