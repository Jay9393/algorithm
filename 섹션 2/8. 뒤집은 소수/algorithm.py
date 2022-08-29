for i in range(1, 6):
    f = open(f"섹션 2/8. 뒤집은 소수/in{i}.txt", "r")
    lines = f.readlines()
    f.close()
    nums = lines[1].split()
    reverse_nums = [ int(i[::-1]) for i in nums ]
    for i, v in enumerate(reverse_nums):
        if v == 2:
            print(2, end=' ')

        for j in range(2, v):
            if v%j == 0 :
                break
            if j == v-1 :
                print(reverse_nums[i], end=' ')
    print("\n")