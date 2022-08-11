for i in range(1, 11):
    a = int(input())
    b= list(map(int, input().split()))
    cnt = 0
    for j in range(2, a-2):
        max=0
        if b[j]>b[j-1] and b[j]>b[j-2] and b[j]>b[j+1] and b[j]>b[j+2]:
            arr=[b[j-1], b[j-2], b[j+1], b[j+2]]
            for k in range(4):
                if arr[k]>max:
                    max=arr[k]
            cnt += b[j]-max
    print('#%d' %i, cnt)