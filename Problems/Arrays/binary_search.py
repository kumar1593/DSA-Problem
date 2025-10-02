def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example (array must be sorted)
arr = [11, 15, 23, 45, 70]
print("Binary Search:", binary_search(arr, 45))  # Output: 3
