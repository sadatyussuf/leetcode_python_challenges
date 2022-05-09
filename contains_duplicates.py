class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        remove_dup = set(nums)
        if len(remove_dup) == len(nums):
            return False
            return True
