class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
        
# class tree:
#     def __init__(self):
#         self.root=None
        
def insert(root,data):
    if root is None:
        root=Node(data)
    else:
        if data > root.data:
            root.right=insert(root.right,data)
        else:
            root.left=insert(root.left,data)
            
    return root
        
def inorderTraversal(root):  
    if root:
        inorderTraversal(root.left)  
        print(root.data, end = " ") 
        inorderTraversal(root.right) 
        
        
def dfs(root):
    if not root:
        return []
    result=[]
    stack=[root]
    while stack:
        node=stack.pop()
        result.append(node.data)
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
            
    return result

def bfs(root):
    if not root:
        return []
    result=[]
    queue=[root]
    while queue:
        next_level=[]
        for node in queue:
            result.append(node.data)
            
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
                
        queue=next_level
    return result
    
#delete the node in tree

def deletion(root,key):
    if root.data == key:
        if root.left is None and root.right is None:
            del root
        elif root.left is None:
            temp=root.right
            del root
            return temp
        elif  root.right is None:
            temp=root.left
            del root
            return temp
        else:
            succp=root
            succ=root.right
            while succ.left is not None:
                succp=succ
                succ=succ.left
            if succp != root:
                succp.left=succ.right
            else:
                succp.right=succ.right
            root.data=succ.data
            del succ
            return root
    elif root.data > key:
        root.left = deletion(root.left,key)
        return root
    elif root.data < key:
        root.right=deletion(root.right,key)
        return root

arr=[10,11,9,8,91,20,7]
root=Node(arr[0])
for i in range(1,len(arr)):
    insert(root,arr[i])
    
# inorderTraversal(root)
# print()
# deletion(root,20)   
print(bfs(root))                    