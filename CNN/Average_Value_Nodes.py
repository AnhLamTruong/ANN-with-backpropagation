# Definition for a binary tree node.

from typing import Optional
from typing import List
from collections import defaultdict

from traitlets import default
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        level_count=defaultdict(int);
        level_sum=defaultdict(int);
        def dfs(node=root, level=0):
          if not node:
            return
          level_count[level] += 1
          level_sum[level] += node.val
          dfs(node.left, level+1)
          dfs(node.right, level+1)
        dfs()
        return [level_sum[i] / level_count[i] for i in range(len(level_count))]


root=None
root=TreeNode(3)
root.left=TreeNode(3)
root.right=TreeNode(20)
root.right.left=TreeNode(15)
root.right.right=TreeNode(7)

s=Solution();
print(s.averageOfLevels(root))