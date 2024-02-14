# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        self.list_arr = []
        def build_list(head):
            tmp = head
            n = 0
            while tmp != None:
                self.list_arr.append(tmp)
                n += 1
                tmp = tmp.next
            return n
        
        def rev(start, end):
            print(start, end)
            while start < end:
                self.list_arr[start], self.list_arr[end] = self.list_arr[end], self.list_arr[start]
                start += 1
                end -=1
                print(start, end)      

        n = build_list(head)

        i = 0
        pre = None
        while i + k -1 < n:            
            rev(i, i+k-1)
            i+=k

        for i in range(1, n):
                self.list_arr[i-1].next = self.list_arr[i]
        
        self.list_arr[-1].next = None
        #print(self.list_arr)
        #print(self.list_arr[0])
        return self.list_arr[0]