
from collections import Counter


class Solution:

  def largestInteger(self, nums: list[int], k: int) -> int:
    n = len(nums)

    # Case 1: k == n (all elements are in 1 subarray)
    if k == n:
      return max(nums)

    # Case 2: k == 1 (count frequencies of single elements)
    if k == 1:
      freq = Counter(nums)
      ans = -1
      for x, count in freq.items():
        if count == 1:
          ans = max(ans, x)
      return ans

    # Case 3: 1 < k < n (only nums[0] or nums[-1] can appear in 1 subarray)
    ans = -1
    if nums.count(nums[0]) == 1:
      ans = max(ans, nums[0])
    if nums.count(nums[-1]) == 1:
      ans = max(ans, nums[-1])

    return ans