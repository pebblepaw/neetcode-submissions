class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        res = 0 

        for n in nums: 
            res = res ^ n
        
        return res


        ## Without bit wise 
        # x = Counter(nums) 

        # y = {}
        # for a,b in x.items():
        #     if b != 2: 
        #         return a

        