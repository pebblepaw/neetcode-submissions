class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # if not nums: 
        #     return [[]]

        # res = []
        # subset = [] 

        # # depth of tree
        # def dfs(i):
            
        #     # every leaf, every subset ends up here bro
        #     if i >= len(nums): 
        #         res.append(subset.copy())
        #         return 
            
        #     subset.append(nums[i])
        #     dfs(i+1)
        #     subset.pop()
        #     dfs(i+1)

        # dfs(0)
        # return res

        if not nums: 
            return []

        res = [[]]

        for i in nums: 
            res += [item + [i] for item in res]

        return res
