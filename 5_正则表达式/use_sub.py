# 正则替换sub

import re

content = 'one1two2three3four6five2six8'

# 正则替换
p = re.compile(r'\d+')
rest = p.sub('@', content)
print(rest)

# 原始的替换
rest2 = content.replace('1', '@').replace('2', '@')
print(rest2)

# 正则替换位置
s2 = 'hello world'
p2 = re.compile(r'(\w+) (\w+)')
rest_pos = p2.sub(r'\2 \1', s2)
print(rest_pos)
print('--------------')


# 替换并改变内容
def f(m):
	"""使用函数进行替换"""
	return m.group(2).upper() + ' ! ' + m.group(1)


rest_change = p2.sub(f, s2)
print(rest_change)
print('--------------')

# 使用匿名函数进行替换lambda
rest_change2 = p2.sub(lambda m: m.group(2).upper() + ' ! ' + m.group(1), s2)
print(rest_change2)
