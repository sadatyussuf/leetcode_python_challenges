# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def insert_tree(nums,start,end):
            if start <= end:

                mid = (start+end)//2

                node_tree = TreeNode(nums[mid])

                node_tree.left = insert_tree(nums[:mid],start,len(nums[:mid])-1)
                node_tree.right =insert_tree(nums[mid+1:],start,len(nums[mid+1:])-1)
                return node_tree

        return insert_tree(nums, 0,len(nums)-1)