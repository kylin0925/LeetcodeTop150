# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        stack = [root]
        anslist = []
        while len(stack) >0:
            tmplist= []
            
            while len(stack) >0:
                tmp = stack.pop()
                tmplist.append(tmp)
            
            avg = 0
            for n in tmplist:
                avg+=n.val
                if n.left!=None:                    
                    stack.append(n.left)
                if n.right!=None:
                    stack.append(n.right)
                    
            avg = avg/len(tmplist)
            anslist.append(avg)
        return anslist
            