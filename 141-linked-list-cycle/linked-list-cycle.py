# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: # if head is None, return false because there are no linked list, hence, no cycles.
            return False

        slow = head
        fast = head
        while fast and fast.next: # checks if fast is not None and fast.next is not none either, otherwise stop
            slow = slow.next
            fast = fast.next.next
            if slow == fast: # tortoise and hare algo will eventually collide if there is a cycle
                return True

        return False # if the loop reach a null, then there is no cycle (normal ending)