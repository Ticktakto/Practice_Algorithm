# https://bnzn2426.tistory.com/112
import sys

# 두 스택의 경계선 => 커서!
stack1 = list(sys.stdin.readline().strip())
stack2 = []
n = int(input())

for i in range(n):
    command = sys.stdin.readline().strip()

    if command[0] == 'L':
        if stack1:
            stack2.append(stack1.pop())
        else:
            continue

    if command[0] == 'D':
        if stack2:
            stack1.append(stack2.pop())
        else:
            continue

    if command[0] == 'B':
        if stack1:
            stack1.pop()
        else:
            continue
    if command[0] == 'P':
        stack1.append(command[2])
        

print(''.join(stack1 + list(reversed(stack2))))