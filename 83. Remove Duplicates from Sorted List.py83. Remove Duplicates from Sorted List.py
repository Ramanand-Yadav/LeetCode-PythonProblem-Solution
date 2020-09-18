# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        curr = head
        if curr.next == None:
            return head
        while curr:
            dat = curr.val
            prev = curr
            curr1 = curr.next
            while curr1:
                if dat == curr1.val:
                    prev.next = curr1.next
                    curr1 = curr1.next
                else:
                    prev = curr1
                    curr1 = curr1.next
            curr = curr.next
        return head
