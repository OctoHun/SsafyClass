import sys
from collections import deque
string = sys.stdin.readline().rstrip()
arr1 = deque()
arr2 = deque()
length = len(string)
number = ''
for i in range(length):
    if string[i] != '-' and string[i] != '+':
        number += string[i]
    else:
        arr1.append(int(number))
        arr1.append(string[i])
        number = ''
arr1.append(int(number))
length = len(arr1)
flag = 0
for i in range(length):
    if flag == 0:
        if arr1[i] != '+' and arr1[i] != '-':
            arr2.append(arr1[i])
        elif arr1[i] == '+':
            flag = 1
    else:
        flag = 0
        temp = arr2.pop()
        arr2.append(temp+arr1[i])
first = arr2.popleft()
print(first - sum(arr2))

