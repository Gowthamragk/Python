def max_heap(arr,n,parent):
    largest=parent
    left = 2*parent + 1 
    right = 2*parent + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
        
    if right < n and arr[right] > arr[largest]:
        largest = right
        
    if largest != parent:
        arr[largest],arr[parent] = arr[parent],arr[largest]
        
        max_heap(arr,n,largest)
        
        
def heap(arr):
    n = len(arr)
    
    for i in range(n//2-1,-1,-1):
        max_heap(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        max_heap(arr,i,0)
        
arr=[12,3,55,1,23,10]

heap(arr)
print(arr)