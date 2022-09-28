n = int(input())
arr = list(map(int, input().split()))
student = [0] * n
for i in range(1, n+1):
    student[i-1] = i
for i in range(n):
    for j in range(arr[i], 0, -1):
        student[i], student[i-j] = student[i-j], student[i]
for i in range(n):
    print(student[i], end = ' ')