l = int(input())
s = input()
result = 0
for i in range(l):
    result += (ord(s[i])-ord('a')+1)*(31**i)
print(result%1234567891)