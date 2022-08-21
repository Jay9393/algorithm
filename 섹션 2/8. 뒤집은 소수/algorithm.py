def is_measure(n,k):
    cnt = 0
    for i in range(1, n+1):
        if n%i == 0:
            cnt += 1
        if cnt == k:
            print(i)
            return i
    print(-1)
    return -1

for i in range(1, 6):
    f = open(f"섹션 2/1. k번째 약수/in{i}.txt", "r")
    line = f.readline()
    n, k=map(int, line.split())
    f.close()
    f = open(f"섹션 2/1. k번째 약수/out{i}.txt", "r")
    answer = int(f.readline())
    f.close()

    if is_measure(n,k) == answer:
        print(f"in{i} ===== 정답입니다.")
    else:
        print(f"in{i} ===== 오답입니다.")
