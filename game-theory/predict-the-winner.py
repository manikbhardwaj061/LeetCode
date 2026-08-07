class Solution:
    def predictTheWinner(self, nums: list[int]) -> bool:
        n = len(nums)
        # dp[i] will store the maximum relative score surplus (Player 1 - Player 2)
        # for the subarray nums[i...j].
        dp = list(nums)
        
        # Iterate over all subarray lengths from 2 up to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                # The current player can pick nums[i] or nums[j].
                # They gain that value minus the opponent's max advantage on the rest.
                dp[i] = max(nums[i] - dp[i + 1], nums[j] - dp[i])
                
        # Player 1 wins if their net score difference is >= 0
        return dp[0] >= 0
# --- Example Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    nums1 = [1, 5, 2]
    print(sol.predictTheWinner(nums1))  # Output: False
    
    # Example 2
    nums2 = [1, 5, 233, 7]
    print(sol.predictTheWinner(nums2))