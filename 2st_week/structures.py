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

ln = LinkedList()

ln.append(3)
ln.append(5)
ln.append(7)

print(ln)