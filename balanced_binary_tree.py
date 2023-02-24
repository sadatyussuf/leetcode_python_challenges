# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_isBal(root):
            if root is None:
                return [True,-1]

            left,right=check_isBal(root.left),check_isBal(root.right)

            if abs(left[1]- right[1]) > 1:
                return [False,1 + max(left[1],right[1])]


            return [left[0] and right[0], 1 + max(left[1],right[1])]

        result = check_isBal(root)

        return result[0]
