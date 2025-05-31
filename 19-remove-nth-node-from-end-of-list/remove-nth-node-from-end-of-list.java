/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {

    public ListNode removeNthFromEnd(ListNode head, int n) {
        if(n == 1 && head.next == null){
            return null;
        }
        int level = levelNext(head, head.next, n);
        if(n == level){
            head = head.next;
        }
        return head;
    }

    public int levelNext(ListNode parent, ListNode child, int n){
        if(parent== null){
            return 0;
        }

        if(child == null){
            return 1;
        }

        int level = levelNext(child, child.next, n);
        if(n == level){
            parent.next = child.next;
        }
        return level+1;

    }
}