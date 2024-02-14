# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.pathp = []
        self.pathq = []
        tpath = []
        def dfs(n,tpath):
            if n!=None:
                tpath.append(n.val)
                
                if n.val == p.val:
                    self.pathp = tpath[:]
                    #print(self.pathp, self.pathq)            
                if n.val == q.val:
                    self.pathq = tpath[:]                    
                    #print(self.pathp, self.pathq)            
                    
                
                dfs(n.left,tpath)
                dfs(n.right,tpath)
                tpath.pop()
        dfs(root,tpath)
        #print("->",self.pathp, self.pathq)
        i = 0
        while i < len(self.pathp) and i < len(self.pathq):
            if self.pathq[i]!=self.pathp[i]:
                break
            i+=1
        return TreeNode(self.pathq[i-1])