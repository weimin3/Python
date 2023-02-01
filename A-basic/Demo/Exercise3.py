"""
> 练习：猜数字
> 定义一个变量，数字类型，基于input输入猜想的数字
"""

num = 10
if int(input("请输入您猜的数字：")) == num:
    print("猜对了")
elif int(input("猜错了，请再猜一次：")) == num:
    print("恭喜你，猜对了")
elif int(input("猜错了，请再猜一次：")) == num:
    print("恭喜你，猜对了")
else:
    print("三次都猜错了")