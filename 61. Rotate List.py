# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        old_tail = head
        temp = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n = n+1
        k = k%n
        old_tail.next = head
        for i in range(n-k-1):
            temp = temp.next
        answer = temp.next
        temp.next = None
        return answer
