import QueueLinkedList as QueueLL

class TreeNode:
    def __init__(self,data):
        self.rightChild = None
        self.leftChild = None
        self.data = data

def insertNode(root, item):
    if root is None:
        return TreeNode(item)
    elif item <= root.data:
        if root.leftChild is None:
            root.leftChild = TreeNode(item)
        else:
            insertNode(root.leftChild, item)
    else:
        if root.rightChild is None:
            root.rightChild = TreeNode(item)
        else:
            insertNode(root.rightChild, item)
    return root

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

def minValueNode(bstNode):
    current = bstNode
    while current.leftChild is not None:
        current = current.leftChild
    return current

def deleteNode(root,node):
    if not root:
        return root
    if node < root.data:
        root.leftChild = deleteNode(root.leftChild,node)
    elif node > root.data:
        root.rightChild = deleteNode(root.rightChild,node)
    else:
        if root.leftChild is None:
            temp = root.rightChild
            root = None
            return temp
        
        if root.rightChild is None:
            temp = root.leftChild
            root = None
            return temp
        
        temp = minValueNode(root.rightChild)
        root.data = temp.data
        root.rightChild = deleteNode(root.rightChild,temp.data)
    return root

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
    
def deleteBST(root):
    root.leftChild = None
    root.rightChild = None
    root.data = None


newBst = TreeNode(12)
insertNode(newBst,10)
insertNode(newBst,20)
insertNode(newBst,60)
insertNode(newBst,80)
insertNode(newBst,40)
insertNode(newBst,50)

insertNode(newBst,30)
insertNode(newBst,70)
inorder(newBst)