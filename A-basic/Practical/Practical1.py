"""
随机生成一个1-10的数字，通过三次判断猜出数字
> 要求：
> 1） 数字随机生成
> 2）通过3层嵌套进行猜并判断
> 3）每次提示 猜中 猜大了或 猜小了
"""
import random
num = random.randint(1,10)

guess = (int(input("请输入你猜的数字")))

if guess == num:
    print("恭喜你，猜对了")
else:
    if guess > num:
        print("猜大了")
    else:
        print("猜小了")

    guess = (int(input("请第二次输入你猜的数字")))

    if guess == num:
        print("恭喜你，猜对了")
    else:
        if guess > num:
            print("猜大了")
        else:
            print("猜小了")

        guess = (int(input("请第三次输入你猜的数字")))

        if guess == num:
            print("恭喜你，猜对了")
        else:
            print("猜错了")
