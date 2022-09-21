import sys
sys.stdin = open("sample_input.txt", 'r')


code1 = {(2, 1, 1):'0', (2, 2, 1):'1', (1, 2, 2):'2', (4, 1, 1):'3', (1, 3, 2):'4', (2, 3, 1):'5', (1, 1, 4):'6', (3, 1, 2):'7', (2, 1, 3):'8', (1, 1, 2):'9'}
code2 = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}
# 찾고 바꾸기 쉽게 딕셔너리 형태로 만들어줌


t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [input().strip() for _ in range(n)]
    arr1 = []
    # arr1에 0으로만 이루어지지 않은 배열들 추가
    for i in range(n):
        for j in range(m-1, -1, -1):
            if arr[i][j] != '0':
                arr1.append(arr[i])

    # 세트로 만들어서 중복제거
    arr1 = set(arr1)
    arr1=list(arr1)
    ans = 0
    visit = []
    # change2에 2진수로 변환하여 저장
    for i in range(len(arr1)):
        change2 = ''
        for j in range(len(arr1[i])):
            change2 += code2[arr1[i][j]]
        # 오른쪽에 있는 0들은 전부 제거
        change2 = change2.rstrip('0')


        cnt = 0 # 8자리 맞는지 세주기
        result = ''
        odd = 0
        even = 0
        n1, n2, n3, n4 = 0, 0, 0, 0
        for j in range(len(change2)-1, -1, -1):
            # 오른쪽에서부터 1과 0들의 개수를 세서 n3, n2, n1에 저장장
            if change2[j] == '1' and n3 == 0:
                n4 += 1
            elif change2[j] == '0' and n2 == 0:
                n3 += 1
            elif change2[j] == '1' and n1 == 0:
                n2 += 1
            elif change2[j] == '0' and change2[j-1] == '1':
                X = min(n4, n3, n2) # 배율
                # 암호코드를 보면 전부 1이 끼어있어서 가장 작은 수로 나누면 그것이 곧 비율이 됨
                pwd = code1[(n2 // X, n3 // X, n4 // X)]
                result += pwd
                pwd = int(pwd)
                cnt += 1
                n1, n2, n3, n4 = 0, 0, 0, 0
                if cnt == 8:
                    if result not in visit:
                        visit.append(result)
                        odd += pwd
                        if (odd*3 + even + pw) % 10 == 0:
                            ans += odd+even+pw
                    odd, even, cnt = 0, 0, 0
                    result = ''
                elif cnt == 1:
                    pw = pwd
                elif cnt % 2 == 0:
                    odd += pwd
                else:
                    even += pwd

    print('#%d' %tc, ans)