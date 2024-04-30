def insertion(arr):
    for i in range(1,len(arr)):
        x=lst[i]
        j=i-1
        while x<arr[j] and j>=0:
            arr[j+1=arr[j]]
            j-=1
        arr[j+1]=x
    return arr


def merge_sort(arr1,arr2):
    