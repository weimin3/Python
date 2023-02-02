'''
练习：
定义字符串变量name,内容为：'qazwsxedcvfredcxswqazaaassddfgrtvaadeada', for循环统计其中a的个数。
'''

name = 'qazwsxedcvfredcxswqazaaassddfgrtvaadeada'
count = 0
for x in name:
    if x == 'a':
        count += 1
print(f"{name}中一共有{count}个a")

