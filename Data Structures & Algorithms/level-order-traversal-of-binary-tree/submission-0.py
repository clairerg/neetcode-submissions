from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(node):
            if not node:
                return
            
            queue = deque([node])
            ans = []
            while queue:
                row = len(queue)
                row_arr = []
                for _ in range(row):
                    node_popped = queue.popleft()
                    row_arr.append(node_popped.val)
                    if node_popped.left:
                        queue.append(node_popped.left)
                    if node_popped.right:
                        queue.append(node_popped.right)
                ans.append(row_arr)
            return ans
        if not root:
            return []
        return bfs(root)
