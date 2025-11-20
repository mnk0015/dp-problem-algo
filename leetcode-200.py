from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def bfs(i, j):
            q = deque()
            q.append((i, j))
            grid[i][j] = '0'   # mark as visited immediately

            while q:
                r, c = q.popleft()

                # 4 directions
                for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                    nr, nc = r + dr, c + dc

                    # If inside grid and it's land
                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == '1':
                        grid[nr][nc] = '0'   # mark visited
                        q.append((nr, nc))

        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    bfs(i, j)

        return count