# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lh = ListNode()
        rh = ListNode()
        ltail = lh
        rtail = rh
        tmp = head
        while tmp !=None:
            #print(tmp.val)
            #print(lh)
            #print(rh)
            if tmp.val < x:
                tn = ListNode()
                tn.val = tmp.val
                
                ltail.next = tn                
                ltail = ltail.next
            else:
                tn = ListNode()
                tn.val = tmp.val
                
                rtail.next = tn                
                rtail = rtail.next
            tmp=tmp.next
        
        #print(lh)
        #print(rh)
        ltail.next = rh.next
        return lh.next
        