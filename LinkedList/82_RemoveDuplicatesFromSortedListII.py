# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num_cnt = {}
        def cntlist(head):
            tmp = head
            while tmp!=None:
                if tmp.val not in num_cnt:
                    num_cnt[tmp.val] =1
                else:
                    num_cnt[tmp.val] +=1
                tmp = tmp.next
                
        cntlist(head)  
        #print(num_cnt)
        next_node = head
        ph = ListNode()
        while next_node !=None:
            if num_cnt[next_node.val]>1:
                while next_node !=None:
                    if num_cnt[next_node.val]==1:
                        break
                    next_node=next_node.next
                    
            #print(next_node)
            if ph.next == None:
                head = next_node
            ph.next = next_node
            
            ph = ph.next
            if next_node!=None:
                next_node = next_node.next
            
        return head
            
                
        