# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        '''
         [-10,-3,0,5]
           
         middle = (l + u) //2 
         newnode(nums[middle])
         build(l,middle-1)
         build(middle+1,u)
         
        '''
        def buildBST(parent,l,r,nums):
            if l >= r:
                return parent
            
            middle = (l + r) >> 1
            val = nums[middle]
            parent = TreeNode()
            parent.val = val
            parent.left = buildBST(parent.left, l        ,middle, nums)
            parent.right= buildBST(parent.right, middle+1,r     , nums)
            return parent
        root = None
        root =buildBST(root,0,len(nums),nums)
        return root
    