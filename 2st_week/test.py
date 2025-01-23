from structures import LinkedList, Stack
from prac import isPalindrome

l1 = LinkedList()
for num in [1, 2, 2, 1]:
    l1.append(num)

l2 = LinkedList()
for num in [1, 2]:
    l2.append(num)


assert isPalindrome(l1)
assert not isPalindrome(l2)


def test_stack():
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    assert stack.pop() == 5
    assert stack.pop() == 4
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() is None
    assert stack.is_empty()