for i in range(1, 11):
    n= int(input())
    pw1 = list(map(int, input().split()))
    a = int(input())
    arr = list(map(str, input().split()))
    pw2 = [-1] * 1000
    c = len(pw1)
    j = 0
    for j in range(len(pw1)):
        pw2[j] = pw1[j]
    for l in range(len(arr)-1, -1, -1):
        if arr[l] == 'I':
            break
    while 1:
        if arr[j] == 'I':
            for k in range(c-1, int(arr[j+1])-1, -1):
                pw2[k+int(arr[j+2])] = pw2[k]
            for k in range(int(arr[j+1]), int(arr[j+1]) + int(arr[j+2])):
                pw2[k] = arr[j+2+k]
            pw1 = pw2
            pw2 = [-1] * 1000
            for k in range(1000):
                if pw1[k] == -1:
                    c = k
                    break
        j += 1
        if j == a:
            break
    print('#%d' %i, end = ' ')
    for k in range(1000):
        if pw1[k] == -1:
            break
        else:
            print(pw1[k], end = ' ')
    print()
