# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        self.maxdepth = 0
        def dfs(root,n):
            #print(n)
            if root == None:
                if self.maxdepth < n:
                    self.maxdepth = n
                return
            dfs(root.left,n+1)
            dfs(root.right,n+1)
        dfs(root,0)            
        return self.maxdepth