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