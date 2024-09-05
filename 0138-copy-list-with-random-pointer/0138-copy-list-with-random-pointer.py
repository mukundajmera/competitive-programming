class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        map = {}
        curr = head
        while curr:
            map[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            #setting next value
            map[curr].next = map.get(curr.next)
            map[curr].random = map.get(curr.random)
            curr = curr.next
        
        return map[head]
 
    # def __init__(self):
    #     # Creating a visited dictionary to hold old node reference as "key" and new node reference as the "value"
    #     self.visited = {}

    # def getClonedNode(self, node):
    #     if node:
    #         if node in self.visited:
    #             return self.visited[node]
    #         else:
    #             self.visited[node] = Node(node.val, None, None)
    #             return self.visited[node]
    #     return None

    # def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":

    #     if not head:
    #         return head

    #     old_node = head
    #     new_node = Node(old_node.val, None, None)
    #     self.visited[old_node] = new_node

    #     while old_node != None:

    #         # Get the clones of the nodes referenced by random and next pointers.
    #         new_node.random = self.getClonedNode(old_node.random)
    #         new_node.next = self.getClonedNode(old_node.next)
    #         old_node = old_node.next
    #         new_node = new_node.next

    #     return self.visited[head]