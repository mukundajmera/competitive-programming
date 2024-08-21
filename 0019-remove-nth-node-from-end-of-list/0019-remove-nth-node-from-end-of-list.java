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
        //use prev pointer
        if(head == null){
            return head;
        }
        ListNode dummy = new ListNode(0, head);
        ListNode prev = dummy;
        while(n > 0){
            head = head.next;
            n--;
        }
        
        //move both pointer now
        while(head != null){
            head = head.next;
            prev = prev.next;
        }

        prev.next = prev.next.next;
        return dummy.next;
    }
}