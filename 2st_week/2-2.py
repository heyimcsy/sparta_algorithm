def postfixNotation(input_text):
    stack = []
    text = input_text.split()
    for t in text:
        if '+' == t:
            if len(stack) > 1:
                result = int(stack[0]) + int(stack[1])
                stack.clear()
                stack.append(result)
        elif '-' == t:
            if len(stack) > 1:
                result = int(stack[0]) - int(stack[1])
                stack.clear()
                stack.append(result)
        elif '*' == t:
            if len(stack) > 1:
                result = int(stack[0]) * int(stack[1])
                stack.clear()
                stack.append(result)
        elif '/' == t:
            if len(stack) > 1:
                result = int(stack[0]) / int(stack[1])
                stack.clear()
                stack.append(result)
        else:
            stack.append(t)
    return stack[0]

print(postfixNotation('2 3 + 5 *'))
print(postfixNotation('4 2 / 3 - 2 *'))