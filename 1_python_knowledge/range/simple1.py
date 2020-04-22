# 创建数字序列
r1 = range(10,20) #10-19的整数，左闭右开
print(type(r1))
print(r1[1:5])

#增加步长
r2 = range(10,20,2)
print(r2)
print(r2[2])

#成员运算符in
print(12 in r2)