# Python
Python 学习笔记
<!-- TOC -->
* [Python](#python)
  * [1. 基础入门](#1-基础入门)
    * [1.1 基础语法](#11-基础语法)
    * [1.2 判断语句](#12-判断语句)
      * [1.2.1 布尔类型和比较运算符](#121-布尔类型和比较运算符)
      * [1.2.2 if语句的基本格式](#122-if语句的基本格式)
      * [1.2.3 if else 语句](#123-if-else-语句)
      * [1.2.4 if elif else语句](#124-if-elif-else语句)
      * [1.2.5 判断语句的嵌套](#125-判断语句的嵌套)
      * [1.2.6 练习](#126-练习)
    * [1.3 循环语句](#13-循环语句)
      * [1.3.1 while循环的基本语法](#131-while循环的基本语法)
      * [1.3.2 while循环的基本案例](#132-while循环的基本案例)
      * [1.3.3 while循环的嵌套案例](#133-while循环的嵌套案例)
      * [1.3.5 for循环的基本语法](#135-for循环的基本语法)
      * [1.3.6 for循环的嵌套应用](#136-for循环的嵌套应用)
      * [1.3.7 循环中断：break和continue](#137-循环中断break和continue)
      * [1.3.8 综合案例](#138-综合案例)
    * [1.4 函数](#14-函数)
    * [1.5 数据容器](#15-数据容器)
      * [1.5.1 列表](#151-列表)
      * [1.5.2 元组](#152-元组)
      * [1.5.3 字符串](#153-字符串)
      * [1.5.4 序列的切片](#154-序列的切片)
      * [1.5.5 集合](#155-集合)
      * [1.5.6 字典](#156-字典)
      * [1.5.7 数据容器对比](#157-数据容器对比)
      * [1.5.8 字符串大小比较](#158-字符串大小比较)
    * [1.6 文件操作](#16-文件操作)
    * [1.7 异常](#17-异常)
    * [1.8 模块](#18-模块)
    * [1.9 包](#19-包)
    * [1.10 自定义工具包 【code】](#110-自定义工具包-code)
    * [1.11 数据可视化 [补充学：]](#111-数据可视化-补充学)
      * [1.11.1 折线图](#1111-折线图)
    * [1.12 面向对象](#112-面向对象)
      * [1.12.1 初识对象](#1121-初识对象)
<!-- TOC -->
------

## 1. 基础入门
### 1.1 基础语法
1. 字面量：在代码中，被写下来的固定的值。
2. 注释
- 单行注释：# 注释信息
- 多行注释： 对类和方法的解释，通常写在开头

"""
  注释信息
"""

3. 变量
> 格式：
> 
> 变量名称 = 变量的值

> print(内容1，内容2，内容3，...)

4. 数据类型
6种数据类型

| 类型             | 描述             | 说明               |
|----------------|----------------|------------------|
| 数字（number）     | 整数（int）        | 10,-10           |
|                | 浮点数（float）     | 13.14,-13.14     |
|                | 复数（complex）    | 4+3j，以j结尾表示复数    |
|                | 布尔（bool）       | true, false      |
| 字符串（string）    | 描述文本的一种数据类型    | 由任意数量的字符组成，"天气好" |
| 列表（list）       | 有序的可变序列        | 使用最频繁的数据类型       |
| 元组（tuple）      | 有序的不可变序列       |                  |
| 集合（set）        | 无序不重复集合        |                  |
| 字典（dictionary） | 无序key-value 集合 |                  |

> type(数据)：查看数据类型

5. 数据类型转换
> 格式：
> - int(x):将x转换为一个整数
> - float(x)：将x转换为一个浮点数
> - str(x)：将x转换为字符串
6. 标识符

给变量、类、方法命名的规则：
- 标识符命名只允许出现中文，英文，数字和下划线
- 数字不允许用在开头
- 大小写敏感
- 不可以使用关键字

命名规范：
- 变量命名规范： 
  1. 见名知意； 
  2. 下划线命名符：下划线分割
  3. 英语字母全小写

7. 运算符
- 算术运算符

| 运算符 | 描述  | 示例        |
|-----|-----|-----------|
| +   | 加   | 1+2       |
| -   | 减   | 2-1       |
| *   | 乘   | 1*2       |
| /   | 除   | 4/2       |
| //  | 取整除 | 9//2=4    |
| %   | 取余  | 3%2=1     |
| **  | 指数  | 10**2=100 |

- 赋值运算符

| 运算符 | 描述  | 示例               |
|-----|-----|------------------|
| =   | 赋值  | num =1           |
| +=  |     | c+=a 等效于 c = c+a |
| -=  |     | 等效于 c= c - a     |
| *=  |     | 等效于 c= c * a     |
| /=  |     | 等效于 c= c / a     |
| %=  |     | 等效于 c= c % a     |
| **= |     | 等效于 c= c **a     |
| //= |     | 等效于 c= c // a    |


8. 字符串扩展
- 1. 字符串的三种定义方式
>  1). 单引号定义法：``` name = 'amy'```
> 
>  2). 双引号定义法：``` name = "Amy"```
> 
>  3). 三引号定义法： ``` name = """Amy"""``` 


> 如果字符串本身包含单双引号如何定义？
> 
> 有两种方式：
> 
>  - 如果字符串本身包含单引号，则用双引号定义字符串，反之亦然；
>  - 用转义字符 \ 解除字符串本身所含引号的作用 ``` name = " \"amy\" "```

- 2. 字符串拼接

    1) 用 + ： print("name" + name )
    * 注意: *  字符串无法用+直接与int, float等数据类型拼接。 
  
- 3. 字符串格式化

占位拼接：
> 例子：
> 
> name = "amy"
> 
> print("my name is %s" % name)
> 
> %s : % 表示占位， s 表示将变量转换为字符串; %d %f
> 
> name = "amy"
> 
> age = 18
> 
> print("my name is %s, my age is %s" %(name, age))


- 4. 格式的精度控制

> "m.n" 来控制数据的宽度和精度
> 
> 例子：
> 
> %5d:将整数的宽度控制在5位，例如10，设置为5d,则变为：[空格][空格][空格]10
> 
> %5.2f:表示宽度为5，小数精度为2 

- 5. 字符串格式化方式2
> 格式：
> 
> f"内容{变量}"
> 
> 例子：
> ``` 
> name = 'Amy'
> 
> age = 18
>
> print(f "my name is {name}, age is {age} .")
> ```

- 6. 对表达式进行格式化
> 例子：
> print("2*1 的结果是：%.2f" %(2 * 1))
> 
> print(f"2 * 1 的结果是：{2*1}")

> 练习： 【[CODE](A-basic/Demo/Exercise1.py)】
> 
> 定义如下变量：
> - name: apple
> - stock_price: 当前股价
> - stock_code:00100
> - stock_price_daily_growth_factor:每日增长系数，1.2
> - growth_days: 增长天数，7
> 使用字符串格式化输出，小数点精度2位

9. 数据输入
变量名 = input("提示信息")
* 说明：
- 使用input语句从键盘获取输入，使用一个变量接收并存储输入的数据
- input 输入的都是 **字符串** 类型

> 练习：欢迎登陆小程序 【[CODE](A-basic/Demo/Exercise2.py)】
> 
> 定义两个变量，用以获取从键盘输入的内容，并给出如下提示信息：
> 
> 您好！xx(user_name),您是VIP(user_type)用户，欢迎登陆。

### 1.2 判断语句
#### 1.2.1 布尔类型和比较运算符
1. 布尔类型： True(1) False(0)
2. 比较运算符(>, ==, <, >=, <=, != )结果是布尔类型

#### 1.2.2 if语句的基本格式

> 格式：
> 
> if 判断条件：
> 
>      条件成立时执行的语句体

#### 1.2.3 if else 语句

> 格式：
> 
> if 判断条件：
> 
>    条件成立时执行的语句体
> 
> else:
> 
>    条件不成立时执行的语句体

#### 1.2.4 if elif else语句
> 格式：
> 
> if 条件1：
>   
>    条件1满足的执行语句体
> 
> elif 条件2：
> 
>    条件2满足的执行语句体
> 
> ....
> 
> elif 条件N：
> 
>    条件n满足的执行语句体
> else:
>   
>    所有条件都不满足的执行语句体

> 练习：猜数字 【[CODE](A-basic/Demo/Exercise3.py)】
> 
> 定义一个变量，数字类型，基于input输入猜想的数字

#### 1.2.5 判断语句的嵌套
多层if..elif..else的嵌套

> 练习： 【[CODE]()】
> 
> 公司发礼物，条件是：
> 
> 1. 必须是18-30之间的成年人
> 2. 同时入职时间大于两年，或者级别大于3

#### 1.2.6 练习
> 练习：【[CODE](A-basic/Practical/Practical1.py)】
> 
> 随机生成一个1-10的数字，通过三次判断猜出数字
> 
> 要求：
> 1） 数字随机生成
> 
> 2）通过3层嵌套进行猜并判断
> 
> 3）每次提示 猜中 猜大了或 猜小了

> 随机生成数字
> 
> import random
> 
> num = random.randint(1,10)

### 1.3 循环语句
#### 1.3.1 while循环的基本语法
>
> 格式：
> 
> while 条件语句:
>  
>     条件满足执行语句体
> 
> * 注意设置循环终止条件
> ```python
> i = 0
> while i < 100:
>    print("天气好")
>    i++

练习： 求1-100的和 【[CODE](A-basic/Demo/Exercise5.py)】


#### 1.3.2 while循环的基本案例
练习：无限猜数 【[CODE](A-basic/Demo/Exercise6.py)】

随机生成1-100之间的整数，猜数，直到猜对为止。

#### 1.3.3 while循环的嵌套案例
> -  print('hello', end = ' ') 输出不换行
> 
> - \t 制表符：作用是对齐


练习： while循环打印九九乘法表 【[CODE](A-basic/Practical/Practical2.py)】

#### 1.3.5 for循环的基本语法
1. 基础语法
格式：
> 
>   for 临时变量 in 待处理数据集：
> 循环满足条件时执行的代码

```python
name = "amy"
for x in name:
  print(x)
```
- for 循环无法定义循环条件，理论上无法构建无限循环

> 练习：【[CODE](A-basic/Practical/Practical3.py)】
> 
> 定义字符串变量name,内容为：'qazwsxedcvfredcxswqazaaassddfgrtvaadeada', for循环统计其中a的个数。

2. range语句

序列类型：内容可以一个个依次取出的一种类型。包括：
- 字符串
- 列表
- 元组

> 语法1：
> 
> range(num)
> 
> 例子： range(5)，取出数据是[0,1,2,3,4]

> 语法2：
> 
> range(num1,num2) : 从num1开始，到num2结束的数字序列，不包含num2。
> 
> 例子：
> 
> range(5,10) 取出数据为：[5,6,7,8,9]


> 语法3：
> 
> range(num1, num2,step):从num1开始，到num2结束的数字序列，不包含num2，数字之间的步长，以step为准
> 
> 例子：
> 
> range(5,10,2)取出数据为：[5,7,9]

> 练习： 统计偶数个数 【[CODE](A-basic/Practical/Practical4.py)】

> 使用range()语句，获取从1到num（num是任意数）的序列，统计偶数的个数

3. 变量作用域


#### 1.3.6 for循环的嵌套应用
练习：【[CODE](A-basic/Practical/Practical5.py)】

用for循环输出九九乘法表

#### 1.3.7 循环中断：break和continue
- break:直接结束循环
- continue: 中断本次循环，进入下一次循环

#### 1.3.8 综合案例
练习：发奖金【[CODE](A-basic/Practical/Practical6.py)】

某公司账户余额1万元，给20名员工发奖金。
- 员工编号从1到20，每人1000
- 绩效分1-10（随机生成），如低于5，无奖金
- 如奖金发完，结束发奖金

### 1.4 函数
1. 函数介绍
组织好的，*可重复使用的，* 用来实现特定功能的代码段。

* 练习：不使用len(),自己写函数统计字符串长度
```python
def  word_len(data):
  count=0
  for i in data:
    count+=1
  print(f"字符串{data}的长度是{count}")
```
2. 函数的定义
* 格式：
> def 函数名(传入参数):
>     函数体
>     return 返回值
- 说明：
  1） 参数可以省略
  2） 返回值可省略
  3）函数必须先定义再使用
3. 函数的参数
传入参数的功能是：在函数进行计算的时候，接受外部(调用时)提供的数据
注意：
- 可以不使用参数
- 可以有任意参数，逗号分开
4. 函数的返回值
结果返回给函数调用者，用变量接收
```python
def sum(a,b):
  result = a+b
  return result

sum1=sum(1,2)
```
-None类型：
如果函数没有使用return语句返回函数，函数也有返回值，返回了None这个字面量

5. 函数说明文档
* 格式： 通过多行注释对函数进行说明解释
```python
def func(x,y):
"""
函数说明
：param x:形参x的说明
：param y: 形参y的说明
：return: 返回值的数码
"""
   函数体
   return 返回值
```
6. 函数的嵌套调用：在一个函数中调用了另一个函数

7. 变量的作用域
- 局部变量：定义在函数体内部的变量，只在函数体内部生效
- 全局变量：在函数体内外都有效的变量，函数定义在函数外部
- global关键字：可以在函数内部修改全局变量的值
8. 综合练习【[CODE](A-basic/Practical/Practical7.py)】

做ATM登陆界面

-----主菜单--------

您好！欢迎登陆

查询余额【输入1】

存款【输入2】

取款【输入3】

退出【输入4】

请输入您的选择：

--------查询余额效果----------


-----查询余额--------

您好！ 您的余额是：500000元

---- 存/取款效果 -----

---存款----

您好！您存款500000成功，您卡上的余额是：60000000元

----取款-----

您好！您取款40000元，卡上余额是：64000000元

9. 函数进阶
* 函数的多返回值
  - 语法： 
    - ```
      def test_return():
          return 1,2
      x,y = test_return() 支持不同类型的数据return 
    - ```
* 函数的多种传参方式
  - 位置参数：调用函数时根据函数定义的参数位置来传递参数
  - 关键字参数：函数调用时通过"键 = 值"形式传递参数 ```def usr_info(name,age,gender)   usr_info(name = '张三'，age=20,gender='男')//可以不安顺序```
  - 不定长参数：即可变参数，用于不确定调用的时候会传递多少个参数的场景，分为两种类型：
    - 位置传递 ：args是元组类型
      - ``` def usr_info(*args):
                print(args)
            
            usr_info('TOM')--打印结果： （'TOM'，） 
            usr_info('TOM'，18) --- 打印结果：('TOM'，18)
        
      - ```
    - 关键字传递
      - ```python
        def usr_info(**kargs):
            print(kargs)
        usr_info(name='TOM',age=18,id=110) 打印值：{'name':'TOM','age':18,'id':110}

      - ```
  - 缺省参数：定义函数时，为参数提供默认值。 ```def usr_info(name,age,gender='男'）``` 注意：默认参数一定写在最后
  * 匿名函数
    - 函数作为参数传递,传入计算逻辑，而非传入数据：
    ```python
    def test_func(compute):
         result = compute(1,2)
         print(result)
    def compute(x,y):
        return x+y

     ```
    - lambda 匿名函数： lambda关键字可以定义匿名函数，只可临时使用一次
      - 定义语法：lambda 传入参数：函数体（一行代码）
      ```python
        test_func(lambda x,y:x+y)
      ```

### 1.5 数据容器

- 定义：一种可以容纳多份数据的数据类型，容纳的每一份数据称之为1个元素。即，数据容器用于批量存储
- 共5类：列表(list)，元组(tuple)，字符串(str)，集合(set)，字典(dict)
####  1.5.1 列表
* 基本语法：
  -  字面量 [元素1，元素2，...]
  -  定义变量 变量名称=[元素1，元素2,....]
  -  定义空列表 变量名称 = [] 变量名称 = list()
* 注意：
  - 列表可以一次存储多个数据，且可以为不同的数据类型，支持嵌套
* 列表的下标索引：
  - 用于取出特定位置的数据 ```列表[下标索引]```
  - 正向：从0开始
  - 反向：从-1开始，依次递减
  - 嵌套的情况：```列表[外层下标索引][内层下标索引]```
* 常用操作：
  - 查询元素：
    - 查询某元素的下标：列表.index(元素) 
  - 插入元素：
    - 列表.insert(下标，元素)，即在指定的下标位置，插入指定的元素
    - 追加元素：列表.append(元素)：指定元素追加到列表的尾部
    - 追加一批元素：列表.extend(其他数据容器)，将其他数据容器的内容取出，依次追加到列表尾部
  - 删除元素：
    - del 列表[下标]
    - 列表.pop(下标)：可以将取出的元素返回
    - 列表.remove(元素)：删除某元素在列表中的第一个匹配项
  - 清空列表
    - 列表.clear()
  - 修改元素：列表[下标]=新值
  - 统计元素个数
    - 列表.count(元素)：统计某元素在列表内的数量
    - len(列表)：统计列表中有多少元素
* 练习 【[CODE](A-basic/Practical/Practical8.py)】
  - 一个记录学生年龄的列表=[21，25，21，23，22，20]，对其进行如下操作：
    1. 定义这个列表，并用变量接收它
    2. 在列表尾部追加一个数字31
    3. 在列表尾部追击一个列表[29,33,30]
    4. 取出第一个元素
    5. 取出最后一个元素
    6. 查找元素31在列表中的下标位置
* 列表的循环遍历
  - while循环遍历列表的元素
    - 格式：
      ```python
      index = 0
      while index < len(列表)：
            元素 = 列表[index]
            对元素进行处理
            index +=1
      ```

  - for循环遍历列表的元素
    - 格式：
    ```python
    for 临时变量 in 数据容器：
        对临时变量进行处理
    ```
* 练习：取出列表中的偶数 【[CODE](A-basic/Practical/Practical9.py)】
  - 遍历列表[1，2，3，4，5，6，7，8，9，10]，取出列表中的偶数，存入一个新列表中
  - 使用while循环和for循环各操作一次

####  1.5.2 元组
- 元组可以存储多个，不同类型的元素，但：元组一旦定义完成，不可修改。
* 定义格式：
  - 字面量：（元素，元素，元素，....）
  - 元组变量：变量名称 = （元素，元素，元素，....）
  - 空元组： 变量名称=（） 变量名称 = tuple()
* 注意
  - 如果元组只有一个数据，这个数据后面要添加逗号,否则类型是string。``` t = ('hello',)```
  - 元组也可嵌套
  - 元组元素只读，不可修改，但元组内如果嵌套list,list内的元素可修改
* 相关操作
  - 查找：元组名称.index(元素)，查找某个数据的下标 
  - 统计
    - 元组名称.count(元素):统计某个数据在当前元组出现的次数
    - len(元组)：统计元组内元素的个数
* 练习 【[CODE](A-basic/Practical/Practical10.py)】
  - 定义一个元组记录学生信息（姓名，年龄，爱好）。对其进行如下操作：
    - 查询年龄所在的下标位置
    - 查询学生姓名
    - 删除学生爱好中的football
    - 增加coding 爱好到list中

####  1.5.3 字符串
* 注意： 
  - 字符串中的元素不可修改
  - 只能存储字符
* 常用操作
  for example: S = "how are you"
  - 通过下标索引取值:取'h''
    - value = S[0]
    - value = S[-11]
  - index方法：字符串.index(元素)，返回字符串中某元素所在位置
  - replace方法：字符串.replace(字符串1，字符串2)，将字符串内所有的字符串1替换为字符串2。注意，不是修改字符串，而是得到一个新的字符串
  - split方法：字符串.split(分隔符字符串)，将字符串划分为多个字符串，并存入列表对象中 例如，对S用空格进行划分 ```S.split(" ")```
  - strip方法:
    - 字符串.strip(),去前后空格
    - 字符串.strip(字符串),去前后指定字符串
  - 统计字符串中某字符出现的次数：字符串.count(元素)
  - 统计字符串长度：len(字符串)
* 练习：分割字符串 【[CODE](A-basic/Practical/Practical11.py)】
  - 给定一个字符串"how are you"
  - 统计字符串内有多少个o
  - 将空格替换为"｜"
  - 按照"｜"进行分割，得到列表


####  1.5.4 序列的切片
* 序列
  - 定义：内容连续，有序，可使用下标索引的一类数据容器，列表，元组，字符串皆是序列
* 序列的切片操作
  - 定义：切片即从一个序列中取出一个子序列
  - 语法：序列[起始下标：结束下标：步长]， 起始下标为空，视为从头开始；结束下标为空，视为到结尾，步长负数，表示反向取
  - 应用：序列[::-1],可以反转序列
* 练习：【[CODE](A-basic/Practical/Practical12.py)】
  - 反转字符串"uoy era woh"
  - 取出 are
####  1.5.5 集合
集合作用：不支持元素重复，且可无序
* 定义格式
  - 字面量：{元素1，元素2，...} 
  - 变量：变量名称={元素1，元素2，...}
  - 空集合： 变量名称=set()
* 特点:
  - 无序，不支持下标索引访问
  - 不支持重复
* 常见操作
  - 添加新元素：集合.add(元素)，将指定元素，添加到集合内
  - 移除元素：集合.remove(元素)，将指定元素，从集合内移除
  - 从集合中随机取出元素：集合.pop(),从集合中随机取出一个元素
  - 清空集合：集合.clear()
  - 取两个集合的差集：集合1.difference(集合2)，取出集合1有而集合2没有的元素，得到一个新集合，集合1和集合2不变
  - 消除2个集合的差集：集合1.difference_update(集合2)，对比集合1和集合2，在集合1内，删除和集合2相同的元素，结果：集合1被修改，集合2不变
  - 2个集合合并：集合1.union(集合2)，将集合1和集合2合并成新集合，得到新集合，集合1和集合2不变
  - 统计集合元素数量：len(集合名称)
  - 集合的遍历：集合不支持下标索引，因此不支持while循环，可以用for循环
* 练习：【[CODE](A-basic/Practical/Practical13.py)】
- 有如下列表对象：my_list = ['today','is','sunday','are','you','enjoying','the','sunshine']
- 定义一个空集合，通过for循环遍历列表，将元素添加到集合，将集合打印出来

####  1.5.6 字典
* 定义：通过key检索到value,
  - 字面量：{key:value, key:value,....}
  - 变量： my_dict = {key:value, key:value,....}
  - 空字典：my_dict = {} my_dict = dict()
* 注意：
  - key不可重复
  - key和value可以是任意数据类型，即字典可以嵌套。key不可以是字典，但value可以是嵌套的字典
  - 不支持while循环
* 相关操作
  - 取值：字典名称[key值]
  - 取嵌套字典的信息：字典名称[key][key]
  - 新增元素：字典[key]=value
  - 更新元素：字典[key]=新的value
  - 删除元素：字典.pop(key),获得指定key的value,同时指定key的数据被删除
  - 清空字典：字典.clear()
  - 获取全部key: 字典.keys(),得到字典中的全部key
  - 遍历字典：
    - 方式1：通过获取全部的key来完成遍历
      - ```for key in my_dict.keys():
               print(key)
               print(my_dict[key])
      - ```
    - 方式2：直接对字典进行for循环，每一次循环都是直接得到key
      - ```python
        for key in my_dict:
           print(key)
           print(my_dict[key])
      - ```
  - 统计字典的元素数量：len(my_dict)
* 练习：升职加薪 【[CODE](A-basic/Practical/Practical14.py)】
  - 有如下员工信息，使用字典完成数据的记录。
  - 并通过for循环对所有级别为1的员工上任1级，薪水增加1000元
  
| 姓名  | 部门  | 工资  | 级别  |
|:---:|:----:|:-----:|:-----:|
| 张三  |科技部 | 3000 |1 |
| 李四  |市场部 | 5000 | 2 |
| 王武  |市场部|7000 |3     |
| 赵六  | 科技部|4000 |1   |
| 钱七  | 市场部 | 6000 | 2  |
####  1.5.7 数据容器对比
* 数据容器分类
  - 是否支持下标索引：
    - 是：列表，元组，字符串--序列类型
    - 否：集合，字典 -- 非序列类型
  - 是否支持重复元素：
    - 是：列表，元组，字符串 -- 序列类型
    - 否：集合，字典 -- 非序列类型
  - 是否可以修改：
    - 是：列表，集合，字典
    - 否：元组，字符串
* 数据容器的通用操作
  - 遍历：都支持for循环，列表，元组，字符串支持while循环，集合，字典不支持
  - 统计元素个数： len(容器)
  - 统计容器中的最大元素：max(容器)
  - 统计容器中的最小元素：min(容器)
  - 转换
    - list(容器)：将给定容器转换为列表； 
    - str(容器)：给定容器转换为字符串 
    - tuple(容器)：转换为元组 
    - set(容器)：转换为集合
  - 排序：sorted(容器，reverse = True)
####  1.5.8 字符串大小比较
依据ASCII码表，只要A字符串有一位比B字符串对应位大，A字符串就大

###  1.6 文件操作
1. 文件的编码
文本内容通过编码技术(密码本)将内容翻译成0和1存入。常用utf-8
2. 文件的读取
   - 打开函数：open(name,mode,encoding) name:文件名；mode=r,w,a(追加) encoding:推荐utf-8 ```f= open(""D:/test.txt","r",encoding="UTF-8")```
   - 读操作：
     - read(): 文件对象.read(num), num表示从文件中读取的数据的长度，单位是字节
     - readlines(): 按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素
     - readline():一次读取一行内容
     - for循环： 
     - ```
       for line in f:
                    print(line)
       ```
   - 关闭文件：f.close()
   - with open('python.txt','r') as f:
         f.readlines()
   // 说明： 通过在with open 的语句块中对文件进行操作，可以在操作完成后自动关闭文件，避免遗忘close方法
练习：
   - 将如下内容复制到文本编辑器中，保存为 word.txt. 文件存放为任意位置，通过文件读取操作，读取此文件，统计today出现的次数。
   - today is Sunday
   - Marry go to school for celebrating something
   - she feel very good and very happy today
   - today is also a special day
   - because today is a sunny day
```python
   # 方式一
   f = open("D:/word.txt","r", encoding = "UTF-8")
   content = f.read()
   count = content.count("today")
   print(f"There are {count} 'today'")
   f.close() 
   # 方式二
   f = open("D:/word.txt","r", encoding = "UTF-8")
   count =0 
   for line in f:
     # 去除前后空格以及换行
     line = line.strip()
     words=line.split(" ")
     for word in words:
       if word == "today":
         count +=1
   print(f"There are {count} 'today'") 
   f.close()
```
3. 文件的写入
- w模式，open可以创建不存在的文件
- w模式，文件存在会清空原有内容
- f = open("D:/word.txt","w", encoding = "UTF-8")
- f.write("hello world")
- 内容刷新 ```f.flush()``` f.close()内置flush功能

4. 文件的追加
- f = open("D:/word.txt","a", encoding = "UTF-8")
- a模式。文件不存在会创建文件
- a模式，文件存在会在最后追加写入文件
5. 综合案例
- 读取文件
- 将文件写出到bill.txt.bak文件作为备份
- 将文件内标记为测试的数据行丢失
```python
# 打开文件得到文件对象,准备读取
fr = open("D:/bill.txt","r",encoding="UTF-8")
# 打开文件得到文件对象，准备写入
fw = open("D:/bill.txt.bak","w",encoding="UTF-8")
# for循环读取文件
for line in fr:
  # 清理回车换行符
  line = line.strip()
  # 用逗号分割,取第四列
  if line.split(",")[4] == "测试":
     continue  #进入下一次循环
  # 将内容写出
  fw.write(line)
    # 由于前面对内容进行了strip()的操作，所以要手动写出换行符
  fw.write("\n")
# close 2个文件对象
fr.close()
fw.close()
```
###  1.7 异常
1. 捕获异常的基本语法
   - 注意：
      - try 只放一行尝试执行的代码
      - 如果尝试执行的代码的异常类型和要捕获的异常类型不一致，则无法捕获异常
```python
try:
   可能发生错误的代码
except：
   如果出现异常执行的代码

例子：尝试以'r'模式打开文件，如文件不存在，则以'w'方式打开
try: 
  f = open('linux.txt','r')
except:
  f = open('linux.txt','w')
```
2. 捕获多个异常
当捕获多个异常时，可以把要捕获的异常类型的名字，放到except后，并使用元组的方式存储
3. 捕获所有异常
```python
try:
   f=open('D:/123.txt','r')
except Exception as e:
   print('出现异常了')
```
4. 异常else
else表示的是如果没有异常要执行的代码。
```python
try:
   print(1)
except Exception as e:
   print(e)
else:
   print('没有异常时执行的代码')
```
5. 异常的finally
finally 表示的是无论是否异常都要执行的代码,例如关闭文件
```python
try:
  f = open('test.txt','r')
except Exception as e:
  f = open('test.txt','w')
else:
  print('没有异常')
finally:
  f.close()
```
6. 异常的传递性：函数嵌套，当函数func01中发生异常且没有捕获处理这个异常的时候，异常会传递到func02，当func02没有捕获异常时，main函数会捕获这个异常
###  1.8 模块
* 模块的定义：module是一个python文件，以.py结尾，模块能定义函数，类和变量
* 模块的作用：工具包
1. 模块的导入
> [from 模块名] import [模块｜类｜变量｜*] [as 别名]
> import 模块名1，模块名2
> from 模块名 import 功能名
> from 模块名 import *: * 表示全部的意思

2. 自定义模块
* 步骤（例如）：新建一个python文件，命名为my_module.py，并定义test函数
  - '--main--'变量功能：内部测试可用，但调用时不会被执行
```python
# 新建一个python文件，命名为my_module.py
def test(a,b):
    print(a + b)
# '--main--'变量功能：内部测试可用，但调用时不会被执行
if --name-- = '--main--':
  test(1,2)
# 调用自定义的模块
import my_module
my_module.test(1,2)
```
- '__all__'变量：如果一个模块文件中有该变量，当使用'from xxx import *'导入时，只能导入这个列表中的元素
```python
# 新建一个python文件，命名为my_module.py
__all__ = ['test_A']

def test_A():
   print('test_A')
   
def test_B():
  print('test_B')
# 调用自定义的模块
from my_model import *
# 只能用testA，因为在all中
test_A()
```
###  1.9 包
1. 自定义包
* 定义：从物理上讲，包就是一个文件夹，在该文件夹下包含一个__init__.py文件，该文件夹可用于包含多个模块文件
* 作用：当模块文件越来越多时，包可以管理这些模块
* 步骤：
  - 新建包'my_package'
  - 新建包内模块
  - 模块内代码
  - 即：[New] -> [Python Package]->输入包名-> ok
2. 安装第三方包
* 常用包：
  - 科学计算：numpy
  - 数据分析：pandas
  - 大数据计算：pyspark,apache-flink
  - 图形可视化：matplotlib, pyecharts
  - 人工智能：tensorflow
* 安装方法： pip install 包名称
### 1.10 自定义工具包 【[code](my_utils)】
创建一个自定义包，名称为：my_utils
在包内提供2个模块：
- str_util.py（字符串相关工具，包含：）
  - 函数：str_reverse（s）,接受传入字符串，将字符串反转返回
  - 函数：substr（s,x,y）,按照下标x和y，对字符串进行切片
- file_util.py(文件处理相关工具，包含：)
  - 函数：print_file_info(file_name),接收传入文件的路径，打印文件的全部内容，如文件不存在则捕获异常，输出提示信息，通过finally关闭文件对象
  - 函数：append_to_file(file_name,data),接收文件路径以及传入数据，将数据追加写入文件中
构建出包后，尝试用编写的工具包
  
```python
//导入工具并使用
import my_utils.str_util
from my_utils import file_util
print(my_utils.str_util.str_reverse("今天天气好"))
print(my_utils.str_util.substr("今天天气好",1,4))

file_util.print_file_info("d:/test_append.txt")
file_util.append_to_file("d:/test_append.txt","今天不下雨")

```
### 1.11 数据可视化 [补充学：]
#### 1.11.1 折线图
json 数据格式
- 本质是带有特定格式的字符串
- 负责不同编程语言中的数据传递和交互
- 数据格式：```[{"name":"admin","age":18},{"name":"root","age":16},{"name":"zhangsan","age":20}]``` or ```{"name":"root","age":16}```
- python 数据和json 数据的相互转化
  - 导入json模块：import json
  - 准备符合json格式的python数据
  - 通过json.dumps(data)方法将python数据转化为json数据：json_str = json.dumps(data,ensure_ascii=false) ensure_ascii=false:解决中文显示问题
  - 通过json.loads(data)方法将json数据转化为python数据

pyecharts模块
- 百度开发：gallery.pyechart.org 内有各种图标
- 基础折线图
  ```python
  //导包
  from pyecharts.charts import line
  //创建对象
  line = line()
  //添加x轴坐标
  line.add_xaxis(["中国","美国","日本"])
  //添加y轴坐标
  line.add_yaxis(gdp"",[30,20,10])
  //生成图标
  line.render()
  ```
- set_global_opts方法进行全局设置
```python
line.set_global_opts(
  title_opts = titleopts("test", post_left ='center', pos_bottom = '1%'),
  legend_opts = legendopts(is_show = True),
  toolbox_opts = toolboxopts(is_show = True),
  visualmap_opts = visualmapopts(is_show = True),
  tooltip_opts = tooltipopts(is_show = True),
)
```
- 数据处理
  - 懒人工具 网站
```python
f_us = open("d://usa.txt","r",encoding = "utf-8")
us_data = f_us.read()
us_dict = json.loads(us_data)
//取key值
trend = us_dict['data'][0]['trend']
```
### 1.12 面向对象
#### 1.12.1 初识对象
使用对象组织数据，步骤如下
- 设计表格，称之为：设计类(class)
```python
class Student:
   name = None
```
- 打印生产表格，称之为：创建对象
```python
stu_1 =  Student()
stu_2 = Student()
```
- 填写表格，称之为：对象属性赋值
```python
stu_1.name = 'zs'
stu_2.name = 'ls'
```
------
