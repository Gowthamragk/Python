class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
                    
def insert(arr, root, i, n):
    if i < n:
        temp = Node(arr[i])
        root = temp
        root.left = insert(arr, root.left, 2 * i + 1, n)
        root.right = insert(arr, root.right, 2 * i + 2, n)
    return root
def buildLevelOrderTree(arr):
    n = len(arr)
    root = None
    root = insert(arr, root, 0, n)
    return root
                    
def inorderTraversal(root):  
    if root:
        inorderTraversal(root.left)  
        print(root.data, end = " ")  
        inorderTraversal(root.right)
        
def levelSum(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        level_sum = 0
        next_level = []

        for node in queue:
            level_sum += node.data

            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        result.append(level_sum)
        queue = next_level

    return result 


def bfsdisplay(root):
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        next_level = []

        for node in queue:
            result.append(node.data)

            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        queue = next_level

    return result 

def dfs(root):
    if not root:
        return
    result=[]
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.data)  # Or perform any other operation you desire on the node
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
            
    return result




def dfsrec(root):
    if not root:
        return
    print(root.data,end=" ")  # Or perform any other operation you desire on the node
    dfs(root.left)
    dfs(root.right)
                               
                

arr=[4,2,-5,-1,3,-2,6]
root=Node(arr[1])
res=insert(arr,root,0,len(arr))
print(dfs(res))


