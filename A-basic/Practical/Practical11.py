
# - 给定一个字符串"how are you"
S = "how are you"
# - 统计字符串内有多少个o
c = S.count('o')
print(f"字符串{S}内有{c} 个'o'")
# - 将空格替换为"｜"
b = S.replace(" ","|")
print(b)
# - 按照"｜"进行分割，得到列表
l=b.split("|")
print(l)