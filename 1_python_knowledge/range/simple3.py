#序列间的互相转换
l1 = ['a','b','c',1]
t1 = ('d','e','f')
s1 = 'abc123'
s2 = 'abc,123'
r1 = range(1,4)
#list()--转换为列表
l2 = list(t1)
print(l2)
print(list(s1))
print(s2.split(","))
print(r1)
print(list(r1))

#tuple() -- 转换为元组
print(tuple(s2.split(",")))#字符串先变成列表，再变成元组

#str函数用于将单个数据转换为字符串 join对列表进行连接
print(str(l1))
print("".join(t1))#要求所有的元素都是字符串
s3 = ""
for i in l1:
    s3 += str(i)
print(s3)

