class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        min_price = float('inf')
        for price in prices:
            if price < min_price:
                min_price = price

            elif (price-min_price) > max_price:
                max_price = price-min_price
            
        return max_price