'''
练习：发奖金
某公司账户余额1万元，给20名员工发奖金。
- 员工编号从1到20，每人1000
- 绩效分1-10（随机生成），如低于5，无奖金
- 如奖金发完，结束发奖金
'''
import random

# 变量存储账户余额
balance = 10000
# 给20个人发奖金
for i in range(1,21):
    # 随机生成绩效
    r = random.randint(1,10)
    # 判断绩效的值
    if(r <= 5):
        print(f"{i}号员工，绩效是{r}，不发奖金")
        continue
    else:
        if(balance !=0):
            balance = balance - 1000
            print(f"{i}号员工，绩效是{r},发奖金1000元,账户余额{balance}")
        else:
            print("没钱了，下次再发")
            break
