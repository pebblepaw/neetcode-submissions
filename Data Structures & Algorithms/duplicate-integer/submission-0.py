class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_unique = []
        for num in nums: 
            if num in list_unique: 
                return True
            else: 
                list_unique.append(num)
            
        return False

        