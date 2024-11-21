class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [0] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            min_coins = float("inf") 
            for coin in coins:
                remainder = i - coin
                if remainder >= 0:
                    curr_count = 1 + dp[remainder]
                    min_coins = min(min_coins, curr_count)
            
            dp[i] = min_coins
        print(dp)
        if dp[-1] != float("inf"):
            return dp[-1]
        
        return -1