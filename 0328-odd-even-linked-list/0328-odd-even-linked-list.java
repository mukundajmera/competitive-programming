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
    public ListNode oddEvenList(ListNode head) {
        if(head == null){
            return head;
        }
        ListNode oddHead = head, evenHead = head.next;
        ListNode odd = oddHead, even = evenHead;
        ListNode prev = odd;
        while(odd != null && even != null){
            if(odd.next != null){
                odd.next = odd.next.next;
            }

            if(even.next != null){
                even.next = even.next.next;
            }

            prev = odd;
            odd = odd.next;
            even = even.next;
        }
        //interweave and join
        if(odd == null){
            prev.next = evenHead;
        }else{
            odd.next = evenHead;
        }
        return oddHead;

    }
}
