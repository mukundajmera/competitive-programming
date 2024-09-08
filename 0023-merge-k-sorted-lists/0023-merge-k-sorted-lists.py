# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            temp = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i + 1 < len(lists) else None
                temp.append(self.merge_lists(l1, l2))
            lists = temp
        
        return lists[0]
    
    def merge_lists(self, l1, l2):
        node = ListNode()
        ans = node
        
        while l1 and l2:
            if l1.val > l2.val:
                node.next = l2
                l2 = l2.next
            else:
                node.next = l1
                l1 = l1.next
            node = node.next
        
        if l1:
            node.next = l1
        else:
            node.next = l2
        
        return ans.next
        # #using heap appraoch
        # heap = []
        # for list_idx in lists:
        #     curr = list_idx
        #     while curr:
        #         heap.append(curr.val)
        #         curr = curr.next
        # heapq.heapify(heap)

        # dummy = ListNode(0)
        # prev = dummy
        # while heap:
        #     prev.next = ListNode(heapq.heappop(heap))
        #     prev = prev.next
        
        # return dummy.next