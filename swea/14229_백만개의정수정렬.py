A = list(map(int, input().split()))
for i in range(500001):
    for j in range(i+1, len(A)):
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]
print(A[500000])
