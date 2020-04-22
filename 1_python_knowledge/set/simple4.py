#集合的增删改查
college1 = {'哲学','经济学','法学','教育学'}
for c in college1:
    print(c)

#判断元素存在
print('计算机学' in college1)

#集合不支持索引查找

#新增数据
college1.add('计算机学')
college1.add('计算机学')#重复则忽略

#update一次添加多个
college1.update(["生物学","工程学"])
print(college1)

#更新操作需要删除原有元素再添加
#remove删除不存在的元素会报错
#discard不存在这种问题，不存在直接忽略
college1.discard('生物学')
college1.discard('医学')
print(college1)