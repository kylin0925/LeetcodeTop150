# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        i=1
        curr = head
        pre = ListNode()
        pre.next = curr
        stack = []
        while curr!=None:
            if i < left:
                pre=pre.next
                curr=curr.next
                pre.next=curr
            elif i>=left and i<=right:
                stack.append(curr)
                curr=curr.next           
            else:
                break
            i+=1
        node = stack.pop()
        if left == 1:
            head = node
        pre.next = node
        pre=pre.next
        
        while len(stack)>0:
            node = stack.pop()
            pre.next = node
            pre=pre.next
           
        pre.next = curr 
        return head