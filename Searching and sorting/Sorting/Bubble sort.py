# def bubble(arr):
#     n = len(arr)
#     for i in range(0,n-1):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr[:]
# lst=[3,2,9,0]
# print(bubble(lst))



arr1=[2,1,2,5,7,1,9,3,6,8,8]
arr2=[2,1,8,3]
res=[]
for i in range(0,len(arr2)):
    while arr1:
        if i in arr1:
            res.append(i)
            arr1.remove(arr2[i])
print(res)
print(arr1)