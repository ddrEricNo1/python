import random
num = random.randint(1, 100)

# 通过一个布尔类型变量，做循环是否继续的标记
flag = True

while flag:
    guess_num = int(input("请输入你猜测的数字:"))
    if guess_num == num:    # 猜中
        print("猜中了")
        flag = False
    else:
        print("猜错了")
        if guess_num < num:
            print("猜小了")
        else:
            print("猜大了")
