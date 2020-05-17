# split正则分割
import re

content = 'one1two2three3four6five2six8'

p = re.compile(r'\d+')
rest = p.split(content)
print(rest)

rest2 = p.split(content, 2)  # 只分割两个
print(rest2)