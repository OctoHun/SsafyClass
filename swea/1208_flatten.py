for i in range(1, 11):
    N = int(input())
    a = list(map(int, input().split()))
    arr = [0] * 101
    max_height=0
    min_heigth=0
    l_index=0
    r_index=100
    for j in range(100):
        arr[a[j]]+=1
    for j in range(N):
        for k in range(l_index, 100):
            if arr[k]>0:
                arr[k]-=1
                arr[k+1]+=1
                l_index=k
                break
        for k in range(r_index, -1, -1):
            if arr[k]>0:
                arr[k]-=1
                arr[k-1]+=1
                r_index=k
                break
    for k in range(l_index, 100):
        if arr[k] > 0:
            min_height=k
            break
    for k in range(r_index, -1, -1):
        if arr[k] > 0:
            max_height=k
            break
    print('#%d' %i, max_height-min_height)
