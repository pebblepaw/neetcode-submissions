class Solution:
    def countBits(self, n: int) -> List[int]:

        output = [0] * (n+1)

        for i in range(0,n+1):
            
            # print(f'at {i}')
            num = i
    
            while num: 
                output[i] += (num%2)
                # print(output)
                num = num >> 1

        return output 
            
