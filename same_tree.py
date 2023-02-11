# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        root1= []
        root2 = []

        def traverse_tree(root,root_list:list):
            if root:
                root_list.append(root.val)
                if root.left:
                    traverse_tree(root.left,root_list)
                if root.left is None:
                    root_list.append('null')
                if root.right:
                    traverse_tree(root.right,root_list)
                if root.right is None:
                    root_list.append('null')
        traverse_tree(p,root1)
        traverse_tree(q,root2)
        if root1 == root2:
            return True
        return False