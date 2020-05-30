import re


# 找出其中的数字
content = 'one111two22three333four456five2six698'

p = re.compile(r'\d+')
rest = p.findall(content)
print(rest)