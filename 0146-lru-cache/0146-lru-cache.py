class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self, Node):
        prev, next = self.right.prev, self.right
        prev.next = Node
        next.prev = Node
        Node.next = next
        Node.prev = prev
        

    def remove(self, Node):
        prev = Node.prev
        next = Node.next

        prev.next = next
        next.prev = prev


    def get(self, key: int) -> int:
        if key in self.cache:
            #update to top
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        #cleaning older nodes beyond capacity
        if len(self.cache) > self.capacity:
            node_to_delete = self.left.next
            self.remove(node_to_delete)
            del self.cache[node_to_delete.key]
        

# class LinkedNode:
#     def __init__(self, key = -1, val = -1):
#         self.key = key
#         self.val = val
#         self.prev = None
#         self.next = None


# class LRUCache:

#     def __init__(self, capacity: int):

#         self.size = capacity;
#         self.cache = dict()
#         self.head = LinkedNode()
#         self.tail = LinkedNode()
#         self.head.next = self.tail
#         self.tail.prev = self.head


#     def get(self, key: int) -> int:
#         if key not in self.cache:
#             return -1
        
#         node = self.__evict(key)
#         self.__add_to_end(node)
#         return node.val

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             node = self.__delete(key)
        
#         node = LinkedNode(key, value)
#         self.cache[key] = node
#         self.__add_to_end(node)

#         if len(self.cache) > self.size:
#             self.__delete(self.head.next.key)

#     def __evict(self, key):
#         node = self.cache[key]
#         node.prev.next = node.next
#         node.next.prev = node.prev
#         node.next = None
#         node.prev = None
#         return node

#     def __add_to_end(self, node):
#         node.prev = self.tail.prev
#         node.next = self.tail

#         self.tail.prev.next = node
#         self.tail.prev = node
    
#     def __delete(self, key):
#         delete_node = self.__evict(key)

#         del delete_node
#         del self.cache[key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)