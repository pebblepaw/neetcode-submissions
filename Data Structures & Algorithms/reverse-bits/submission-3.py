class Solution:
    def reverseBits(self, n: int) -> int:
        
        
        res = 0 

        for _ in range(32): 
            
            res = res << 1 # shift left first, make space

            add = n & 1 # 1010 and 0001 = 0, gets the last digit !!!
            n  = n >> 1 
            res = res | add # 1010 and 0001 = 1011; takes all the 1s basically, damn
        
        
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

