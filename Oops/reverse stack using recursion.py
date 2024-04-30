n = 4
arr = [1, 2, 3, 4]

def reverse(arr):
    if len(arr) == 1:
        return arr
    return reverse(arr[1:]) + arr[:1]

arr=reverse(arr)
print(arr)
# for num in reversed_arr:
#     print(num, end=' ')