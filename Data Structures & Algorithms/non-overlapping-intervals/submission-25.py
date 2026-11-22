class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if len(intervals) < 2: 
            return 0

        intervals.sort(key = lambda i: (i[1], i[0]))
        # print(f'intervals:{intervals}')
        
        res = 0
        _i = 0 # keeping one index 

        
        for i in range(1,len(intervals)): 
            
            if intervals[i][0] < intervals[_i][1]: 

                res+=1 
            else: 
                _i = i

        return res
            
            
            