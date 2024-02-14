# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        q = deque([(root,0)])
        tmp = [(root,0)]
        ans = []
        level = -1
        while len(q)>0:
            n = q.popleft()
            if n[1]!=level:
                
                tmp2=[]
                for it in tmp:
                    tmp2.append(it[0].val)
                ans.append(tmp2)
                
                level = n[1]
                tmp=[]
                
            if n[0].left!=None:
                tmp.append((n[0].left, level+1))
                q.append((n[0].left, level+1))
            if n[0].right!=None:
                tmp.append((n[0].right, level+1))
                q.append((n[0].right, level+1))
            #print(q)
        return ans