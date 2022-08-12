def my_strcmp(a, b):
    if len(a) == len(b):
        for i in range(len(a)):
            if a[i] != b[i]:
                if ord(a[i]) - ord(b[i]) > 0:
                    return 1
                else:
                    return -1
        return 0
    elif len(a) > len(b):
        return 1
    else:
        return -1


#간단하게 부등호를 이용해 비교해도 된다.
#알아서 아스키코드로 비교해줌



a = 'string'
b = 'string'
print(my_strcmp(a, b))