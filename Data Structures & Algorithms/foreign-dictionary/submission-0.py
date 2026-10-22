from collections import defaultdict

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        def dfs(char):
            if char in path:
                return False
            if char in visited:
                return True
            path.add(char)
            for neighbor in graph[char]:
                if not dfs(neighbor):
                    return False
            visited.add(char)
            result.append(char)
            path.remove(char)
            return True

        graph = {}
        for word in words:
            for char in word:
                graph[char] = set()
        
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i+1]
            
            min_length = min(len(w1), len(w2))
            for j in range(min_length):
                if (len(w1) > len(w2) and w1[:len(w2)] == w2):
                    return ""
                if w1[j] != w2[j]:
                    graph[w1[j]].add(w2[j])
                    break
        path = set()
        visited = set()
        result = []

        for char in graph:
            if not dfs(char):
                return ""
        return "".join(reversed(result))
            
                    
            
                



        