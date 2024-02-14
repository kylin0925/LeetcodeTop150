# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.data = []
        def dfs(n):
            if n!=None:
                dfs(n.left)
                self.data.append(n.val)
                dfs(n.right)
        dfs(root)
        #print(self.data)
        diff = self.data[-1] - self.data[0]
        
        for i in range(1,len(self.data)):
            diff = min(diff, self.data[i] - self.data[i-1])
        return diff