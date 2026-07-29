# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invert(self, current: Optional[TreeNode]) -> None:
        if current is None:
            return
        self.invert(current.left)
        self.invert(current.right)
        current.left, current.right = current.right, current.left

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invert(root)
        return root
