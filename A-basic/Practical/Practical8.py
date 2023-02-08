# 一个记录学生年龄的列表=[21，25，21，23，22，20]，对其进行如下操作：
# 1. 定义这个列表，并用变量接收它
l = [21,25,21,23,22,20]
# 2. 在列表尾部追加一个数字31
l.append(31)
print(l)
# 3. 在列表尾部追击一个列表[29,33,30]
l.extend([29,33,30])
print(l)
# 4. 取出第一个元素
first_element = l[0]
print(first_element)
# 5. 取出最后一个元素
last_element = l[-1]
print(last_element)
# 6. 查找元素31在列表中的下标位置
index_31 = l.index(31)
print(f"元素31在列表中的下标位置是：{index_31}" )