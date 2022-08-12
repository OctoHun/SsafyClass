s1 = 'abc'
s2 = 'abc'
s3 = 'def'
s4 = s1
s5 = s1[:2] + 'c'

print(s1 == s2)
print(s1 is s2)
print(s1 == s3)
print(s1 is s3)
print(s1 == s4)
print(s1 is s4)
print(s1 == s5)
print(s1 is s5)

# '=='은 모양이 같은가를 판단, 'is'는 주소까지 판단