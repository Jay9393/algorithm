
for i in range(1, 6):
    f = open(f"섹션 3/2. 숫자만 추출/in{i}.txt", "r")
    line = f.readline()
    f.close()
    answer = ""
    for i in line:
        # try:
        #     answer = answer + str(int(i))
        # except:
        #     pass
        if i.isdecimal():
            answer = answer + i 

    answer = int(answer)
    print(answer)

    list_measure = list(filter(lambda x: answer%x == 0, range(1, answer+1)))
    print(len(list_measure))
