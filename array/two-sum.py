class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}  # Maps number -> its index
        
        for index, num in enumerate(nums):
            complement = target - num
            
            # Check if the needed complement has already been seen
            if complement in seen:
                return [seen[complement], index]
            
            # Store current number and its index
            seen[num] = index
            
        return []


# --- Example Test Cases ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
    
    # Example 2
    print(sol.twoSum([3, 2, 4], 6))       # Output: [1, 2]
    
    # Example 3
    print(sol.twoSum([3, 3], 6))          # Output: [0, 1]