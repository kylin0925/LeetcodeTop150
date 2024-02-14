# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        tmp = head
        while tmp !=None:
            vals.append(tmp.val)
            tmp = tmp.next
        vals.sort()
        tmp = head
        i = 0
        while tmp!=None:
            tmp.val = vals[i]
            tmp = tmp.next
            i+=1
        return head
        