class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        cur_val = 0
        max_val =max(candies)
        

        for candy in candies:
            cur_val = candy + extraCandies

            if cur_val >= max_val:
                res.append(True)
            else:
                res.append(False)
        return res