class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if not intervals: 
            return intervals
        intervals.sort()
        output = []

        for start, end in intervals: 
            if not output:
                output.append([start,end])
            
            # if [2,4]'s start is before [1,2]'s end, then overlap 
            if start <= output[-1][1]:  
                # update the end
                output[-1][1] = max(end, output[-1][1])
                continue
            
            output.append([start,end])
        
        return output 