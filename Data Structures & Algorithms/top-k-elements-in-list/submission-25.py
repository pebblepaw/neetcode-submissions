class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq 

        _counter = Counter(nums)
        q = []

        for value, count in _counter.items():
            # Negate count so the largest count becomes the smallest number (popped first)
            heapq.heappush(q, [-count, value])

        res = []
        for _ in range(k):
            res.append(heapq.heappop(q)[1])

        return res
