# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def cntLen(n):
            l = 0
            while n!=None:
                l+=1
                n=n.next
            return l
        def addto(l,by):
            ans = l
            c =0
            back = l
            while by!=None:
                tmp = l.val + by.val +c
                l.val = tmp % 10
                c = tmp //10
                back = l
                l = l.next
                by = by.next
                
            while l!=None and c > 0:
                tmp = l.val + c
                l.val = tmp % 10
                c = tmp //10
                back = l
                l = l.next
                
            if c > 0:
                newnode = ListNode(c)
                back.next = newnode
                
            return ans
        if cntLen(l1) > cntLen(l2):
            return addto(l1,l2)
        else:
            return addto(l2,l1)
        