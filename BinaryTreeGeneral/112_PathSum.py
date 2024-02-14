# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        self.flag = False
        self.count = 0
        if root == None:
            return False
        def dfs(r,sum,target):
            #print(sum)
            
            if r.left == None and r.right==None:
                if sum + r.val == target:
                    self.flag = True
            else:                
                if self.flag == False and r.left!=None: dfs(r.left,sum+r.val,target)
                if self.flag == False and r.right!=None: dfs(r.right,sum+r.val,target)
        dfs(root,0,sum)
        return self.flag
        