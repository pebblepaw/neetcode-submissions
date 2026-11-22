class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        from collections import defaultdict 

        if len(s) <= 2: 
            return len(s)

        maxf = 0 
        count = defaultdict(int)
        count[s[0]] = 0
        l = 0 

        for r in range(len(s)): 
            
            # print(f'looking at string: {s[l:r]}')
            # print(count)

            count[s[r]] += 1
            max_sofar = max(count.values())
            
            # print(f'maxsofar: {max_sofar}')

            if ((r - l + 1) - max_sofar) > k: 
                
                # print(f'reached here: {r-l+1} and {max_sofar}')
                count[s[l]] -= 1
                l += 1
                continue
            
            maxf = max(maxf, r-l+1)
            # print(f'current maxf {maxf}')
        
        return maxf

