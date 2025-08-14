# 계산기 1번 문제

# 1. 중위 -> 후위표기법으로 바꾸는 함수
def infix_to_postfix(tokens):
    stack = []          # 후위표기법 최종 결과
    oper_stack = []     # 연산자들이 중간에 거쳐갈 스택

    for token in tokens:
        # 1. 숫자라면, 그냥 stack 에 쌓는다
        if token.isdigit():
            stack.append(token)

        # 2. 연산자라면
        # - oper_stack 에 연산자가 있는 지 확인
        #   - 있다면
        #     - 기존 연산자를 꺼내서 stack 에 넣는다.
        #     - 현재 연산자를 oper_stack 에 넣는다.
        #   - 없다면, oper_stack 에 추가
        else:
            if oper_stack:
                stack.append(oper_stack.pop())
            # oper_stack 에 현재 연산자를 추가하는 코드는
            # 조건이 만족하던 하지않던 무조건 동작한다
            # --> else 없애기 + 내어쓰기
            oper_stack.append(token)

    # oper_stack 에 남은 연산자를 stack 에 넣어준다
    # (마지막 연산자)
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

            stack.append(num1 + num2)

    # stack 에 남은 최종 결과를 return
    return stack[0]


for tc in range(1, 11):
    N = int(input())
    row = input()
    postfix = infix_to_postfix(row)
    result = calculate(postfix)
    print(f'#{tc} {result}')