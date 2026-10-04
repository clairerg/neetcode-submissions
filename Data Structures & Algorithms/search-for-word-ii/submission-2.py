class TrieNode():
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n

        def backtrack(x, y, seen, curr, path):
            letter = board[x][y]
            if letter not in curr.children:
                return
            
            curr = curr.children[letter]
            path = path + letter

            if curr.end_of_word == True:
                ans.append(path)
                curr.end_of_word = False

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if valid(nx, ny) and (nx, ny) not in seen:
                    if board[nx][ny] in curr.children:
                        seen.add((nx, ny))
                        backtrack(nx, ny, seen, curr, path)
                        seen.remove((nx, ny))

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        m = len(board)
        n = len(board[0])
        root = TrieNode()
        ans = []
        for word in words:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.end_of_word = True
        
        for x in range(m):
            for y in range(n):
                if board[x][y] in root.children:
                    backtrack(x, y, {(x, y)}, root, "")
        
        return ans

            



        