for tc in range(1, 11):
    n = int(input()) # 암호문 길이
    pwd = list(map(int, input().split())) # 원본 암호문
    a = int(input()) # 명령어 갯수
    q = list(input().split()) # 명령어
    arr = [-1] * 100000 # arr에 최종 pwd를 저장할 것
    cnt = 0
    temp = [0] * 100000 # 임시 저장소
    for i in range(n):  # arr에 pwd 저장
        arr[i] = pwd[i]
    for i in q: # 명령어 q의 길이 세기
        cnt += 1
    for i in range(cnt): # 명령어 순회하다가
        if q[i] == 'I': # I 발견하면
            x = int(q[i+1])
            y = int(q[i+2])
            for j in range(x, cnt):
                temp[j] = arr[j]
            for j in range(y):
                arr[x+j] = q[i+3+j]
            for j in range(x, cnt):
                arr[j+y] = temp[j]
        if q[i] == 'D':
            x = int(q[i+1])
            y = int(q[i+2])
            for j in range(x, cnt):
                arr[j] = arr[j+y]
        if q[i] == 'A':
            y = int(q[i+1])
            for j in range(100000):
                if arr[j] == -1:
                    break
            for k in range(y):
                arr[j+k] = q[i+2+k]
    print('#%d' %tc, end = ' ')
    for i in range(10):
        print(arr[i], end = ' ')
    print()