#Queue
import sys
from collections import deque
n = int(input())

queue = deque()
for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        num = int(command[1])
        queue.append(num)

    if command[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            res = queue.popleft()
            print(res)

    if command[0] == 'size':
        print(len(queue))

    if command[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    if command[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])

    if command[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
