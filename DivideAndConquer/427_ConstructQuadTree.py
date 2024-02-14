"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def build(ux,uy,lx,ly):
            #print("e:",ux,uy,lx,ly)
            if lx - ux == 1 and ly - uy == 1:
                #print("leaf",ux,uy,grid[uy][ux])
                node = Node(grid[uy][ux],True,None,None,None,None)
                return node
            
            midx = (lx + ux)>>1
            midy = (ly + uy)>>1
            #print("mid",midx,midy)

            ulnode = build(ux,uy, midx, midy)           
            urnode = build(midx,uy, lx, midy)
            llnode = build(ux,midy, midx, ly)
            lrnode = build(midx,midy, lx, ly)
            
            if ulnode.val == urnode.val and urnode.val == llnode.val and llnode.val == lrnode.val and \
               ulnode.isLeaf and urnode.isLeaf and  llnode.isLeaf and lrnode.isLeaf:
                node = Node(ulnode.val,True,None,None,None,None)
                return node
            else:
                node = Node(ulnode.val,False,ulnode,urnode,llnode,lrnode)
                return node
        n = len(grid)
        node = build(0,0,n,n)
        #print(node.val, node.isLeaf,  node.topLeft, node.topRight,  node.bottomLeft,  node.bottomRight)
        return node
        