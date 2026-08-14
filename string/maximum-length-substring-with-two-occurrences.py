from collections import defaultdict


class Solution:

  def maximumLengthSubstring(self, s: str) -> int:
    counts = defaultdict(int)
    left = 0
    max_len = 0

    for right in range(len(s)):
      # Expand the window to the right
      char = s[right]
      counts[char] += 1

      # Shrink the window from the left if any character count exceeds 2
      while counts[char] > 2:
        counts[s[left]] -= 1
        left += 1

      # Update the maximum valid window size found so far
      max_len = max(max_len, right - left + 1)

    return max_len