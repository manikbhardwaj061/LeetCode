from typing import List
from functools import reduce
import operator

class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        # Case 1: If all elements are 0, no subsequence can have a non-zero XOR.
        if not any(nums):
            return 0
        
        # Calculate the bitwise XOR of all elements
        total_xor = reduce(operator.xor, nums, 0)
        
        # Case 2: If the total XOR is non-zero, the longest subsequence is the whole array.
        if total_xor != 0:
            return len(nums)
        
        # Case 3: If total XOR is 0 but there are non-zero elements,
        # removing one non-zero element leaves a subsequence of length N - 1 with non-zero XOR.
        return len(nums) - 1