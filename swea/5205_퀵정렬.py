def quickSort(arr, start, end):
    if start >= end:
        return
    pivot = start
    left, right = start+1, end
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] > arr[pivot]:
            right -= 1
        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]
    quickSort(arr, start, right-1)
    quickSort(arr, right+1, end)


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    quickSort(arr, 0, n-1)
    print('#%d' %tc, arr[n//2])