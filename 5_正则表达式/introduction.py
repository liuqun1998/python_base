# re模块:正则表达式的导入模块
import re

# 将正则表达式编译
pattern = re.compile(r'hello', re.I)  # re.I：忽略大小写
# 通过match匹配
print(dir(pattern))
rest = pattern.match('Hello world!')
print(rest)
print(dir(rest))
print('string\n{0}'.format(rest.string))  # 无空格
print('re:\n', rest.re)    # 换行有空格


