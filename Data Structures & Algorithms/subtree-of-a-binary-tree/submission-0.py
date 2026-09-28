# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 and node2:
                return False
            if node1 and not node2:
                return False
            if node1.val != node2.val:
             return False
            
            if dfs(node1.left, node2.left) and dfs(node1.right, node2.right):
                return True
            else:
                return False
        
        def search(node):
            if not node:
                return False
            if dfs(node, subRoot):
                return True
            
            return search(node.left) or search(node.right)
        
        return search(root)
            
        
        
        