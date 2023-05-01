class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            if num in res:
                res.remove(num)
            else:
                res.append(num)

        return res[0]
            

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num

        return res
            
