from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:     
        def dfs(course):
            if course in path:
                return False
            if course in visited:
                return True

            path.add(course)
            for neighbor in graph[course]:
                if not dfs(neighbor):
                    return False
            visited.add(course)
            path.remove(course)
            return True

        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        visited = set()
        path = set()
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
        
        
       
 

        