from pickle import TRUE


for i in range(1, 6):
    f = open(f"섹션 2/3. K번째 큰 수/in{i}.txt", "r")
    lines = f.readlines()
    f.close()
    n, k = map(int, lines[0].split())
    cards = list(map(int, lines[1].split()))
    result = set()
    for j in range(n):
        for l in range(j+1, n):
            for m in range(l+1, n):
                result.add(cards[j] + cards[l] + cards[m])
    result = list(result)
    result.sort(reverse=True)
    print(result[k-1])
    print(f"==================={i}=================")
    