m, n = map(int, input().split())
key = []
lock = []

for _ in range(m):
    key.append(list(map(int, input().split())))

for _ in range(n):
    lock.append(list(map(int, input().split())))

# 외우자!!
def rotation(a):
    n = len(a)
    m = len(a[0])
    res = [[0] * n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            res[j][n-i-1] = a[i][j] 
    return res

def find(lock):
    normal_length = len(lock) // 3
    # 원래 자물쇠 위치( 중간 )
    for i in range(normal_length, normal_length*2):
        for j in range(normal_length, normal_length*2):
            if lock[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    # 3배 크기의 새로운 자물쇠, 중간 부분은 원래 자물쇠 값
    new_lock = [[0] * (n+3) for _ in range(n+3)]
    
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n] = lock[i][j]

    rotate_key = key
    # 회전시킨 key (4방향) 모두 완전 탐색 수행
    for _ in range(4):
        rotate_key = rotation(rotate_key)
        
        #(n*2-1) == 중간 부분(실제 자물쇠)의 마지막 부분
        for x in range(n*2): 
            for y in range(n*2):
                # 자물솨에 열쇠 끼우기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += rotate_key[i][j]  
                
                if find(new_lock) == True:
                    return True
                # 자몰쇠에 열쇠 빼기
                for i in range(m):
                    for j in range(n):
                        new_lock[x+i][y+j] -= rotate_key[i][j]
    return False 
        
        
print(solution(key,lock))