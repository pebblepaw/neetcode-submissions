class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        #because we're using 0 index
        # let's say there are 9 rows, r = 8 
        l, r = 0, len(matrix)-1

        while l < r: 
            
            # for the first row, this prints from 0 to (8-0) = 7; 
            # because we don't need to rotate the rightmost one, it's alr part of 
            # the initial rotation
            for i in range(r-l): 

                top, bottom = l, r 
            
                # keep this first
                topleft = matrix[top][l+i]

                # go in counter-clockwise direction
                matrix[top][l+i] = matrix[bottom-i][l]
                
                matrix[bottom-i][l] = matrix[bottom][r-i]

                matrix[bottom][r-i] = matrix[top+i][r]

                matrix[top+i][r] = topleft

            l += 1
            r -= 1
                