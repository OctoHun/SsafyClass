a = [7, 6, 0, 5, 8, 9, 3, 2]

for i in range(7,0, -1):
    for j in range(i):
        if a[j]>a[j+1]:
            a[j], a[j+1] =  a[j+1], a[j]
print(a)