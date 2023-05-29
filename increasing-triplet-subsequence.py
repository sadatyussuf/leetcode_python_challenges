class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_val = float("inf")
        max_val = float("inf")
       

        for num in nums:
            if num <= min_val:
                min_val = num
            elif num <= max_val:
                max_val = num
            else:
                return True
        else:
            return False
            
      