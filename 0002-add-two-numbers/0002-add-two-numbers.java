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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        if(l1 == null){
            return l1;
        }
        if(l2 == null){
            return l2;
        }
        ListNode p1 = l1, p2 = l2;
        ListNode dummy = new ListNode();
        ListNode current = dummy;
        while(p1 != null && p2 != null){
            int total = p1.val + p2.val + carry;
            carry = total / 10;
            total %= 10;
            current.next = new ListNode(total);
            current = current.next;
            p1 = p1.next;
            p2 = p2.next;
        }

        ListNode rest = p1;
        if(p1 == null){
            rest = p2;
        }
        while(rest != null){
            int total = carry + rest.val;
            carry = total / 10;
            current.next = new ListNode(total%10);
            current = current.next;
            rest = rest.next;            
        }

        if(carry > 0){
            current.next = new ListNode(carry);
        }

        return dummy.next;

    }
}