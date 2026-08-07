from typing import List

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        last_seen = {}
        min_dist = float('inf')
        
        for j, num in enumerate(nums):
            # Check if num[j] matches the reversed value of any previous element
            if num in last_seen:
                min_dist = min(min_dist, j - last_seen[num])
            
            # Reverse the digits of the current number (omitting leading zeros)
            reversed_num = int(str(num)[::-1])
            
            # Record/update the most recent index for this target reversed number
            last_seen[reversed_num] = j
            
        return min_dist if min_dist != float('inf') else -1