import Tree.Binary_Tree.QueueLinkedList as QueueLL

class TreeNode:
    def __init__(self,data):
        self.rightChild = None
        self.leftChild = None
        self.data = data

def insertNode(root,item):
    if root.data == None:
        root.data = item
    elif item <= root.data:
        if root.leftChild == None:
            root.leftChild = TreeNode(item)
        else:
            insertNode(root.leftChild,item)
    else:
        if root.rightChild == None:
            root.rightChild = TreeNode(item)
        else:
            insertNode(root.rightChild,item)
    return "Inserted Successfully"

def searchNode(root,item):
    if root.data == item:
        print("Found")
    elif root.data < item:
        if root.leftChild.data == item:
            print("Found")
        else:
            searchNode(root.leftChild,item)
    else:
        if root.rightChild.data == item:
            print("Found")
        else:
            searchNode(root.rightChild,item)
    
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
