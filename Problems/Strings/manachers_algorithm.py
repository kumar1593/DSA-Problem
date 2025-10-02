def manachers_algorithm(s):
    """Manacher's Algorithm - finds all palindromes in O(n) time"""
    # Preprocess string: insert '#' between characters
    processed = '#'.join('^{}$'.format(s))
    n = len(processed)
    
    # Array to store radius of palindromes
    radius = [0] * n
    center = right = 0
    
    for i in range(1, n - 1):
        # Mirror of i with respect to center
        mirror = 2 * center - i
        
        if i < right:
            radius[i] = min(right - i, radius[mirror])
        
        # Try to expand palindrome centered at i
        try:
            while processed[i + (1 + radius[i])] == processed[i - (1 + radius[i])]:
                radius[i] += 1
        except IndexError:
            pass
        
        # If palindrome centered at i extends past right, adjust center and right
        if i + radius[i] > right:
            center, right = i, i + radius[i]
    
    return radius, processed

def find_longest_palindrome(s):
    """Find the longest palindromic substring"""
    radius, processed = manachers_algorithm(s)
    
    max_len = 0
    center_index = 0
    
    for i in range(len(radius)):
        if radius[i] > max_len:
            max_len = radius[i]
            center_index = i
    
    # Convert back to original string indices
    start = (center_index - max_len) // 2
    return s[start:start + max_len]

def count_palindromes(s):
    """Count total number of palindromic substrings"""
    radius, _ = manachers_algorithm(s)
    count = 0
    
    for r in radius:
        count += (r + 1) // 2
    
    return count

def all_palindromes(s):
    """Get all palindromic substrings"""
    radius, processed = manachers_algorithm(s)
    palindromes = []
    
    for i in range(len(radius)):
        for j in range(radius[i] + 1):
            start = (i - j) // 2
            end = (i + j) // 2
            if start >= 0 and end < len(s):
                palindrome = s[start:end + 1]
                if len(palindrome) > 0:
                    palindromes.append(palindrome)
    
    return list(set(palindromes))

# Interactive mode with user input
if __name__ == "__main__":
    print("Manacher's Algorithm - Palindrome Detection")
    print("=" * 40)
    
    s = input("Enter a string to analyze: ")
    
    print(f"\nAnalyzing string: '{s}'")
    print("-" * 30)
    
    # Find longest palindrome
    longest = find_longest_palindrome(s)
    print(f"Longest palindrome: '{longest}' (length: {len(longest)})")
    
    # Count total palindromes
    total_count = count_palindromes(s)
    print(f"Total palindromic substrings: {total_count}")
    
    # Show all palindromes
    choice = input("\nShow all palindromes? (y/n): ").lower()
    if choice == 'y':
        all_pals = all_palindromes(s)
        print(f"\nAll palindromic substrings:")
        for i, pal in enumerate(sorted(all_pals, key=len, reverse=True), 1):
            print(f"  {i}. '{pal}' (length: {len(pal)})")
    
    print(f"\nTime complexity: O(n) where n = {len(s)}")