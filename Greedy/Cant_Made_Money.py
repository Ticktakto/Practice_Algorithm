n = int(input())
coins = list(map(int, input().split()))

coins.sort()
# 1원이 없다면, 언제나 1원이 return

# target은, 해당 값 이하로는 모두 만들 수 있다는 의미..
target = 1

for x in coins:
    # 못 만드는 금액을 찾으면 끝! 아니면, 해당 동전 범위 다 수행하면 바로 다음 값(+1) return
    if target < x:
        break
    target += x

print(target)