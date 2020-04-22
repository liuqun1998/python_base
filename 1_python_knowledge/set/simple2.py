#集合特有的作用：运算   交并差
college1 = {'哲学','经济学','法学','教育学'}
college2 = {'金融学', '哲学', '经济学', '历史学', '文学'}

#交
c3 = college1.intersection(college2)
print(c3)
print(college1)
college1.intersection_update(college2)
print(college1)

#并
college1 = {'哲学','经济学','法学','教育学'}
college2 = {'金融学', '哲学', '经济学', '历史学', '文学'}
c4 = college1.union(college2)
print(c4)

#差
college1 = {'哲学','经济学','法学','教育学'}
college2 = {'金融学', '哲学', '经济学', '历史学', '文学'}
c5 = college1.difference(college2)
print(c5)
c6 = college1.symmetric_difference(college2)#双向差集 A在B中不存在的和B在A中不存在的
print(c6)