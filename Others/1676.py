# https://developmentdiary.tistory.com/332
n=int(input())

# RunTime Error -> 재귀형식은 불가능! 
factorial=[1 for _ in range(n+1)]
 
for i in range(1,n+1):
    factorial[i]=i*factorial[i-1]
 
 
result=0
check=1
while check:
    if factorial[n]%10==0:
        factorial[n]//=10
        result+=1
    else: #  한 번이라도 0이 없다면 그대로 종료
        check=0
 
 
print(result)
