"""
练习：无限猜数
随机生成1-100之间的整数，猜数，直到猜对为止。
"""
import random
r = random.randint(1,100)
count = 1
flag = True
while(flag):
    guess = int(input(f"请输入你第{count}次猜的数："))
    if(guess > r):
        print("猜大了")
    elif (guess < r):
        print("猜小了")
    else:
        print("猜中了")
        flag = False

    count +=1
