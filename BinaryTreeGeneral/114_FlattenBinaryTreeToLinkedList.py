# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        arr = []
        
        def preorder(root):
            if root !=None:
                arr.append(root.val)
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        tmp = root
        
        for i in range(1,len(arr)):
            tmp.right = TreeNode(arr[i])
            tmp.left=None
            tmp=tmp.right
        tmp=None
        return root