from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):        
            seen.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)
        
        adj_list = defaultdict(list)
        seen = set()
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        components = 0
        for node in range(n):
            if node not in seen:
                dfs(node)
                components += 1
        return components
        