def heapify(arr, n, i):
    """Heapify subtree rooted at index i"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    """Heap Sort - O(n log n) time, O(1) space"""
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Move current root to end
        heapify(arr, i, 0)
    
    return arr

def heap_sort_iterative(arr):
    """Iterative version of heap sort"""
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        # Iterative heapify
        root = i
        while True:
            largest = root
            left = 2 * root + 1
            right = 2 * root + 2
            
            if left < n and arr[left] > arr[largest]:
                largest = left
            
            if right < n and arr[right] > arr[largest]:
                largest = right
            
            if largest != root:
                arr[root], arr[largest] = arr[largest], arr[root]
                root = largest
            else:
                break
    
    # Extract elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        
        # Heapify reduced heap
        root = 0
        while True:
            largest = root
            left = 2 * root + 1
            right = 2 * root + 2
            
            if left < i and arr[left] > arr[largest]:
                largest = left
            
            if right < i and arr[right] > arr[largest]:
                largest = right
            
            if largest != root:
                arr[root], arr[largest] = arr[largest], arr[root]
                root = largest
            else:
                break
    
    return arr

# Interactive mode
if __name__ == "__main__":
    print("Heap Sort Algorithm")
    print("=" * 20)
    
    # Get user input
    input_str = input("Enter numbers separated by spaces: ")
    arr = list(map(int, input_str.split()))
    
    print(f"\nOriginal array: {arr}")
    
    choice = input("Choose version (1: Recursive, 2: Iterative): ")
    
    if choice == "1":
        sorted_arr = heap_sort(arr.copy())
        print(f"Sorted array (Recursive): {sorted_arr}")
    elif choice == "2":
        sorted_arr = heap_sort_iterative(arr.copy())
        print(f"Sorted array (Iterative): {sorted_arr}")
    else:
        sorted_arr = heap_sort(arr.copy())
        print(f"Sorted array (Default Recursive): {sorted_arr}")
    
    print(f"\nTime Complexity: O(n log n)")
    print(f"Space Complexity: O(1)")
    print(f"Array size: {len(arr)}")