class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        num_rows, num_cols = len(grid), len(grid[0])
        directions = [[1,0], [0,1],[-1,0],[0,-1]]
        islands = 0

        def dfs(r,c): 

            if r < 0 or c < 0 or r >= num_rows or c >= num_cols or grid[r][c] == "0": 
                return 
            
            # set as 0 
            grid[r][c] = "0"
            # visit all in the surroundings, if also 1, set as 0
            for dr, dc in directions: 
                dfs(r + dr, c + dc)
            return 

        for r in range(num_rows): 
            for c in range(num_cols): 
                if grid[r][c] == "1": 
                    dfs(r, c)
                    islands += 1
        
        return islands
        