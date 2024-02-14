# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None:
            return l2
        if l2 == None:
            return l1

        result = ListNode(0)
        head = result
        tail = head
        
        if l1.val > l2.val:
            result.val = l2.val
            l2 = l2.next
        else:
            result.val = l1.val 
            l1 = l1.next

        tail = result 
        print "head ",head.val
        while l1 != None and l2 !=None:
            tmp = None
            print l1.val,l2.val
            if l1.val < l2.val:
                tmp = ListNode(l1.val)
                l1 = l1.next
            else:
                tmp = ListNode(l2.val)
                l2 = l2.next

            tail.next = tmp
            tail = tail.next

        while l1!=None:
            tail.next = l1
            l1 = l1.next
            tail = tail.next
        while l2!=None:
            tail.next = l2
            l2 = l2.next
            tail = tail.next
        
        return head

        