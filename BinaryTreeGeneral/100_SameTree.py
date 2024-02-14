# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        def dfs(p,q):
            #print(p,q,p==q)
            #check p==q if p and q is None
            # check left not none 
            # dfs left none
            # check right none none 
            # dfs right
            
            if p == q :
                return True
            
            if (p ==None and q!=None) or (p!=None and q == None):
                return False
            
            if p.val != q.val:
                return False
                        
            return dfs(p.left,q.left) and dfs(p.right,q.right)
            
            
        return dfs(p,q)    