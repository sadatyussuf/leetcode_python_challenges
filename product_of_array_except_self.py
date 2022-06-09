from typing import List

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    counter = 1
    n = len(nums)
    results = []
    for i in range(0,n):
      results.append(counter)
      counter *=  nums[i]
    # 
    counter = 1 
    for i in range(n-1,-1,-1):
      results[i] *=  counter
      counter *=  nums[i]
    # 
    return results