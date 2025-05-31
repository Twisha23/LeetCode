class Solution:
    def reverseList(self, head):
        prev=None
        current=head
        
        while current:
            after=current.next
            current.next=prev
            prev=current
            current=after
        return prev
        
        
        
    