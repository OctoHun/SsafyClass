# def meeting(a, start, end, cnt):
#     global max
#     for k in range(a+1, n):
#         if temp[k] == 1:
#             if arr[k][0] >= end or arr[k][1] <= start:
#                 pass
#             else:
#                 temp[k] = 0
#     for j in range(n):
#         if temp[j] == 1:
#             temp[j] = 0
#             meeting(j, arr[j][0], arr[j][1], cnt+1)
#     if cnt > max:
#         max = cnt
#
#
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# max = 0
# temp = [1] * n
# for i in range(n):
#     temp[i] = 0
#     meeting(i, arr[i][0], arr[i][1], 1)
# print(max)

#///////////////////////////////////////////////////////////////


#
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# max = 0
#
# flag = 0
# while flag < n:
#     cnt = 0
#     temp = [1] * n
#     for i in range(flag):
#         temp[i] = 0
#     for i in range(n):
#         if temp[i] == 1:
#             temp[i] = 0
#             cnt += 1
#             for j in range(i+1, n):
#                 if arr[j][0] >= arr[i][1] or arr[j][1] <= arr[i][0]:
#                     pass
#                 else:
#                     temp[j] = 0
#     if cnt > max:
#         max = cnt
#     flag += 1
# print(max)

# ///////////////////////////////////////////////////////////




n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: (x[1], x[0]))
max = 0
end = arr[0][1]
cnt = 1
for i in range(1, n):
    if end <= arr[i][0]:
        cnt += 1
        end = arr[i][1]
print(cnt)

