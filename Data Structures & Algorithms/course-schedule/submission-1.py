from collections import defaultdict
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            adj_list[b].append(a)
            indegree[a] += 1
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        taken = 0
        while queue:
            course = queue.popleft()
            taken += 1
            for neighbor in adj_list[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return taken == numCourses

