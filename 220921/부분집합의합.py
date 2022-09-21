def abc(i, n, result):
    global cnt
    if i == n:
        if result == 0 and ans:
            cnt += 1
            for i in ans:
                print(i, end = ' ')
            print()
        return
    ans.append(arr[i])
    abc(i+1, n, result+arr[i])
    ans.pop()
    abc(i+1, n, result)


arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
ans = []
cnt = 0
result = 0
abc(0, 10, result)
print(cnt)