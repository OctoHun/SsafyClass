t = int(input())
for i in range(1, t+1):
    str1 = input()
    str2 = input()
    cnt = 0
    for j in str1:
        cnt += 1
    a = cnt
    cnt = 0
    for j in str2:
        cnt += 1
    b = cnt
    arr = [0] * 100
    max = 0
    for j in range(b):
        arr[ord(str2[j])] += 1
    for j in range(a):
        if arr[ord(str1[j])]> max:
            max = arr[ord(str1[j])]
    print('#%d' %i, max)