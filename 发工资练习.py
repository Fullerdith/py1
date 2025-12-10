import random
account = 10000#公司账户有1w元
for i in range(1,21):
    score = random.randint(0,10)#绩效随机1-10，小于5没工资
    if score >=5:
        account -= 1000
        print(f"为{i}号员工派发工资一千元")
    elif score < 5:
        continue#切换下一位员工
    if account <= 0:
        break