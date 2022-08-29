for i in range(1, 6):
    f = open(f"섹션 2/9. 주사위 게임/in{i}.txt", "r")
    lines = f.readlines()
    f.close()
    n = int(lines[0])
    result = 0

    for i in range(1, n+1):
        points = list(map(int, lines[i].split()))
        if len(set(points)) == 3:
            if max(points)*100 > result:
                result = max(points)*100
        elif len(set(points)) == 2:
            for j in set(points):
                if points.count(j) == 2:
                    if 1000+j*100 > result:
                        result = 1000+j*100
                        break
        else:
            if 10000+points[0]*1000 > result:
                result = 10000+points[0]*1000
    print(result)
