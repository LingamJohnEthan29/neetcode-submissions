class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0
        visited = set()
        def dfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            area = 1
            while q:
                row,col = q.popleft()
                drs = [[1,0],[-1,0],[0,1],[0,-1]]
                for dx, dy in drs:
                    dr, dc = row + dx, col + dy
                    if (
                        dr in range(rows)
                        and dc in range(cols) 
                        and grid[dr][dc] == 1
                        and (dr,dc) not in visited
                    ):
                        area += 1
                        q.append((dr,dc))
                        visited.add((dr,dc))
            return area
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row,col) not in visited:
                    area = dfs(row,col)
                    maxArea = max(maxArea, area)
        return maxArea


        