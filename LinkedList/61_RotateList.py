# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        tmpHead = head
        newHead = head
        tail = None
        list_len = 0
        while tmpHead!=None:
            list_len+=1
            tail = tmpHead
            tmpHead = tmpHead.next
        
        #print(list_len)
        if list_len == 0 or k%list_len == 0:
            return head
        
        k = k % list_len
        headto = list_len - k
        #print(k)
        tmpHead = head
        for i in range(headto-1):
            tmpHead = tmpHead.next
        
        head = tmpHead.next
        tail.next = newHead
        tmpHead.next =None
        return head
        
        
        
        