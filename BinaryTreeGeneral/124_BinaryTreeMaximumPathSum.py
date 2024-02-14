# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def maxPathSum(self, root: TreeNode) -> int:
        self.maxsum = -1000000000
        
        def dfs(root):
            if root == None: # return 0 when root is None 
                return 0     #   node
                             # null  null 
            l = dfs(root.left)
            r = dfs(root.right)
            
            #tmp = max(l,r)
            #print(tmp)
            tmp = root.val + r            
            tmp = max( tmp,root.val + l)            
            tmp = max( tmp,root.val + r+l)            
            self.maxsum = max(self.maxsum,tmp)
            self.maxsum = max(self.maxsum,root.val) # max val: root + l , root+r ,root+r+l
            
            tmp = max( root.val + l,root.val + r) # choice one path
            tmp = max(tmp,root.val)               # cmp with parent nod val
        
            return tmp
            
        tmp = dfs(root)
        
        return self.maxsum
        