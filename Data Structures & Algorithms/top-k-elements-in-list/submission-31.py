class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq 

        _counter = Counter(nums)

        # print(f'counter { _counter}')

        q = []
        # heapq.heapify(q)

        for value, count in _counter.items():
            # MAX heap
            heapq.heappush(q, [-count, value])

        res = []

        for i in range(k): 
            if len(q) != 0:
                res.append(heapq.heappop(q)[1])

        return res