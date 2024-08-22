class LinkedNode:
    def __init__(self, key = -1, val = -1):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):

        self.size = capacity;
        self.cache = dict()
        self.head = LinkedNode()
        self.tail = LinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.__evict(key)
        self.__add_to_end(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.__delete(key)
        
        node = LinkedNode(key, value)
        self.cache[key] = node
        self.__add_to_end(node)

        if len(self.cache) > self.size:
            self.__delete(self.head.next.key)

    def __evict(self, key):
        node = self.cache[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        return node

    def __add_to_end(self, node):
        node.prev = self.tail.prev
        node.next = self.tail

        self.tail.prev.next = node
        self.tail.prev = node
    
    def __delete(self, key):
        delete_node = self.__evict(key)

        del delete_node
        del self.cache[key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)