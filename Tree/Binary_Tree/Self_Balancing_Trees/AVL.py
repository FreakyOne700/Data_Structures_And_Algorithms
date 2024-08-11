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

def getHeight(root):
    if not root:
        return 0
    else:
        return root.height

def rightRotation(disbalancedNode):
    newRoot = disbalancedNode.leftChild
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
    newRoot.rightChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild),getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))
    return newRoot

def leftRotation(disbalancedNode):
    newRoot = disbalancedNode.rightChild
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftChild
    newRoot.leftChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild),getHeight(disbalancedNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild),getHeight(newRoot.rightChild))
    return newRoot

def getBalanced(root):
    if not root:
        return 0
    return getHeight(root.leftChild) - getHeight(root.rightChild)

def insertNode(root,value):
    if not root:
        return AVLNode(value)
    elif value < root.data:
        root.leftChild = insertNode(root.leftChild,value)
    else:
        root.rightChild = insertNode(root.rightChild,value)

    root.height = 1+max(getHeight(root.leftChild),getHeight(root.rightChild))
    balance = getBalanced(root)

    # LL Conditon
    if balance > 1 and value < root.leftChild.data:
        return rightRotation(root)
    
    # LR Condition 
    if balance > 1 and value > root.leftChild.data:
        root.leftChild = leftRotation(root.leftChild)
        return rightRotation(root)
    
    #RL Condition
    if balance < -1 and value < root.rightChild.data:
        root.rightChild = rightRotation(root.rightChild)
        return leftRotation(root)
    
    # RR Conditon
    if balance < -1 and value > root.rightChild.data:
        return leftRotation(root)
    return root

def getMinValue(root):
    if not root or root.leftChild is None:
        return root
    return getMinValue(root.leftChild)

def deleteNode(root,value):
    if not root:
        return root
    elif value < root.data:
        root.leftChild = deleteNode(root.leftChild,value)
    elif value > root.data:
        root.rightChild = deleteNode(root.rightChild,value)
    else:
        if root.leftChild is None:
            temp = root.rightChild
            root = None
            return temp
        elif root.rightChild is None:
            temp = root.leftChild
            root = None
            return temp
        temp = getMinValue(root.rightChild)
        root.data = temp.data
        root.rightChild = deleteNode(root.rightChild,temp.data)
    
    balance = getBalanced(root)
    # LL Condtion
    if balance > 1 and getBalanced(root.leftChild) >= 0:
        return rightRotation(root)
    
    # RR Condition
    if balance < -1 and getBalanced(root.rightChild) <= 0:
        return leftRotation(root)
    
    # LR Condition
    if balance > 1 and getBalanced(root.leftChild) < 0:
        root.leftChild = leftRotation(root.leftChild)
        return rightRotation(root)
    
    # RL Condition
    if balance < -1 and getBalanced(root.rightChild) > 0:
        root.rightChild = rightRotation(root.rightChild)
        return leftRotation(root)
    
    return root

def deleteAVL(root):
    root.data = None
    root.rightChild = None
    root.leftChild = None
    return "Deleted Successfully"

newAVL = AVLNode(5)
newAVL = insertNode(newAVL,10)
newAVL = insertNode(newAVL,15)
newAVL = insertNode(newAVL,20)
newAVL = deleteNode(newAVL,5)
levelorder(newAVL)