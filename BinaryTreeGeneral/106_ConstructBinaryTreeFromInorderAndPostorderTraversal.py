# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        tbl = {}
        def build(pre_idx,start,end):  
            #print(pre_idx, start, end)
            if start == end:
                return None

            #print(pre_idx,postorder[pre_idx],"start",start,"end",end)
            tn = TreeNode(postorder[pre_idx])
            for i in range(start,end):
                if postorder[pre_idx] == inorder[i]:
                    break
            #print(i)
            tn.left = build(pre_idx - (end -i) ,start,i)
            tn.right = build(pre_idx - 1,i+1,end)

            return tn


        root = build(len(postorder)-1,0,len(postorder))

        return root