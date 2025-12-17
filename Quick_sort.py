def quickSortInPlace(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    # if subarray has 1 or 0 elements
    if low < high:
        # Partition and get pivot position
        pivot_index = partition(arr, low, high)
        
        # Recursively sort left side
        quickSortInPlace(arr, low, pivot_index - 1)
        
        # Recursively sort right side
        quickSortInPlace(arr, pivot_index + 1, high)
    
    return arr


def partition(arr, low, high):
    # Choosing last element as pivot
    pivot = arr[high]
    
    # i tracks the boundary between smaller and larger elements
    i = low - 1
    
    # Compare each element with pivot
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            # Swaping
            arr[i], arr[j] = arr[j], arr[i]
    
    # Placing pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# Test
arr = [64, 34, 25, 12, 22, 11, 90]
print(quickSortInPlace(arr))
# Output: [11, 12, 22, 25, 34, 64, 90]



