class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l_pointer = 1
        for r_pointer in range(1,len(nums)):
            if nums[r_pointer] != nums[r_pointer - 1]:
                nums[l_pointer]=nums[r_pointer]

                l_pointer += 1
        return l_pointer