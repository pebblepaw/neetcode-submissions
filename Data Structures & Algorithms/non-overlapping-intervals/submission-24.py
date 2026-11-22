class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        if len(intervals) < 2: 
            return 0

        intervals.sort(key = lambda i: (i[0], i[1]))
        # print(f'intervals:{intervals}')
        
        res = 0
        _i = 0 # keeping one index 

        
        for i in range(1,len(intervals)): 
            
            if intervals[i][0] < intervals[_i][1]: 

                # print(f'removed: {intervals[i]} because of {intervals[_i]}')
                res += 1 
        
                if intervals[i][1] < intervals[_i][1]: 
                    # print(f'changed i to {intervals[i]}')
                    _i =i
            else: 
                _i = i 

        return res
            
            
            