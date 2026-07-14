class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hm = {}

        # dummy head and dummy tail
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node) -> None:
        """Remove node from current position."""
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_tail(self, node: Node) -> None:
        """Add node right before tail = most recently used."""
        last_node = self.tail.prev

        last_node.next = node
        node.prev = last_node

        node.next = self.tail
        self.tail.prev = node

    def _move_to_tail(self, node: Node) -> None:
        """Mark node as recently used."""
        self._remove(node)
        self._add_to_tail(node)

    def get(self, key: int) -> int:
        if key not in self.hm:
            return -1

        node = self.hm[key]
        self._move_to_tail(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            node = self.hm[key]
            node.val = value
            self._move_to_tail(node)
            return

        new_node = Node(key, value)
        self.hm[key] = new_node
        self._add_to_tail(new_node)

        if len(self.hm) > self.cap:
            # remove least recently used node
            lru_node = self.head.next
            self._remove(lru_node)
            del self.hm[lru_node.key]