# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def inorder(self, node):
        if node == None:
            return
        self.inorder(node.left)
        self.data.append(node.val)
        self.cnt += 1 
        self.inorder(node.right)

    def __init__(self, root: Optional[TreeNode]):
        self.data = []
        self.idx = 0
        self.cnt = 0
        
        self.inorder(root)

    def next(self) -> int:
        n = self.data[self.idx]
        self.idx +=1
        return n

    def hasNext(self) -> bool:
        return self.idx < self.cnt


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()