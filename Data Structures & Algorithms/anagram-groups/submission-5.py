class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict 

        res = defaultdict(list)

        for str in strs:
            _hashed = ''.join(sorted(str))

            res[_hashed].append(str)

        # print(list(res.values()))

        return list(res.values())