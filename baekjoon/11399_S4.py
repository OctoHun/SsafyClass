N = int(input())
p = list(map(int, input().split()))
p.sort()
time = 0
for i in range(N):
    time += p[i]*(N-i)
print(time)