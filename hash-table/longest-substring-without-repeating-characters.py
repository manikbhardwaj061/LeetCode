class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # Maps character -> its last seen index
        left = 0
        max_length = 0
        
        for right, char in enumerate(s):
            # If the character was seen inside the current window, move the left pointer
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            
            # Update last seen index of current character
            char_map[char] = right
            
            # Calculate window size and update max_length
            max_length = max(max_length, right - left + 1)
            
        return max_length


# --- Example Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    print(sol.lengthOfLongestSubstring("abcabcbb"))  # Output: 3 ("abc")
    
    # Example 2
    print(sol.lengthOfLongestSubstring("bbbbb"))     # Output: 1 ("b")
    
    # Example 3
    print(sol.lengthOfLongestSubstring("pwwkew"))    # Output: 3 ("wke")
    
    # Edge Cases
    print(sol.lengthOfLongestSubstring(""))          # Output: 0
    print(sol.lengthOfLongestSubstring(" "))         # Output: 1