# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        def cal_minDepth(root):
            if root is None:
                return 0
            
            left,right = cal_minDepth(root.left),cal_minDepth(root.right)

            if left == 0 or right == 0:
                return 1+ max(left,right)
            
            return 1+ min(left,right)
        
        res = cal_minDepth(root)
        
        return res
        