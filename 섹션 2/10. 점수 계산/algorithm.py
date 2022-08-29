for i in range(1, 6):
    f = open(f"섹션 2/1. k번째 약수/in{i}.txt", "r")
    line = f.readline()
    f.close()
    n, k=map(int, line.split())
    f = open(f"섹션 2/1. k번째 약수/out{i}.txt", "r")
    answer = int(f.readline())
    f.close()

    if is_measure(n,k) == answer:
        print(f"in{i} ===== 정답입니다.")
    else:
        print(f"in{i} ===== 오답입니다.")
