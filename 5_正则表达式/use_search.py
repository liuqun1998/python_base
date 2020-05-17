import re

content = 'hello world!'

p = re.compile(r'world')
rest = p.search(content)
print(rest)

# match vs search
# match开头找不到就不找了，search会一直找下去
