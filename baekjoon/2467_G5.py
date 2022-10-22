import sys
def find(target, left, right):
    mid = (left+right)//2
    if left == right:
        if abs(arr[left]-target) < a[2][0]:
            a[2] = [abs(arr[left]-target), arr[left], target*(-1)]
        if abs(arr[left+1]-target) <a[2][0] and target*(-1) != arr[left+1]:
            a[2] = [abs(arr[left+1]-target), arr[left+1], target*(-1)]
        if left-1 >= 0 and abs(arr[left-1]-target) <a[2][0]:
            a[2] = [abs(arr[left-1]-target), arr[left-1], target*(-1)]
        return
    if arr[mid] == target:
        a[2] = [0, arr[mid], target*(-1)]
        return
    elif arr[mid] < target:
        find(target, mid+1, right)
    elif arr[mid] >= target:
        find(target, left, mid)


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
index = -1
a = [[2000000001, 1000000001, 1000000001] for _ in range(4)]
for i in range(n):
    if arr[i] >= 0:
        index = i
        break
if index == -1:
    print(arr[n-2], arr[n-1])
elif index == 0:
    print(arr[0], arr[1])
else:
    if index != n-1:
        a[0] = [arr[index] + arr[index+1], arr[index], arr[index+1]]
    a[1] = [abs(arr[index-1] + arr[index-2]), arr[index-2], arr[index-1]]
    for i in range(index, n):
        find(arr[i]*(-1), 0, index-1)
    a.sort()
    print(a[0][1], a[0][2])
