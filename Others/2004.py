# https://somjang.tistory.com/entry/BaeKJoon-2004번-조합-0의-개수-Python

m, n = map(int, input().split())

def countNum(n, num):
    count = 0
    divNum = num
    while n >= divNum:
        count += (n // divNum)
        divNum = divNum * num
    return count

res = min(countNum(m,5) - countNum(n,5) - countNum(m-n,5), 
          countNum(m,2) - countNum(n,2) - countNum(m-n,2))
print(res) 