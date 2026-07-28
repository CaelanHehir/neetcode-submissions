# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def get_max_depth(self, current: Optional[TreeNode], depth: int) -> int:
        if current is None:
            return depth
        left_depth = self.get_max_depth(current.left, depth + 1)
        right_depth = self.get_max_depth(current.right, depth + 1)
        return max(left_depth, right_depth)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_depth = self.get_max_depth(root, 0)
        return max_depth

        