# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        import sys
        if not head:
            return head

        node = ListNode(-sys.maxsize - 1)  # dummy node
        node.next = head
        head = node

        prev = head
        current = head.next

        while current:
            if current.val == val:
                prev.next = current.next  # skip current node
                current = current.next    # move to next
            else:
                prev = current
                current = current.next
        
        return head.next