# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def cal_max_depth(root):
            if not root:
                return 0
            
            return 1 + max(cal_max_depth(root.left),cal_max_depth(root.right))
        return cal_max_depth(root)
