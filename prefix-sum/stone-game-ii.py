from typing import List
from functools import lru_cache

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        
        # Precalculate suffix sums: suffix_sum[i] = sum of piles[i:]
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        @lru_cache(None)
        def dp(i: int, M: int) -> int:
            # If current player can take all remaining piles
            if i + 2 * M >= n:
                return suffix_sum[i]
            
            max_stones = 0
            # Try taking X piles for 1 <= X <= 2 * M
            for X in range(1, 2 * M + 1):
                # Current player gets total remaining stones minus what the opponent gets
                stones = suffix_sum[i] - dp(i + X, max(M, X))
                if stones > max_stones:
                    max_stones = stones
                    
            return max_stones
            
        return dp(0, 1)

# Example Usage:
sol = Solution()
print(sol.stoneGameII([2, 7, 9, 4, 4]))       # Output: 10
print(sol.stoneGameII([1, 2, 3, 4, 5, 100]))   # Output: 104