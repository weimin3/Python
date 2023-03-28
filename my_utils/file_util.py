"""
- file_util.py(文件处理相关工具，包含：)
  - 函数：print_file_info(file_name),接收传入文件的路径，打印文件的全部内容，如文件不存在则捕获异常，输出提示信息，通过finally关闭文件对象
  - 函数：append_to_file(file_name,data),接收文件路径以及传入数据，将数据追加写入文件中
"""
def print_file_info(file_name):
    f = None
    try:
        f = open(file_name, 'r', 'utf-8')
        content = f.read()
        print("文件读取如下：")
        print(content)
    except Exception as e:
        print(f"文件读取异常,原因是：{e}")
    finally:
        if f: #none 表示false
            f.close()


if __name__ == '__main__':
    # print_file_info("file_name")


def append_to_file(file_name,data):
    """
    功能：将指定数据添加到指定文件中
    :param file_name: 指定文件路径
    :param data: 指定数据
    :return: none
    """
    f = open(file_name,'a','utf-8')
    f.write(data)
    f.write("\n")
    f.close()





