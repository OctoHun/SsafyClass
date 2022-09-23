t = int(input())
for tc in range(1, t+1):
    sec = input()
    thr = input()
    length_sec = len(sec)
    length_thr = len(thr)
    ans = 0
    for i in range(length_sec):
        sec = list(sec)
        if sec[i] == '1':
            sec[i] = '0'
        else:
            sec[i] = '1'
        sec = ''.join(sec)
        for j in range(length_thr):
            thr = list(thr)
            if thr[j] == '2':
                thr[j] = '1'
                thr = ''.join(thr)
                if int(thr, 3) == int(sec, 2):
                    ans = int(sec, 2)
                    break
                thr = list(thr)
                thr[j] = '0'
                thr = ''.join(thr)
                if int(thr, 3) == int(sec, 2):
                    ans = int(sec, 2)
                    break
                thr = list(thr)
                thr[j] = '2'
            if thr[j] == '1':
                thr[j] = '2'
                thr = ''.join(thr)
                if int(thr, 3) == int(sec, 2):
                    ans = int(sec, 2)
                    break
                thr = list(thr)
                thr[j] = '0'
                thr = ''.join(thr)
                if int(thr, 3) == int(sec, 2):
                    ans = int(sec, 2)
                    break
                thr = list(thr)
                thr[j] = '1'
            if thr[j] == '0':
                thr[j] = '1'
                thr = ''.join(thr)
                if int(thr, 3) == int(sec, 2):
                    ans = int(sec, 2)
                    break
                thr = list(thr)
                thr[j] = '2'
                thr = ''.join(thr)
                if int(thr, 3) == int(sec, 2):
                    ans = int(sec, 2)
                    break
                thr = list(thr)
                thr[j] = '0'
        if ans != 0:
            break
        sec = list(sec)
        if sec[i] == '1':
            sec[i] = '0'
        else:
            sec[i] = '1'
    print('#%d' %tc, ans)
