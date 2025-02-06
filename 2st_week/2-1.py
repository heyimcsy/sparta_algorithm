def postfixNotation(input_text):
    stack = []
    text = input_text.split()
    for t in text:
        if '+' == t:
            if len(stack) > 1:
                b, a = stack.pop(), stack.pop()
                result = a + b
                stack.append(result)
        elif '-' == t:
            if len(stack) > 1:
                b, a = stack.pop(), stack.pop()
                result = a - b
                stack.append(result)
        elif '*' == t:
            if len(stack) > 1:
                b, a = stack.pop(), stack.pop()
                result = a * b
                stack.append(result)
        elif '/' == t:
            if len(stack) > 1:
                b, a = stack.pop(), stack.pop()
                result = a / b
                stack.append(result)
        else:
            stack.append(int(t))
    return stack[0]

print(postfixNotation('2 3 + 5 *'))
print(postfixNotation('4 2 / 3 - 2 *'))

# GPT가 손 봐준 코드
# def postfixNotation(input_text):
#     stack = []
#     text = input_text.split()
#
#     # 연산자와 함수 매핑
#     operators = {
#         '+': lambda x, y: x + y,
#         '-': lambda x, y: x - y,
#         '*': lambda x, y: x * y,
#         '/': lambda x, y: x / y
#     }
#
#     for t in text:
#         if t in operators:
#             if len(stack) > 1:
#                 b, a = stack.pop(), stack.pop()  # 스택에서 두 개의 피연산자 꺼내기
#                 stack.append(operators[t](a, b))  # 연산 수행 후 결과 다시 스택에 추가
#         else:
#             stack.append(int(t))  # 숫자는 스택에 추가
#
#     return stack[0]
#
# # 테스트
# print(postfixNotation('2 3 + 5 *'))   # (2 + 3) * 5 = 25
# print(postfixNotation('4 2 / 3 - 2 *'))  # ((4 / 2) - 3) * 2 = -2