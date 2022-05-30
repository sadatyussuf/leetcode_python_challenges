from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        results = []
        for i in range(len(nums)):
            num = nums[i]
            if num not in hashmap:
              hashmap[num] = 1
            # If the item is in the hashmap increse the value
        else:
          hashmap[num] = hashmap[num] + 1
        # sort the items in the hashmap in descending order
        hashmap = sorted(hashmap.items(),key = lambda x:x[1],reverse = True)[:k]
        for key_value in hashmap:
            key = key_value[0]
            results.append(key)
        # return the results
        return results