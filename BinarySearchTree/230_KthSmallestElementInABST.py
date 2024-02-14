# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = 0
        self.ans = 0
        def inorder(n):
            if n!=None:
                inorder(n.left)
                self.cnt+=1
                if self.cnt == k:
                    self.ans=n.val
                inorder(n.right)
        inorder(root)
        return self.ans