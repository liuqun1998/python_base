#字典的操作
emp1 = {'name':'Jacky','grade':'B'}
emp2 = {'name':'Lili','grade':'A'}
#setdefault为字典设置默认值，存在则忽略，否则设置
emp1.setdefault('grade','C')
emp2.setdefault('grade','C')
print(emp2)

#h获取字典的视图
#1 keys获取所有的关键词
ks = emp1.keys()
print(ks)

print(type(ks))
#2 values代表获取所有的值
vs = emp1.values()
print(vs)
print(type(vs))

#3 items获取字典键值对   (每个对是一个元组)
its = emp1.items()
print(its)
print(type(its))

emp1['hiredate'] = '1984-05-30'
print(ks)
print(vs)
print(its)

#利用字典格式化字符串
#老版本：
emp_str = "姓名:%(name)s,入职时间:%(hiredate)s,评级:%(grade)s" %emp1
print(emp_str)
#新版本：
emp_str1 = "姓名:{name},评级:{grade},入职时间:{hiredate}".format_map(emp1)
print(emp_str1)