class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def valid(x, y):
            return 0 <= x < m and 0 <= y < n
        def backtrack(row, col, seen, path):
            if path == list(word):
                return True

            for dx, dy in directions:
                nx, ny = row + dx, col + dy
                if valid(nx, ny) and (nx, ny) not in seen and board[nx][ny] == word[len(path)]:
                    seen.add((nx, ny))
                    path.append(board[nx][ny])
                    if backtrack(nx, ny, seen, path):
                        return True
                    path.pop()
                    seen.remove((nx, ny))

            return False

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(board)
        n = len(board[0])
        seen = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    seen.add((i, j))
                    if backtrack(i, j, seen, [word[0]]):
                        return True
                    seen.remove((i, j))
        return False
        