from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        # dp1, dp2, dp3 represent dp[i+1], dp[i+2], dp[i+3] respectively
        dp1 = dp2 = dp3 = 0
        
        for i in range(n - 1, -1, -1):
            ans = float('-inf')
            
            # Take 1 stone
            ans = max(ans, stoneValue[i] - dp1)
            
            # Take 2 stones
            if i + 1 < n:
                ans = max(ans, stoneValue[i] + stoneValue[i+1] - dp2)
                
            # Take 3 stones
            if i + 2 < n:
                ans = max(ans, stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp3)
            
            # Shift states backwards
            dp3, dp2, dp1 = dp2, dp1, ans
            
        if dp1 > 0:
            return "Alice"
        elif dp1 < 0:
            return "Bob"
        else:
            return "Tie"
        