class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left, right = 0, len(heights) - 1

        _max = 0 

        while left < right: 

            volume = min(heights[left], heights[right]) * (right - left)

            _max = max(volume, _max)

            if heights[left] < heights[right]: 
                left +=1 
                continue
            
            else: 
                right -= 1 
                continue
        
        return _max
        