class Solution:
    def reverseBits(self, n: int) -> int:
        
        
        res = 0 

        for _ in range(32): 
            
            res = res << 1 
            
            add = n & 1
            n  = n >> 1 
            res = res | add
        
        return res 



        ## easier way 
        # res = 0 
        # counter = 32

        # while n: 
        #     res = res << 1
        #     counter -= 1 
        #     res += (n%2)
        #     n = n >> 1 

        # while counter: 
        #     res = res << 1
        #     counter -= 1
        
        # return res

