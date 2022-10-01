from collections import deque
n = int(input())
arr = [0] * (n+1)
for i in range(n):
    arr[i] = int(input())
stack = deque()
result = [0]*(n+1)
ans = [0]*1000000
# arr는 만들어야 할 수열
# stack은 저장할 스텍 공간
# result 내가 만든 수열
now = 0
index = 1
ans_index = 0
while result[n-1] == 0:
    if stack and stack[len(stack)-1] == arr[now]:
        result[now] = stack.pop()
        ans[ans_index] = '-'
        ans_index += 1
        now += 1
    else:
        stack.append(index)
        index += 1
        ans[ans_index] = '+'
        ans_index += 1
    if index > n+1:
        ans[0] = 0
        break
if ans[0] == 0 or result[n-1] != arr[n-1]:
    print('NO')
else:
    for i in ans:
        if i == 0:
            break
        print(i)