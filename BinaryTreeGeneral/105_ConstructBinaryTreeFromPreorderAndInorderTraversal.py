# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        tbl = {}
        def build(pre_idx,start,end):
            # if pre_idx >= len(preorder):
            #     return None
            if start == end:
                return None

            #print(pre_idx,preorder[pre_idx],"start",start,"end",end)
            tn = TreeNode(preorder[pre_idx])

            for i in range(start,end):
                if preorder[pre_idx] == inorder[i]:

                    break

            tn.left = build(pre_idx + 1 ,start,i)
            tn.right = build(pre_idx + i -start + 1,i+1,end)

            return tn


        root = build(0,0,len(preorder))

        return root