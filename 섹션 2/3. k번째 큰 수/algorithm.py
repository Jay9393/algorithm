for i in range(1, 6):
    f = open(f"섹션 2/1. k번째 큰 수/in{i}.txt", "r")
    line = f.readline()
    n, k=map(int, line.split())
    f.close()
    f = open(f"섹션 2/1. k번째 큰 수/out{i}.txt", "r")
    answer = int(f.readline())
    f.close()
