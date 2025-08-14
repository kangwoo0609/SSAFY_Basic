# 계산기 2번 문제

# 우선순위표
priority = {'+': 1, '*': 2}

# 1. 중위 -> 후위표기법으로 바꾸는 함수
def infix_to_postfix(tokens):
    stack = []          # 후위표기법 최종 결과
    oper_stack = []     # 연산자들이 중간에 거쳐갈 스택

    for token in tokens:
        # 1. 숫자라면, 그냥 stack 에 쌓는다
        if token.isdigit():
            stack.append(token)

        # 2. 연산자라면
        else:
            # oper_stack 에 남아있는 연산자들 중에서
            # 나보다 우선순위가 높거나 같은 연산자들을
            # stack 으로 이동 (반복문)
            # [주의] 반복하면서 pop()을 하는 경우, 항상 데이터가 있는 지 함께 체크
            while oper_stack and priority[oper_stack[-1]] >= priority[token]:
                stack.append(oper_stack.pop())

            oper_stack.append(token)

    # 남아 있는 연산자들을 뒤에서부터 스택으로 이동
    while oper_stack:
        stack.append(oper_stack.pop())

    return stack


# 2. 후위표기법을 계산하는 함수
def calculate(tokens):
    stack = []

    for token in tokens:
        # 숫자라면, stack 에 넣는다
        if token.isdigit():
            stack.append(int(token))
        # 아니라면, stack 에서 숫자 2개를 꺼내서 계산한다.
        # - 계산 결과를 stack 에 넣어준다.
        else:
            num1 = stack.pop()
            num2 = stack.pop()

            # +, * 두 가지 연산이 존재
            if token == '+':
                stack.append(num1 + num2)
            else:
                stack.append(num1 * num2)

    # stack 에 남은 최종 결과를 return
    return stack[0]


for tc in range(1, 11):
    N = int(input())
    row = input()
    postfix = infix_to_postfix(row)
    result = calculate(postfix)
    print(f'#{tc} {result}')