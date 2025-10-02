def insertion_sort(arr, left, right):
    """Insertion sort for small arrays"""
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def median_of_three(arr, low, high):
    """Find median of three elements for better pivot selection"""
    mid = (low + high) // 2
    if arr[mid] < arr[low]:
        arr[low], arr[mid] = arr[mid], arr[low]
    if arr[high] < arr[low]:
        arr[low], arr[high] = arr[high], arr[low]
    if arr[high] < arr[mid]:
        arr[mid], arr[high] = arr[high], arr[mid]
    return mid

def three_way_partition(arr, low, high, pivot):
    """3-way partitioning for handling duplicates"""
    i = low
    lt = low
    gt = high
    
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    
    return lt, gt

def quick_sort_optimized(arr, low=0, high=None):
    """Optimized Quick Sort with 3-way partitioning and hybrid approach"""
    if high is None:
        high = len(arr) - 1
    
    # Use insertion sort for small arrays
    if high - low + 1 <= 10:
        insertion_sort(arr, low, high)
        return arr
    
    if low < high:
        # Median-of-three pivot selection
        pivot_idx = median_of_three(arr, low, high)
        pivot_value = arr[pivot_idx]
        
        # 3-way partitioning
        lt, gt = three_way_partition(arr, low, high, pivot_value)
        
        # Recursively sort partitions
        quick_sort_optimized(arr, low, lt - 1)
        quick_sort_optimized(arr, gt + 1, high)
    
    return arr

def quick_sort_basic(arr, low=0, high=None):
    """Basic Quick Sort implementation"""
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Partition
        pivot = partition_basic(arr, low, high)
        
        # Recursively sort elements
        quick_sort_basic(arr, low, pivot - 1)
        quick_sort_basic(arr, pivot + 1, high)
    
    return arr

def partition_basic(arr, low, high):
    """Basic partition function"""
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_iterative(arr):
    """Iterative Quick Sort to avoid recursion overhead"""
    stack = [(0, len(arr) - 1)]
    
    while stack:
        low, high = stack.pop()
        
        if low < high:
            # Use insertion sort for small subarrays
            if high - low + 1 <= 10:
                insertion_sort(arr, low, high)
                continue
            
            # Partition
            pivot = partition_basic(arr, low, high)
            
            # Push subarrays to stack
            stack.append((low, pivot - 1))
            stack.append((pivot + 1, high))
    
    return arr

# Interactive mode
if __name__ == "__main__":
    print("Quick Sort Algorithms")
    print("=" * 20)
    
    input_str = input("Enter numbers separated by spaces: ")
    arr = list(map(int, input_str.split()))
    
    print(f"\nOriginal array: {arr}")
    
    print("\nChoose Quick Sort variant:")
    print("1. Basic Quick Sort")
    print("2. Optimized Quick Sort (3-way + hybrid)")
    print("3. Iterative Quick Sort")
    
    choice = input("Enter choice (1-3): ")
    
    if choice == "1":
        sorted_arr = quick_sort_basic(arr.copy())
        print(f"Sorted array (Basic): {sorted_arr}")
    elif choice == "2":
        sorted_arr = quick_sort_optimized(arr.copy())
        print(f"Sorted array (Optimized): {sorted_arr}")
    elif choice == "3":
        sorted_arr = quick_sort_iterative(arr.copy())
        print(f"Sorted array (Iterative): {sorted_arr}")
    else:
        sorted_arr = quick_sort_optimized(arr.copy())
        print(f"Sorted array (Default Optimized): {sorted_arr}")
    
    print(f"\nTime Complexity: O(n log n) average, O(n²) worst")
    print(f"Space Complexity: O(log n) average")
    print(f"Array size: {len(arr)}")