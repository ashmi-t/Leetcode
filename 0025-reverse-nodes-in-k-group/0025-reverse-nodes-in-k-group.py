# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        mover = head

        length = 0
        while mover:
            mover = mover.next
            length += 1

        def reverseLinkedList(head, remaining):
            if remaining - k < 0:
                return head
            
            prev = None
            start = head
            curr = start
            next = curr.next

            elems = 0

            while curr:
                curr.next = prev
                prev = curr
                curr = next
                next = next.next if next else None
                elems += 1

                if elems % k == 0:
                    start.next = reverseLinkedList(curr, remaining - k)
                    break
            
            return prev

        return reverseLinkedList(head, length)