#字典的创建
#1.使用{}
dict1 = {} #空字典
print(dict1)
dict2 = {'name':'汪峰' , 'sex':'男' ,
         'hiredate':'1997-10-20' , 'grade':'A' ,
         'job':'销售' , 'salary':'1000' ,
         'welfare':'100'
         }
print(dict2)

#2.利用dict函数创建字典
dict3 = dict(name = '汪峰',sex = '男',hiredate = '1997-10-20')
print(dict3)
dict4 = dict.fromkeys(['name','sex','hiredate','grade'] , 'N\A')
print(dict4)

