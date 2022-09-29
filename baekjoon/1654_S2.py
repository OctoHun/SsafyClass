k, n = map(int, input().split())
total_length = 0
arr = [int(input()) for _ in range(k)]
for i in range(k):
    total_length += arr[i]
c = total_length//n
left = 0
right = c+1
while 1:
    if left == right:
        break
    mid = (left+right)//2
    rope = 0
    for i in range(k):
        rope += arr[i]//mid
    if rope >= n:
        left = mid+1
    else:
        right = mid
print(left-1)