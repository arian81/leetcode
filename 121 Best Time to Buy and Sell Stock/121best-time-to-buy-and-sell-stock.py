class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = 1000000

        for i in prices:
            min_buy = min(min_buy, i)
            max_profit = max(max_profit, i - min_buy)
        return max_profit
            