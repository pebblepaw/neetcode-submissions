class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # bfs solution 
        from collections import deque

        if not grid: 
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        visited = set()
        islands = 0 


        def bfs(r,c): 
            visited.add((r,c))
            q = deque()
            q.append((r,c))
            
            while q: 
                r, c = q.popleft()
                for dr, dc in directions: 
                    _r, _c = r + dr, c + dc
                    if (
                    _r in range(ROWS) 
                    and _c in range(COLS) 
                    and grid[_r][_c] == "1" 
                    and (_r,_c) not in visited
                    ):
                        q.append((_r,_c))
                        visited.add((_r,_c))
            return 

        for r in range(ROWS): 
            for c in range(COLS): 
                if grid[r][c] == "1" and (r,c) not in visited: 
                    bfs(r,c)
                    islands+=1
        
        return islands







        # # dfs solution 
        # num_rows, num_cols = len(grid), len(grid[0])
        # directions = [[1,0], [0,1],[-1,0],[0,-1]]
        # islands = 0

        # def dfs(r,c): 

        #     if r < 0 or c < 0 or r >= num_rows or c >= num_cols or grid[r][c] == "0": 
        #         return 
            
        #     # set as 0 
        #     grid[r][c] = "0"
        #     # visit all in the surroundings, if also 1, set as 0
        #     for dr, dc in directions: 
        #         dfs(r + dr, c + dc)
        #     return 

        # for r in range(num_rows): 
        #     for c in range(num_cols): 
        #         if grid[r][c] == "1": 
        #             dfs(r, c)
        #             islands += 1
        
        # return islands
        