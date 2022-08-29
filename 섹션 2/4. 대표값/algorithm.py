
for i in range(1, 6):
    f = open(f"섹션 2/4. 대표값/in{i}.txt", "r")
    lines = f.readlines()
    f.close()
    n = int(lines[0])
    scores = list(map(int, lines[1].split()))
    average = sum(scores)/n
    average = average + 0.5
    average = int(average)
    min = 3000

    for i, x in enumerate(scores):
        tmp = abs(x-average)
        if tmp < min:
            min = tmp
            score = x
            result = i + 1
        elif tmp == min:
            if x > score:
                score = x
                result = i + 1
    print(average, result)