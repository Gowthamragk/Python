'''def selec(lst, size):
    for i in range(size):
        min_index = i

        for j in range(i+ 1, size):
            if lst[j] < lst[min_index]:
                min_index = j
        (lst[i], lst[min_index]) = (lst[min_index], lst[i])


arr = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
size = len(arr)
selec(arr, size)
print(arr)'''

# Python 3 program for recursive binary search.
# Modifications needed for the older Python 2 are found in comments.

# Returns index of x in arr if present, else -1


if result != -1:
	print("Element is present at index", str(result))
else:
	print("Element is not present in array")
