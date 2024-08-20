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
    public boolean isPalindrome(ListNode head) {
        //go to middle and check with reverse list
        ListNode slow = head, fast = head.next;
        boolean isPal = true;
        if(head == null){
            return false;
        }
        //find middle node
        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        slow.next = reverse(slow.next);
        slow = slow.next;
        ListNode curr = head;


        while(slow != null){
            if(curr.val != slow.val){
                isPal = false;
                break;
            }
            curr = curr.next;
            slow = slow.next;
        }
        return isPal;
    }

    public ListNode reverse(ListNode head){
        if(head == null){
            return head;
        }
        ListNode curr = head, prev = null;
        while(curr != null){
            ListNode next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }
        return prev;
    }
}