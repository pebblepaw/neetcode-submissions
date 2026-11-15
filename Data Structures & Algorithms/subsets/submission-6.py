class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        if not nums: 
            return []

        # try defs first
        res = []
        subset = []

        def dfs(i): 

            # end when we've covered every item basically 
            if i >= len(nums): 
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i+1)
            subset.pop() #remove the number just added for this step
            dfs(i+1)
        
        dfs(0)
        return res

