class Solution:
    def rob(self, nums: List[int]) -> int:
        

        p, pp = 0,0

        for num in nums: 
            
            cur = max(p, pp+num)
            pp = p 
            p = cur 
            
        return p

        # # edge cases 
        # if not nums: 
        #     return 0 
        # if len(nums) == 1: 
        #     return nums[0]
        # if len(nums) ==2: 
        #     return max(nums[0], nums[1])

        # # base cases 
        # num_houses = len(nums)+1
        # dp = [0] * (num_houses+1)
        # dp[0] = 0
        # dp[1] = nums[0]

        # # 10 houses, house 1 to house 10
        # # for each house, house 1 to house 10 
        # for i in range(2,num_houses):

        #     # either the previous house i.e. don't rob this one
        #     # of 2 houses ago + this house's value
        #     dp[i] = max(dp[i-1], dp[i-2] + nums[i-1]) 

        # if dp[num_houses-1] != 0: 
        #     return dp[num_houses-1]
        # return 0


