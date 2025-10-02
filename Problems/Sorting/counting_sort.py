def counting_sort_basic(arr):
    """Basic counting sort for non-negative integers"""
    if not arr:
        return arr
    
    max_val = max(arr)
    count = [0] * (max_val + 1)
    
    # Count occurrences
    for num in arr:
        count[num] += 1
    
    # Reconstruct sorted array
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])
    
    return sorted_arr

def counting_sort_stable(arr):
    """Stable counting sort that preserves relative order"""
    if not arr:
        return arr
    
    max_val = max(arr)
    min_val = min(arr)
    range_size = max_val - min_val + 1
    
    # Count array and output array
    count = [0] * range_size
    output = [0] * len(arr)
    
    # Count occurrences
    for num in arr:
        count[num - min_val] += 1
    
    # Convert to cumulative count
    for i in range(1, range_size):
        count[i] += count[i - 1]
    
    # Build output array (backwards to maintain stability)
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
    
    return output

def counting_sort_in_place(arr):
    """In-place counting sort (modifies original array)"""
    if not arr:
        return arr
    
    max_val = max(arr)
    min_val = min(arr)
    range_size = max_val - min_val + 1
    
    count = [0] * range_size
    
    # Count occurrences
    for num in arr:
        count[num - min_val] += 1
    
    # Reconstruct array in-place
    index = 0
    for i in range(range_size):
        while count[i] > 0:
            arr[index] = i + min_val
            index += 1
            count[i] -= 1
    
    return arr

def counting_sort_with_duplicates(arr):
    """Counting sort optimized for arrays with many duplicates"""
    if not arr:
        return arr
    
    # Use dictionary for sparse ranges
    count_dict = {}
    
    # Count occurrences
    for num in arr:
        count_dict[num] = count_dict.get(num, 0) + 1
    
    # Reconstruct sorted array
    sorted_arr = []
    for key in sorted(count_dict.keys()):
        sorted_arr.extend([key] * count_dict[key])
    
    return sorted_arr

def counting_sort_range(arr, min_val, max_val):
    """Counting sort when range is known"""
    if not arr:
        return arr
    
    range_size = max_val - min_val + 1
    count = [0] * range_size
    output = [0] * len(arr)
    
    # Count occurrences
    for num in arr:
        if min_val <= num <= max_val:
            count[num - min_val] += 1
    
    # Cumulative count
    for i in range(1, range_size):
        count[i] += count[i - 1]
    
    # Build output
    for i in range(len(arr) - 1, -1, -1):
        if min_val <= arr[i] <= max_val:
            output[count[arr[i] - min_val] - 1] = arr[i]
            count[arr[i] - min_val] -= 1
    
    return output

# Interactive mode
if __name__ == "__main__":
    print("Counting Sort Algorithms")
    print("=" * 23)
    
    input_str = input("Enter integers separated by spaces: ")
    arr = list(map(int, input_str.split()))
    
    print(f"\nOriginal array: {arr}")
    
    if not arr:
        print("Empty array!")
        exit()
    
    # Check if array has negative numbers
    has_negative = any(x < 0 for x in arr)
    
    print(f"\nArray info:")
    print(f"  Size: {len(arr)}")
    print(f"  Range: {min(arr)} to {max(arr)}")
    print(f"  Has negatives: {has_negative}")
    
    print("\nChoose counting sort variant:")
    print("1. Basic counting sort (non-negative only)")
    print("2. Stable counting sort (handles negatives)")
    print("3. In-place counting sort")
    print("4. Optimized for duplicates")
    print("5. Range-specified counting sort")
    
    choice = input("Enter choice (1-5): ")
    
    if choice == "1" and not has_negative:
        sorted_arr = counting_sort_basic(arr.copy())
        print(f"Sorted array (Basic): {sorted_arr}")
    elif choice == "2":
        sorted_arr = counting_sort_stable(arr.copy())
        print(f"Sorted array (Stable): {sorted_arr}")
    elif choice == "3":
        arr_copy = arr.copy()
        counting_sort_in_place(arr_copy)
        print(f"Sorted array (In-place): {arr_copy}")
    elif choice == "4":
        sorted_arr = counting_sort_with_duplicates(arr.copy())
        print(f"Sorted array (Duplicate-optimized): {sorted_arr}")
    elif choice == "5":
        min_range = int(input(f"Enter min value (current min: {min(arr)}): "))
        max_range = int(input(f"Enter max value (current max: {max(arr)}): "))
        sorted_arr = counting_sort_range(arr.copy(), min_range, max_range)
        print(f"Sorted array (Range {min_range}-{max_range}): {sorted_arr}")
    else:
        if choice == "1" and has_negative:
            print("Basic counting sort doesn't handle negative numbers!")
        sorted_arr = counting_sort_stable(arr.copy())
        print(f"Sorted array (Default Stable): {sorted_arr}")
    
    print(f"\nTime Complexity: O(n + k) where k = range of input")
    print(f"Space Complexity: O(k)")
    print(f"Stable: Yes (except in-place variant)")