"""
- str_util.py（字符串相关工具，包含：）
  - 函数：str_reverse（s）,接受传入字符串，将字符串反转返回
  - 函数：substr（s,x,y）,按照下标x和y，对字符串进行切片
"""

def str_reverse(s):
    """
    功能是字符串完成反转
    :param s:将被反转的字符串
    :return:反转后的字符串
    """
    return s[::-1]

def substr(s,x,y):
    """
    按照给定的下标完成给定字符串的切片
    :param s: 即将被切片的字符串
    :param x: 切片的开始下标
    :param y: 切片的结束下标
    :return: 切片完成后的字符串
    """
    return s[x:y]

if __name__ == '__main__':
    print(str_reverse("今天天气好"))
    print(substr("今天天气好",1,3))

