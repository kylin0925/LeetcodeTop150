"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node == None:
            return None
        vis={}
        nodemap={}
        q = deque()
        q.append(node)
        while len(q) > 0:
            node = q.popleft()
            if node.val not in vis:
                vis[node.val]=1
                if node.val not in nodemap:                    
                    newnode = Node(node.val)                
                    nodemap[newnode.val] = newnode
                else:                    
                    newnode = nodemap[node.val]
                    
                for ne in node.neighbors:
                    if ne.val in nodemap:
                        tmp = nodemap[ne.val]                                               
                    else:
                        #print("new ne",ne.val)
                        tmp = Node(ne.val)
                        nodemap[tmp.val] = tmp
                        
                    newnode.neighbors.append(tmp)
                    q.append(ne)  
                
                
        #print(nodemap[1].neighbors)   
        return nodemap[1]
                
        