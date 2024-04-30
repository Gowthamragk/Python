'''def binary(lst,low,high,x):
    if low>high:
        return -1
    else:
        mid=(low+high) //2
        if lst[mid]==x:
            return mid
        elif lst[mid]>x:
            return binary(lst,low,mid-1,x)
        else:
            return binary(lst,mid+1,high,x)

lst = [1, 4, 6, 3, 9, 5, 8]
lst.sort()
x = 4
low=0
high=len(lst)-1
res= binary(lst,low,high,x)
print(res)'''


def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1


arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, 0, len(arr) - 1, x)
