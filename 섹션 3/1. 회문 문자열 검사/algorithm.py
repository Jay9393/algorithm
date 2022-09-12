
for i in range(1, 6):
    f = open(f"섹션 3/1. 회문 문자열 검사/in{i}.txt", "r")
    lines = f.readlines()
    f.close()
    n = int(lines[0])
    strings = list(map(lambda x: x.strip().lower(), lines[1:]))
    k = 1

    for s in strings:
        if s[::-1] == s:
            print(f"#{k} YES")
        else :
            print(f"#{k} NO")
        k += 1
