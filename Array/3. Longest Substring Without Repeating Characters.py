def lengthOfLongestSubstring(s):
    char_map = {} # Stores {character: last_seen_index}
    max_len = 0
    left = 0
    
    for right in range(len(s)):
        current_char = s[right]
        
        # If we've seen this char before and it's inside our current window
        if current_char in char_map and char_map[current_char] >= left:
            # Move left to the position right after the last occurrence
            left = char_map[current_char] + 1
        
        # Record/Update the index of the current character
        char_map[current_char] = right
        
        # Update the global maximum length found so far
        max_len = max(max_len, right - left + 1)
        
    return max_len

print(lengthOfLongestSubstring('rahullohra'))