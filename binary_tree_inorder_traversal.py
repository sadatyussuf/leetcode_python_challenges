# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []

        def inorder(root):
            if root is None:
                return 
            inorder(root.left)
            result.append(root.val)
            inorder(root.right)
            
        inorder(root)
        return result