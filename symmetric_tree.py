# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def is_mirror(node_left,node_right):
            if node_left is None and node_right is None:
                return True
            if node_left is None or node_right is None:
                return False

            if node_left.val != node_right.val:
                return False
                
            print(node_left.val,node_right.val)
            
            return is_mirror(node_left.left,node_right.right) and is_mirror(node_left.right,node_right.left)
        if root is None:
            return True
        else:
            return is_mirror(root.left,root.right)
        