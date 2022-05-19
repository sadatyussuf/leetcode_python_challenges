from typing import List

class Solution:
    def twoSum(self,nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index,i in enumerate(nums):
          sub = target - i
          if sub in hashmap:
            results = [hashmap[sub], index]
            return results
          hashmap[i] = index