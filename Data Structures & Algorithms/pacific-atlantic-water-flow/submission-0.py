class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def valid(x, y):
            return 0 <= x < m and 0 <= y < n
        
        def dfs(x, y, seen):
            if (x, y) in seen:
                return
            seen.add((x, y))
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if valid(nx, ny) and heights[nx][ny] >= heights[x][y]:
                    dfs(nx, ny, seen)

        m = len(heights)
        n = len(heights[0])
        pacific = set()
        atlantic = set()
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for r in range(m):
            dfs(r, 0, pacific)
            dfs(r, n - 1, atlantic)
        for c in range(n):
            dfs(0, c, pacific)
            dfs(m - 1, c, atlantic)

        return list(list(pacific & atlantic))

        

        
            