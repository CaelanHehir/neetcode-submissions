# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        encountered = []
        if head and not head.next:
            return head
        while head and head.next:
            encountered.append(head)
            head = head.next
        if not encountered:
            return None
        new_head = ListNode(head.val)
        prev = new_head
        while encountered:
            current = ListNode(encountered.pop().val)
            prev.next = current
            prev = current

        return new_head
