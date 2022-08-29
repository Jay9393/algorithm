def digit_sum(x):
    return sum(list(map(int, list(str(x)))))

for i in range(1, 6):
    f = open(f"섹션 2/5. 정다면체/in{i}.txt", "r")
    line = f.readline()
    f.close()
    s = list(map(int, line.split()))
    nums = []

    for i in range(1, s[0]+1):
        for j in range(1, s[1]+1):
            nums.append(i+j)

    set_nums = set(nums)
    dic_nums = {}

    for i in set_nums:
        dic_nums[i] = nums.count(i)

    max_num = max(dic_nums.values())
    answer =[]

    for k, v in dic_nums.items():
        if v == max_num:
            answer.append(k)
    answer.sort()

    for i in answer:
        print(i, end=' ')
    print('\n')