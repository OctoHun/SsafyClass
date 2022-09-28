a = input()
arr = [0] * 100
max = 0
maxindex = 0
ans = ''
for i in a:
    if ord('a') <= ord(i) <= ord('z'):
        result = ord(i) - ord('a') + ord('A')
        arr[result] += 1
    else:
        arr[ord(i)] += 1
for i in range(100):
    if arr[i] > max:
        max = arr[i]
        maxindex = i
        ans = ''
    elif arr[i] == max:
        ans = '?'
if ans == '?':
    print(ans)
else:
    print(chr(maxindex))