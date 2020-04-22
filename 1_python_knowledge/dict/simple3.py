#字典的更新操作
employee = {'name': '汪峰', 'sex': '男',
            'hiredate': '1997-10-20', 'grade': 'A',
            'job': '销售', 'salary': 1000,
            'welfare': 100
            }
print(employee)
employee['grade'] = 'B'
print(employee)
employee.update(salary = 1200,welfare = 150)
print(employee)

#字典的更新：有则改进，无则添加
employee['dept'] = '研发部'
print(employee)
employee.update(weight=80,dept='财务部')
print(employee)

#删除
employee.pop('weight')
print(employee)
kv = employee.popitem() #返回删除元素，只删除最后一个
print(kv)
print(employee)
employee.clear()#清空
print(employee)