class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        if not grid: 
            return 0 

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS,COLS = len(grid), len(grid[0])
        max_island = 0 

        def dfs(r,c): 
            island_size = 1
            grid[r][c] = 0

            for dr, dc in directions: 
                _r, _c = r + dr, c + dc

                if (
                    _r in range(ROWS) and 
                    _c in range(COLS) and 
                    grid[_r][_c] == 1
                ): 
                    grid[_r][_c] = 0
                    island_size += dfs(_r,_c)
            
            return island_size 

        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == 1: 
                    this_island = dfs(r, c)
                    max_island = max(max_island, this_island)
        
        return max_island
        