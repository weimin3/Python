# 定义全局变量money记录银行卡余额，默认5000000
money = 5000000
# 定义name全局变量记录客户信息
name = input("请输入您的姓名：")

# 定义查询余额函数
def query(show_header):
    if show_header:
        print("-------查询余额---------")
    print(f"{name},您卡上的余额是：{money} 元。")

#定义取款函数
def withdraw():
    print("-------取款---------")
    num1 = int(input("请输入取款金额："))
    global money
    money -= num1
    print(f"{name}，您取款{num1}元")
    query(False)

#定义存款函数
def saving():
    print("-------存款---------")
    num2 = int(input("请输入存款金额："))
    global money
    money += num2
    print(f"{name}，您存款{num2}元")
    query(False)

#定义主菜单函数
'''
您好！欢迎登陆

查询余额【输入1】

存款【输入2】

取款【输入3】

退出【输入4】

请输入您的选择：
'''
def main_face():
    print("-------主菜单---------")
    print(f"{name} 您好！欢迎登陆")
    print("查询余额\t【输入1】")
    print("存款\t【输入2】")
    print("取款\t【输入3】")
    print("退出\t【输入4】")
    input_num = input("请输入您的选择")
    return input_num

#设置循环保证程序循环运行
while True:
    in_num = main_face()
    if in_num == "1":
        query(True)
        continue #重新进入主菜单
    elif in_num == "2":
        saving()
        continue
    elif in_num == "3":
        withdraw()
        continue
    else:
        break;



