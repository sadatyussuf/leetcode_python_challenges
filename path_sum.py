# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def cal_path_sum(root,reminder):
            if root is None:
                return False
            if not root.left and not root.right:
                return root.val == reminder
            
            left = cal_path_sum(root.left,reminder-root.val)
            right = cal_path_sum(root.right,reminder-root.val)
            
            return left or right
        
        res = cal_path_sum(root,targetSum)
        return res