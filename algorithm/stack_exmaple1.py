for tc in range(1, 11):
    N = int(input())
    arr = list(input())
    stack = []

    if N % 2 == 1:  # 홀수 개수의 괄호는 불가능함
        print(f'#{tc} 0')
        continue

    flag = True  # 정답 여부 판별 변수
    # 닫는 괄호일 때: stack 의 맨 위와 비교
    #  - stack 이 비어있다면, 불가능!
    #  - 가장 위의 괄호가 쌍이 맞다면 정상
    # 여는 괄호일 때: stack 에 넣어주고
    for w in arr:
        if w == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                flag = False
                break
        elif w == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                flag = False
                break
        elif w == '}':
            if len(stack) > 0 and stack[-1] == '{':
                stack.pop()
            else:
                flag = False
                break
        elif w == '>':
            if len(stack) > 0 and stack[-1] == '<':
                stack.pop()
            else:
                flag = False
                break
        else:  # 여는 괄호라면
            stack.append(w)

    if len(stack) > 0:  # 아직 여는 괄호가 남아 있다면, 잘못된 괄호
        flag = False

    # if flag:
    #     print(f'#{tc} 1')
    # else:
    #     print(f'#{tc} 0')

    # 출력 한 줄로 표현
    print(f'#{tc} 1' if flag else f'#{tc} 0')