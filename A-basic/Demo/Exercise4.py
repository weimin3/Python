"""
公司发礼物，条件是：
> 1. 必须是18-30之间的成年人
> 2. 同时入职时间大于两年，或者级别大于3
"""
age = int(input("请输入您的年龄:"))
level = int(input("请输入您的职级:"))
year = int (input("请输入您的入职时间："))
if age >= 18:
    if age < 30:
        if year > 2 :
            print("您可以领礼物呀")
        else:
           print("您不可以领礼物")
    elif level > 3:
        print("可直接领礼物")
    else:
        print("年龄超过30，且职级未达到30以上，不可以领礼物")
else:
    print("年龄不达标，无法领礼物")
