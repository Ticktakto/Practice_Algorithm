# https://duwjdtn11.tistory.com/512
# 2 -> 10 -> 8 로 바꾸면 시간초과!!

# 내장함수를 활용하자
res = int(input(), 8)
# bin(res) = '0b' + 'num' => 0o는 8진수를 나타내는 의미!
res = bin(res)[2:]
print(res)