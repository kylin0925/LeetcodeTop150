# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        
        if root == None:
            return root
        
        q = deque([root])
        cnt = 1
        ans = [root.val]
        while len(q) > 0:
            
            tmpcnt = 0
            for i in range(cnt):
                n = q.popleft()
                if n.left!=None:
                    tmpcnt+=1
                    q.append(n.left)
                if n.right!=None:
                    tmpcnt+=1
                    q.append(n.right)
                    
            if tmpcnt > 0:
                ans.append(q[tmpcnt-1].val)            
                cnt=tmpcnt
        return ans
    
    
