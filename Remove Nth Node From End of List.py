# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        cur = head
        count = 0   
        while cur:
            count = count +1
            cur = cur.next
        if count == n:
            head = head.next
            return head
        pos = 1
        pre = head
        nex = pre.next
        while pos<count-n:
            pre = nex
            nex = nex.next
            pos += 1
        pre.next = nex.next
        nex.next = None
        return head
    
    
