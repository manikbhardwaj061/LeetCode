from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:

  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class Solution:

  def pathSum(
      self, root: Optional[TreeNode], targetSum: int
  ) -> List[List[int]]:
    result = []

    def dfs(node: Optional[TreeNode], current_path: List[int], current_sum: int):
      if not node:
        return

      # Add current node value to path and sum
      current_path.append(node.val)
      current_sum += node.val

      # Check if we reached a leaf node
      if not node.left and not node.right:
        if current_sum == targetSum:
          result.append(list(current_path))  # Append a copy of current_path
      else:
        # Recurse on left and right subtrees
        dfs(node.left, current_path, current_sum)
        dfs(node.right, current_path, current_sum)

      # Backtrack: remove current node before returning to parent
      current_path.pop()

    dfs(root, [], 0)
    return result