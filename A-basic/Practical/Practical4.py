'''
练习： 统计偶数个数
使用range()语句，获取从1到num（num是任意数）的序列，统计偶数的个数
'''
count = 0
for x in range(1,100):
    if(x%2==0):
        count +=1

print(f"1-100之间一共有{count}个偶数")

