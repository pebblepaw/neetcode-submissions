class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        x = Counter(nums) 

        y = {}
        for a,b in x.items():
            if b != 2: 
                return a

        