import sys

def search(ys, ye, xs, xe):
    global white, blue
    cnt = 0
    if ys >= ye:
        if arr[ys][xs] == 1:
            blue += 1
        else:
            white += 1
        return
    for i in range(ys, ye):
        for j in range(xs, xe):
            if arr[i][j] == 1:
                cnt += 1
    if cnt == (xe-xs)**2:
        blue += 1
        return
    elif cnt == 0:
        white += 1
        return
    else:
        search(ys, (ye+ys)//2, xs, (xe+xs)//2)
        search(ys, (ye+ys)//2, (xe+xs)//2, xe)
        search((ye+ys)//2, ye, xs, (xe+xs)//2)
        search((ye+ys)//2, ye, (xe+xs)//2, xe)
        return


n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
white = 0
blue = 0
search(0, n, 0, n)
print(white)
print(blue)