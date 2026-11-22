class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [amount+1] * (amount + 1)
        dp[0] = 0 # base case, no coins needed

        # from 0 to 10 out of $10 
        for i in range(amount+1): 

            for coin in coins: 
                
                # if this amount - coin > 0: 
                if i - coin >= 0: 
                    dp[i] = min(dp[i], dp[i-coin] + 1)
        
        if dp[amount] != amount + 1: 
            return dp[amount]
        return -1
        