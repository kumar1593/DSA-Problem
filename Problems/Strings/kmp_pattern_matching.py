def compute_lps(pattern):
    """Compute Longest Prefix Suffix array"""
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    """KMP Pattern Matching Algorithm - O(n+m) time complexity"""
    n = len(text)
    m = len(pattern)
    
    if m == 0:
        return []
    
    lps = compute_lps(pattern)
    matches = []
    
    i = 0  # text index
    j = 0  # pattern index
    
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == m:
            matches.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return matches

# Interactive mode with user input
if __name__ == "__main__":
    print("KMP Pattern Matching Algorithm")
    print("=" * 30)
    
    text = input("Enter the text: ")
    pattern = input("Enter the pattern to search: ")
    
    result = kmp_search(text, pattern)
    
    if result:
        print(f"\nPattern '{pattern}' found at indices: {result}")
        print(f"Total occurrences: {len(result)}")
    else:
        print(f"\nPattern '{pattern}' not found in the text.")
    
    # Display matches in context
    if result:
        print("\nMatches in context:")
        for idx in result:
            start = max(0, idx - 10)
            end = min(len(text), idx + len(pattern) + 10)
            context = text[start:end]
            pattern_start = idx - start
            pattern_end = pattern_start + len(pattern)
            
            print(f"Index {idx}: ...{context[:pattern_start]}[{context[pattern_start:pattern_end]}]{context[pattern_end:]}...")