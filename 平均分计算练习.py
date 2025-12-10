#3个5人班级
#你需要利用输入的每名学生的成绩，计算班级平均分和总分以及全员平均分
all_score = 0                                              #7
for x in range(1,4):                                       #1
    sum_score = 0                                          #4
    for y in range(1,6):                                   #2
        score = int(input(f"请输入{x}班{y}号同学的成绩"))      #3
        sum_score += score                                 #5
    print(f"{x}班的总分为{sum_score},平均分为{sum_score / 5}") #6
    all_score += sum_score                                  #8
