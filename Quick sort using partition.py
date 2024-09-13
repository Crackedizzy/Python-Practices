import random

# TODO: Define the 'quick_sort_desc' and 'partition_desc' functions to implement Quick Sort in descending order

def partition_desc(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] > pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1
    
def quick_sort_desc(arr, low, high):
    if low < high:
        p = partition_desc(arr, low, high)
        quick_sort_desc(arr, low, p-1)
        quick_sort_desc(arr, p+1, high)
    

# Generate a list of 20 random numbers between 50 and 100
random_numbers = [random.randint(50, 100) for _ in range(20)]
print("Unsorted List: ", random_numbers)

# TODO: Use the Quick Sort function to sort the list in descending order and print the sorted list
quick_sort_desc(random_numbers, 0, len(random_numbers) - 1)
print("Sorted List: ", random_numbers)