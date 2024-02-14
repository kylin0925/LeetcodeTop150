# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        from queue import  PriorityQueue
        q = PriorityQueue()
        for head in lists:
            t = head
            while t != None:
                q.put(t.val)
                t = t.next
        root = None
        tmp = None
        while q.empty() == False:
            n = q.get()
            if root == None:
                root = ListNode(n)
                tmp = root
            else:
                node = ListNode(n)
                tmp.next = node
                tmp=tmp.next
        return root
        