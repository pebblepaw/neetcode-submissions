class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1
        mid = 0

        while l < r: 

            mid = (l + r) //2

            if nums[mid] > nums[r]: 
                l = mid + 1
            else: 
                r = mid 
        
        pivot = r
        # l,r = mid, len(nums)-1
        print(f'mid is {nums[r]}')

        if target >= nums[pivot] and target <= nums[-1]: 
            l, r = pivot, len(nums)-1
        else: 
            l,r = 0, pivot -1

        print(f'l {l}, r {r}')
        
        while l <= r: 
            mid = (l+r) // 2
            if target == nums[mid]: 
                return mid
            if target > nums[mid]: 
                l = mid+ 1
            else: 
                r = mid -1 
        
        return -1
        





        # #My own solution (bad)
        # l, r = 0, len(nums)-1

        # mid = 0

        # while l < r: 
            
        #     mid = (r + l) // 2

        #     if nums[mid] > nums[r]: 
        #         l = mid + 1
        #     else: 
        #         r = mid

        # l1, r1 = 0, l-1
        # l2, r2 = l, len(nums)-1

        # while l1 <= r1: 
        #     mid = (r1 + l1) //2
        #     if nums[mid] == target: 
        #         return mid
            
        #     if nums[mid] > target: 
        #         r1 = mid - 1
        #     else: 
        #         l1 = mid + 1

        # while l2 <= r2: 
        #     mid = (r2 + l2) //2
        #     if nums[mid] == target: 
        #         return mid 
            
        #     if nums[mid] > target: 
        #         r2 = mid - 1
        #     else: 
        #         l2 = mid + 1
        
        # return -1
        


            
        