def insert_position(nums, target):
    # implement this
    left, right = 0, len(nums) - 1
    result = len(nums)  # Default insert position if target is larger than all elements
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] >= target:
            result = mid  # Potential answer; if target exists, this will be the leftmost occurrence
            right = mid - 1  # Search left half to find the leftmost
        else:
            left = mid + 1  # Search right half
    
    return result

print(insert_position([1, 2, 3, 3, 5], 3))  # Expected output: 2
print(insert_position([1, 2, 3, 3, 5], 4))  # Expected output: 4
print(insert_position([1, 3, 5, 7, 9], 10)) # Expected output: 5