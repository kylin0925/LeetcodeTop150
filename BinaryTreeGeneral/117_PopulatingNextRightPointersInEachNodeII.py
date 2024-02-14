"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return root
        q = deque([root])
        cnt = 1
        tmpcnt = 0
        while len(q) > 0:
            tmpcnt=0
            for i in range(cnt):
                n = q.popleft()
                if n.left!=None:
                    tmpcnt+=1
                    q.append(n.left)
                if n .right!=None:
                    tmpcnt+=1
                    q.append(n.right)
            #print(tmpcnt)
            for i in range(1,tmpcnt):
                q[i-1].next = q[i]
            cnt = tmpcnt
        return root