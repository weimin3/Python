# 遍历列表[1，2，3，4，5，6，7，8，9，10]，取出列表中的偶数，存入一个新列表中
# - 使用while循环和for循环各操作一次
mylist = [1,2,3,4,5,6,7,8,9,10]

# while循环取出偶数存到新列表中
evenlist = list()
index = 0
while index < len(mylist):
    if mylist[index] % 2 == 0:
        evenlist.append(mylist[index])
    index += 1
print(evenlist)

# for循环取出偶数存到新列表中
elist=[]
for i in mylist:
    if(i % 2 ==0):
        elist.append(i)
print(elist)
