import random
import string

# TODO: Define a merge_sort function that takes data to sort and returns the sorted data
def merge_sort(arr):
    # TODO: If the alphanumeric array has one or no elements, it is already sorted. So, return the array immediately.
    if len(arr) <= 1:
        return arr

    # TODO: Next, divide the array into two equal parts.
    mid = len(arr) // 2

    # TODO: Sort the left and right parts of the array with the merge_sort function.
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # TODO: After sorting both halves of the array, combine them together using the merge function.
    return merge(left, right)

    # TODO: In the merge function, take two sorted arrays as inputs
def merge(left, right):
    # TODO: While both arrays have elements in them, compare the first element of each.
    # If the first element of the left array is smaller, add it to the result array and remove it from the left array.
    # Otherwise, do the same with the right array.
    i = j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # TODO: If the left or right array still has elements, add them to the result array.
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# TODO: Generate some random data to sort
data = [random.randint(1,50) for _ in range(30)]

# TODO: Print the original data
print("Original data: ", data)

# TODO: Use your merge_sort function to sort the data
sorted_data = merge_sort(data)

# TODO: Print the sorted data
print("Sorted data", sorted_data)