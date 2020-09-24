# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        s,p = 0,0
        m,n = headA,headB
        while m:
            s = s+1
            m = m.next
        while n:
            p = p+1
            n = n.next
        m,n = headA,headB
        while s>p:
            m = m.next
            s = s-1
        while p>s:
            n = n.next
            p = p-1
        while n and m:
            if n is m:
                return n 
            m,n = m.next,n.next
        return None   
                
