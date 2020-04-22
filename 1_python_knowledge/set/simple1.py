#集合的创建
college1 = {'哲学','经济学','法学','教育学'}
print(college1)#打印是无序的，因为存储是hash后的地址

#set（）内置函数从其他数据结构转换
college2 = {'金融学', '哲学', '经济学', '历史学', '文学'}
print(college2)

#set创建字符串集合
college3 = set('中华人民共和国')
print(college3)

#set创建空集合
college4 = set()
print(college4)
print(type(college4))
