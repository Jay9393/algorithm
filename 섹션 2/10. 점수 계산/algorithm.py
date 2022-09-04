for i in range(1, 6):
    f = open(f"섹션 2/10. 점수 계산/in{i}.txt", "r")
    lines = f.readlines()
    f.close()
    n = int(lines[0])
    answers = list(map(int, lines[1].split()))
    points = [0]

    for i in range(0, n):
        if answers[i] == 1:
            points.append(points[i]+1)
        elif answers[i] == 0:
            points.append(0)
    print(sum(points))
