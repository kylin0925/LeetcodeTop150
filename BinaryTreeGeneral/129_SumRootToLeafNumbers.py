# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.acc = 0
        def dfs(n, num):
            if n!=None:
                if n.left == None and n.right==None:
                    num = num *10 +n.val        
                    self.acc += num
                    return
                else:
                    num = num *10 +n.val
                    dfs(n.left, num)
                    dfs(n.right, num)
        dfs(root, 0)
        return self.acc
        