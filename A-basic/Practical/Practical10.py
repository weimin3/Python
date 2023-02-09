# 定义一个元组记录学生信息（姓名，年龄，爱好）。
student_t = ("张三",28,["football","reading"])
# - 查询年龄所在的下标位置
index_age = student_t.index(28)
print(f"学生年龄的索引是：{index_age}")
# - 查询学生姓名
name = student_t[0]
print(f"学生姓名是：{name}")
# - 删除学生爱好中的football
del student_t[2][0]
print(student_t)
# - 增加coding 爱好到list中
student_t[2].append("coding")
print(student_t)

