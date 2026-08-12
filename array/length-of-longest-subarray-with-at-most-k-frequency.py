from collections import defaultdict
from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0
        max_length = 0
        
        for right in range(len(nums)):
            # Expand the window by adding the current element
            freq[nums[right]] += 1
            
            # If frequency of nums[right] exceeds k, shrink the window from the left
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1
            
            # Update the maximum valid subarray length found so far
            max_length = max(max_length, right - left + 1)
            
        return max_length
        