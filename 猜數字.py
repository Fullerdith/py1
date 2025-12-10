import random
list1 = [2,4,6,8,10]
ran_num = random.choice(list1)
count = 0
while True:
    user_num = int(input("请输入数字"))
    count += 1
    if user_num > ran_num:
        print("数字过大，再试一次吧！")
    elif user_num < ran_num:
        print("数字过小，再试一次吧！")
    elif user_num == ran_num:
        print("真棒，答对了！")
        break