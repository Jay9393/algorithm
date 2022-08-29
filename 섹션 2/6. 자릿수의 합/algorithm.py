def digit_sum(x):
    return sum(list(map(int, list(str(x)))))

for i in range(1, 6):
    f = open(f"섹션 2/6. 자릿수의 합/in{i}.txt", "r")
    lines = f.readlines()
    f.close()
    s = list(map(int, lines[1].split()))
    
    sum_list = [ digit_sum(x) for x in s ]
    answer_index = sum_list.index(max(sum_list))
    answer = s[answer_index]

    print(answer)