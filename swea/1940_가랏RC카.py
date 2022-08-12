t = int(input())
for i in range(1, 1+t):
    N = int(input())
    distance = 0
    vel = 0
    for j in range(N):
        a = input()
        if len(a) == 1:
            a = int(a)
        else:
            a, b = map(int, a.split())
        if a==0:
            distance += vel
        elif a==1:
            vel += b
            distance += vel
        else:
            vel -= b
            if vel <0:
                vel = 0
            distance += vel
    print('#%d' %i, distance)
