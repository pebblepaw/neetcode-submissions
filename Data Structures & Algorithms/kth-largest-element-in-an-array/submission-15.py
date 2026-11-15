class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        import heapq 
        from collections import Counter

        if not nums or not k: 
            return None

        _counter = Counter(nums)

        q = []

        for num, count in _counter.items(): 
            heapq.heappush(q, (-num, count))
        
        sum = 0
        while sum < k: 
            res_num, res_count = heapq.heappop(q) 
            sum += res_count 
        
        return -res_num
        