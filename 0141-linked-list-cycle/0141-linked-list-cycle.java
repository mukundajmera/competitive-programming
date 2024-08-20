/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        if(head == null){
            return false;
        }
        ListNode slow = head, fast = head.next;
        while(slow != fast){
            slow = slow.next;
            if(fast != null && fast.next != null){
                fast = fast.next.next;
            }else{
                return false;
            }
        }
        return true;
    }
}