class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        minHeap = [[grid[0][0],0,0]]
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        visited.add((0,0))
        while minHeap:
            height, r,c = heapq.heappop(minHeap)
            if r == n-1 and c == n-1:
                return height
            for dx,dy in dirs:
                neiR, neiC = r + dx, c + dy
                if (neiR < 0 or neiC < 0 or neiR == n or neiC == n 
                or (neiR,neiC) in visited):
                    continue
                visited.add((neiR,neiC))
                heapq.heappush(minHeap,[max(height,grid[neiR][neiC]),neiR,neiC])


        