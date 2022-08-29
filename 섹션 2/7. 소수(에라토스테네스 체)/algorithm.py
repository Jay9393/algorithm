# *****
for i in range(1, 6):
    f = open(f"섹션 2/7. 소수(에라토스테네스 체)/in{i}.txt", "r")
    line = f.readline()
    f.close()
    n = int(line)

    ch = [0]*(n+1)
    cnt = 0

    for i in range(2, n+1):
        if ch[i] == 0:
            cnt += 1
            for j in range(i, n+1, i):
                    ch[j] = 1

    print(cnt)