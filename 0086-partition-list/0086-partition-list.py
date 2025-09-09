# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        small=ListNode(0)
        high=ListNode(0)

        sh=small
        lh=high

        while(head):
            if(head.val<x):
                sh.next=head
                sh=sh.next

            else:
                lh.next=head
                lh=lh.next

            head=head.next

        sh.next=high.next
        lh.next=None

        return small.next