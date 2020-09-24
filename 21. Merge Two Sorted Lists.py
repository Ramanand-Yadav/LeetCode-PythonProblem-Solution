# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1
        p = l1 
        q  = l2
        if p.val>=q.val:
            s = q
            q = q.next
        else:
            s = p
            p = p.next
        new_head = s
        while p and q:
            if p.val>=q.val:
                s.next = q
                s = q
                q = q.next
            else:
                s.next = p
                s = p
                p = p.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        return new_head
        
