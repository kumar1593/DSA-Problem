def counting_sort(arr, exp=None):
    """Counting sort for radix sort or standalone use"""
    if exp is None:  # Standalone counting sort
        if not arr:
            return arr
        
        max_val = max(arr)
        min_val = min(arr)
        range_size = max_val - min_val + 1
        
        # Count array
        count = [0] * range_size
        output = [0] * len(arr)
        
        # Count occurrences
        for num in arr:
            count[num - min_val] += 1
        
        # Cumulative count
        for i in range(1, range_size):
            count[i] += count[i - 1]
        
        # Build output array
        for i in range(len(arr) - 1, -1, -1):
            output[count[arr[i] - min_val] - 1] = arr[i]
            count[arr[i] - min_val] -= 1
        
        return output
    
    else:  # For radix sort
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        
        # Count occurrences of each digit
        for i in range(n):
            index = (arr[i] // exp) % 10
            count[index] += 1
        
        # Cumulative count
        for i in range(1, 10):
            count[i] += count[i - 1]
        
        # Build output array
        i = n - 1
        while i >= 0:
            index = (arr[i] // exp) % 10
            output[count[index] - 1] = arr[i]
            count[index] -= 1
            i -= 1
        
        # Copy output array to arr
        for i in range(len(arr)):
            arr[i] = output[i]

def radix_sort(arr):
    """Radix Sort - Non-comparison based sorting"""
    if not arr:
        return arr
    
    # Handle negative numbers
    negative = []
    positive = []
    
    for num in arr:
        if num < 0:
            negative.append(-num)
        else:
            positive.append(num)
    
    # Sort positive numbers
    if positive:
        max_num = max(positive)
        exp = 1
        while max_num // exp > 0:
            counting_sort(positive, exp)
            exp *= 10
    
    # Sort negative numbers (as positive, then reverse)
    if negative:
        max_num = max(negative)
        exp = 1
        while max_num // exp > 0:
            counting_sort(negative, exp)
            exp *= 10
        negative = [-num for num in reversed(negative)]
    
    return negative + positive

def radix_sort_strings(arr):
    """Radix sort for strings of equal length"""
    if not arr or not arr[0]:
        return arr
    
    max_len = len(arr[0])
    
    # Sort from rightmost to leftmost character
    for pos in range(max_len - 1, -1, -1):
        # Use counting sort for current character position
        buckets = [[] for _ in range(256)]  # ASCII characters
        
        for string in arr:
            char_code = ord(string[pos]) if pos < len(string) else 0
            buckets[char_code].append(string)
        
        # Reconstruct array
        arr = []
        for bucket in buckets:
            arr.extend(bucket)
    
    return arr

def counting_sort_for_integers(arr):
    """Standalone counting sort for integer arrays"""
    return counting_sort(arr)

# Interactive mode
if __name__ == "__main__":
    print("Radix Sort & Counting Sort")
    print("=" * 25)
    
    print("Choose sorting type:")
    print("1. Radix Sort (integers)")
    print("2. Counting Sort (integers)")
    print("3. Radix Sort (strings of equal length)")
    
    choice = input("Enter choice (1-3): ")
    
    if choice == "1":
        input_str = input("\nEnter integers separated by spaces: ")
        arr = list(map(int, input_str.split()))
        print(f"Original array: {arr}")
        
        sorted_arr = radix_sort(arr.copy())
        print(f"Sorted array (Radix Sort): {sorted_arr}")
        print(f"Time Complexity: O(d * (n + k)) where d=digits, k=range")
    
    elif choice == "2":
        input_str = input("\nEnter integers separated by spaces: ")
        arr = list(map(int, input_str.split()))
        print(f"Original array: {arr}")
        
        sorted_arr = counting_sort_for_integers(arr)
        print(f"Sorted array (Counting Sort): {sorted_arr}")
        print(f"Time Complexity: O(n + k) where k=range of input")
    
    elif choice == "3":
        input_str = input("\nEnter strings of equal length separated by spaces: ")
        arr = input_str.split()
        
        if arr and len(set(len(s) for s in arr)) > 1:
            print("Error: All strings must have equal length!")
        else:
            print(f"Original array: {arr}")
            sorted_arr = radix_sort_strings(arr)
            print(f"Sorted array (String Radix Sort): {sorted_arr}")
            print(f"Time Complexity: O(d * n) where d=string length")
    
    else:
        print("Invalid choice!")