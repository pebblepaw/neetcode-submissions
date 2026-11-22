class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        import heapq
        import math

        if not points: 
            return []

        h = []
        x2, y2 = 0,0
        for x1, y1 in points: 
            dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
            heapq.heappush(h,(dist,[x1,y1]))

        
        res = []
        while k: 
            res.append(heapq.heappop(h)[1])
            k-=1
        
        return res

        
            
