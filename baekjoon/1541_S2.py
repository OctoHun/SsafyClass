import sys
from collections import deque
string = sys.stdin.readline().rstrip()
arr = deque(string)
length = len(string)
for i in range(length):
    if arr[i] == '+':
        target1 = ''
        target2 = ''
        for j in range(1, 6):
            if arr[i+j] != '+' and arr[i+j] != '-':
                target1 += arr[i+j]
            if arr[i - j] != '+' and arr[i + j] != '-':
                target2 += arr[i-j]


