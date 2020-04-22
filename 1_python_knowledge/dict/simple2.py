# 字典的取值操作
employee = {'name': '汪峰', 'sex': '男',
            'hiredate': '1997-10-20', 'grade': 'A',
            'job': '销售', 'salary': '1000',
            'welfare': '100'
            }
#字典的取值
name = employee['name']
print(name)
salary = employee['salary']
print(salary)
print(employee.get('job'))
print(employee.get('dept','其他部门'))

# in 成员运算符
print('name' in employee)
print('dept' in employee)
print('dept' not in employee)

#遍历字典(两种方法）
for key in employee:
    v = employee[key]
    print(v)

for k,value in employee.items():
    print(k,value)

