# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head

        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next


        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)

        dummy = ListNode()
        curr = dummy

        while left and right:
            if left.val<=right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
        
            curr = curr.next
        
        curr.next = left if left else right
        return dummy.next
