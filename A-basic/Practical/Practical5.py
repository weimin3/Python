# 用for循环输出九九乘法表
# i = 1
# j = 1
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j} * {i} = {i*j}\t", end = "")
    print()