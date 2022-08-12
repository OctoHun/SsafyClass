def strlen(a):
    i=0
    while(1):
        if a[i]=='\0':
            return i
        else:
            i += 1


a = ['a', 'b', 'c', '\0']
ans = strlen(a)
print(ans)