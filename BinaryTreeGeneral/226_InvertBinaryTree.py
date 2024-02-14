# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invert(self,node):
        if node != None:
		    tmp = node.left
		    node.left = node.right
		    node.right = tmp
		    self.invert(node.left)
		    self.invert(node.right)
		    
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.invert(root)
        return root