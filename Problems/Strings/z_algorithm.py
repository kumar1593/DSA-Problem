def z_algorithm(s):
    """Z Algorithm - computes Z array where Z[i] is length of longest substring starting from i which is also prefix"""
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    
    return z

def pattern_search_z(text, pattern):
    """Pattern searching using Z algorithm - O(n+m) time"""
    combined = pattern + "$" + text
    z_array = z_algorithm(combined)
    
    pattern_len = len(pattern)
    matches = []
    
    for i in range(len(combined)):
        if z_array[i] == pattern_len:
            matches.append(i - pattern_len - 1)
    
    return matches

def find_all_occurrences(s, pattern):
    """Find all occurrences of pattern in string using Z algorithm"""
    return pattern_search_z(s, pattern)

# Interactive mode with user input
if __name__ == "__main__":
    print("Z Algorithm - Pattern Matching & Z Array")
    print("=" * 40)
    
    choice = input("Choose option:\n1. Compute Z array for a string\n2. Pattern matching\nEnter choice (1 or 2): ")
    
    if choice == "1":
        s = input("\nEnter string to compute Z array: ")
        z_arr = z_algorithm(s)
        print(f"\nZ array for '{s}': {z_arr}")
        
        # Show meaning of Z values
        print("\nZ array explanation:")
        for i, val in enumerate(z_arr):
            if val > 0:
                print(f"  Z[{i}] = {val}: substring '{s[i:i+val]}' matches prefix")
    
    elif choice == "2":
        text = input("\nEnter the text: ")
        pattern = input("Enter the pattern to search: ")
        
        matches = pattern_search_z(text, pattern)
        
        if matches:
            print(f"\nPattern '{pattern}' found at indices: {matches}")
            print(f"Total occurrences: {len(matches)}")
        else:
            print(f"\nPattern '{pattern}' not found in the text.")
    
    else:
        print("Invalid choice!")