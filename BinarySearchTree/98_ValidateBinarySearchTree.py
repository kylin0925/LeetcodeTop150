# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.isBal = True
        
        def dfs(n):
            #print(n)
            if n==None:
                return None
            if n.left == None and n.right == None:
                return (n.val, n.val)
            
            l = dfs(n.left)
            r = dfs(n.right)
            #print(n.val, "left",l,"right",r)
            maxval = n.val
            minval = n.val
            if l !=None:
                if n.val <= l[1]:
                    self.isBal = False
                minval = min(minval,l[0],l[1])
                maxval = max(maxval,l[0],l[1])
            if r !=None:
                if n.val >= r[0]:
                    self.isBal = False
                minval = min(minval,r[0],r[1])
                maxval = max(maxval,r[0],r[1])
            #print(minval, maxval)
            return (minval, maxval)
           
            
        dfs(root)
        return self.isBal
            
        