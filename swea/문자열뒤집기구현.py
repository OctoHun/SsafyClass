def my_reverse1(a):
    len = 0
    for i in a:
        len += 1
    b = ''
    for i in range(len):
        b += a[len-1-i]
    return b


def my_reverse2(a):
    len = 0
    for i in a:
        len += 1
    a = list(a)
    for i in range(len//2):
        a[i], a[len-1-i] = a[len-1-i], a[i]

    return a


a = 'string'
print(my_reverse1(a))
print(my_reverse2(a))
