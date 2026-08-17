from bisect import bisect_right

class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        n = len(stoneValue)
        if n <= 1:
            return 0
        
        # Compute prefix sums array
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stoneValue[i]
            
        dp = [[0] * n for _ in range(n)]
        max_left = [[0] * n for _ in range(n)]
        max_right = [[0] * n for _ in range(n)]
        
        # Base cases initialization (intervals of length L = 1)
        for i in range(n):
            max_left[i][i] = pref[i + 1]
            max_right[i][i] = -pref[i]
            
        # Iterate over subsegment length L from 2 to n
        for L in range(2, n + 1):
            for i in range(n - L + 1):
                j = i + L - 1
                
                # Find mid such that 2 * pref[mid + 1] <= pref[j + 1] + pref[i]
                target = (pref[j + 1] + pref[i]) // 2
                mid = bisect_right(pref, target) - 2
                
                ans = 0
                
                # Range 1: k <= mid, where left_sum <= right_sum
                if mid >= i:
                    ans = max(ans, max_left[i][mid] - pref[i])
                    
                # Range 2: k > mid, where right_sum <= left_sum
                # If left_sum == right_sum at mid, k = mid is also valid for right choice
                if mid >= 0 and 2 * pref[mid + 1] == pref[j + 1] + pref[i]:
                    right_start = mid + 1
                else:
                    right_start = mid + 2
                    
                if right_start <= j:
                    ans = max(ans, pref[j + 1] + max_right[right_start][j])
                    
                dp[i][j] = ans
                
                # Update max_left and max_right prefix/suffix max tables
                max_left[i][j] = max(max_left[i][j - 1], pref[j + 1] + ans)
                max_right[i][j] = max(max_right[i + 1][j], ans - pref[i])
                
        return dp[0][n - 1]