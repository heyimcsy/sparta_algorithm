from collections import deque

def isPalindrome(ln):
    arr = []
    head = ln.head

    if not head:
        return True

    node = head
    while node:
        arr.append(node.val)
        node = node.next
        print(arr)
    while len(arr) > 1:
        first = arr.pop(0)
        print(first)
        last = arr.pop()
        print(last)
        if first != last:
            return False

    return True

def test_problem_stack(s):
    stack = []
    pair = {
        ')':'(',
        '}':'{',
        ']':'['
    }
    for char in s:
        if char in '({[':
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            top = stack.pop()
            if pair[char] != top:
                return False
    return len(stack) == 0

def test_problem_queue(n):
    deq = deque([i for i in range(1, n + 1)])

    while len(deq) > 1:
        deq.popleft()
        front = deq.popleft()
        deq.append(front)
    return deq.pop()