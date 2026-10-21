from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def dfs(node, parent):
            print(seen)
            seen.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in seen:
                    if not dfs(neighbor, node):
                        return False
                elif neighbor != parent:
                    return False
            return True
        
        adj_list = defaultdict(list)
        seen = set()
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
        if not dfs(0, None):
            return False
        if len(seen) != n:
            return False
        return True

        
