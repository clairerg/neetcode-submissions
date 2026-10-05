class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def valid(x, y):
            return 0 <= x < m and 0 <= y < n and grid[x][y] == '1'

        def dfs(x, y, seen):
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if valid(nx, ny) and (nx, ny) not in seen:
                    seen.add((nx, ny))
                    dfs(nx, ny, seen)

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(grid)
        n = len(grid[0])
        ans = 0
        seen = set()
        count = 0
        for i in range(m):
            for j in range(n):
                if valid(i, j) and (i, j) not in seen:
                    seen.add((i, j))
                    dfs(i, j, seen)
                    count += 1
        return count

        