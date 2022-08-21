
for i in range(1, 6):
    f = open(f"섹션 2/2. K번째 수/in{i}.txt", "r")
    lines = f.readlines()
    f.close()
    t = int(lines[0])
    
    for j in range(1, t+1):
        n,s,e,k=map(int, lines[2*j-1].split())
        a = list(map(int, lines[2*j].split()))
        a = a[s-1:e]
        a.sort()
        print(f"#{j} {a[k-1]}")
    
    # f = open(f"섹션 2/2. k번째 수/out{i}.txt", "r")
    # answer = int(f.readline())
    # f.close()