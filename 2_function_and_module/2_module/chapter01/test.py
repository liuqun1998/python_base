import hello
#导入过程：当前包->内置函数->sys.path（环境变量）
#模块属性：dir 列出模块属性    __name__ 名字     __file__ 文件      __doc__ 文档注释
"""
文档注释
"""
def add(num1,num2):
    """
    这是一个方法注释
    :param num1: 说明1
    :param num2: 说明2
    :return: 返回值
    """
    return num1+num2