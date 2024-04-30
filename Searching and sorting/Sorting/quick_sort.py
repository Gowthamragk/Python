#Quick sort
#time-O(nlogn)

def quick(low, high, arr):
	if low < high:
		pivot = arr[(low+high) // 2+1]
		i = low
		j = high
		while i < j:
			while arr[i] < pivot:
				i += 1
			while arr[j] > pivot:
				j -= 1
			if i < j:
				arr[i], arr[j] = arr[j], arr[i]
			i += 1
			j -= 1
			if low < j:
				quick(low, j, arr)
			if i < high:
				quick(i, high, arr)
	return arr

# Python program for implementation of Quicksort Sort

# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot


# Function to find the partition position
# def partition(array, low, high):
#
# 	# choose the rightmost element as pivot
# 	pivot = array[high]
# 	print("pivot:",pivot)
#
# 	# pointer for greater element
# 	i = low
# 	print("i:",i)
#
# 	# traverse through all elements
# 	# compare each element with pivot
# 	for j in range(low, high):
# 		if array[j] <= pivot:
#
# 			# If element smaller than pivot is found
# 			# swap it with the greater element pointed by i
#
#
# 			# Swapping element at i with element at j
# 			(array[i], array[j]) = (array[j], array[i])
# 			i = i + 1
# 			print("inner iteration:",array)
#
# 	# Swap the pivot element with the greater element specified by i
# 	(array[i], array[high]) = (array[high], array[i])
# 	print(array)
#
# 	# Return the position from where partition is done
# 	return i
#
# # function to perform quicksort
#
#
# def quickSort(array, low, high):
# 	if low < high:
#
# 		# Find pivot element such that
# 		# element smaller than pivot are on the left
# 		# element greater than pivot are on the right
# 		pi = partition(array, low, high)
#
# 		# Recursive call on the left of pivot
# 		quickSort(array, low, pi - 1)
#
# 		# Recursive call on the right of pivot
# 		quickSort(array, pi + 1, high)
#
#
# data = [3, 7, 1, 8, 10, 9,4]
# print("Unsorted Array")
# print(data)
#
# size = len(data)
#
# quickSort(data, 0, size - 1)
#
# print('Sorted Array in Ascending Order:')
# print(data)



arr=[10,7,12,2,1,6,9,3,17]
high=len(arr)-1
print(quick(0,high,arr))