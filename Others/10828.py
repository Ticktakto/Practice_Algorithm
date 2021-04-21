#Stack
import sys

n = int(input())

arr = []

for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        arr.append(command[1])
    
    if command[0] == 'pop':
        if len(arr) == 0:
            print(-1)
        else:
            num = arr.pop()
            print(num)
    
    if command[0] == 'size':
        print(len(arr))
    
    if command[0] == 'empty':
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    
    if command[0] == 'top':
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])