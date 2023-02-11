# - 有如下列表对象：my_list = ['today','is','sunday','are','you','enjoying','the','sunshine']
# - 定义一个空集合，通过for循环遍历列表，将元素添加到集合，将集合打印出来
my_list = ['today','is','sunday','are','you','enjoying','the','sunshine','is']
# 定义一个空集合
set1=set()
# 遍历列表，添加元素到集合
for i in my_list:
    set1.add(i)
# 打印集合
print(set1)
