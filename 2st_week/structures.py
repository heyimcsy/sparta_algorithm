# 연결 리스트를 만들어보자.
# 상자와 링크가 합쳐진 노드들이 만들어 져야 한다.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val   # 깂, 상자
        self.next = next  # 링크


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val, None)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = ListNode(val, None)

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if self.top is None:
            return None

        node = self.top
        self.top = self.top.next

        return node.val

    def is_empty(self):
        return self.top is None

class Queue:
    def __init__(self):
        self.front = None

    def push(self, value):
        if not self.front:
            self.front = Node(value)
            return

        node = self.front
        while node.next:
            node = node.next
        node.next = Node(value)

    def pop(self):
        if not self.front:
            return None

        node = self.front
        self.front = self.front.next
        return node.val

    def is_empty(self):
        return self.front is None

class HashNode:
    def __init__(self, key, val, next):
        self.key = key
        self.val = val
        self.next = next

class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def _hash_function(self, key):
        return key % self.size

    def put(self, key, val):
        idx = self._hash_function(key)

        if self.table[idx] is None:
            self.table[idx] = HashNode(key, val, None)
        else:
            node = self.table[idx]
            while node.next is not None:
                node = node.next
            node.next = HashNode(key, val, None)

    def get(self, key):
        idx = self._hash_function(key)
        node = self.table[idx]

        while node is not None:
            if node.key == key:
                return node.val
            node = node.next

        return -1

    def remove(self, key):
        idx = self._hash_function(key)
        node = self.table[idx]
        prev_node = None

        while node is not None:
            if node.key == key:
                if prev_node is not None:
                    prev_node.next = node.next
                else:
                    self.table[idx] = node.next
            prev_node = node
            node = node.next


class BinaryMaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, val):
        self.items.append(val)

        cur = len(self.items) - 1
        parent = cur // 2

        while parent > 0:
            if self.items[cur] > self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]

            cur = parent
            parent = cur //2

    def extract(self):
        if len(self.items) < 2:
            return None

        root = self.items[1]
        self.items[1], self.items[-1] =self.items[-1], self.items[1]
        self.items.pop()

        self._percolate_down(1)
        return root

    def _percolate_down(self, cur):
        largest = cur
        left = 2 * cur
        right = 2 * cur + 1

        if left < len(self.items) and self.items[left] > self.items[largest]:
            largest = left
        if right < len(self.items) and self.items[right] > self.items[largest]:
            largest = right
        if largest != cur:
            self.items[largest], self.items[cur] = self.items[cur], self.items[largest]
            self._percolate_down(largest)

