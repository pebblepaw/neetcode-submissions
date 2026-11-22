class Solution:
    def reverseBits(self, n: int) -> int:
        
        res = 0 
        counter = 32

        while n: 
            res = res << 1
            counter -= 1 
            res += (n%2)
            n = n >> 1 

        while counter: 
            res = res << 1
            counter -= 1
        
        return res

