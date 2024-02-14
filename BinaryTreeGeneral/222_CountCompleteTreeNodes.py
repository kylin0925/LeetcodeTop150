# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.cnt = 0
        def dfs(n):
            if n !=None:
                self.cnt+=1
                dfs(n.left)
                dfs(n.right)
        dfs(root)
        return self.cnt
        