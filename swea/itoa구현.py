def return_str(a):
    i = 10
    s = ""
    while 1:
        mod = a% i
        s += chr(ord('0') + mod)
        a = a//10
        if a == 0:
            return s[::-1]



a = int(input())
print(return_str(a))