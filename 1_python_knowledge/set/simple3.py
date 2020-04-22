#集合间的关系操作
s1 = {1,2,3,4,5,6}
s2 = {6,5,4,3,2,1}
s3 = {4,5,6,7}
s4 = {1,2,3,4,5,6,7,8}
print(s1 == s2)
print(s3.issubset(s4))#是否为子集
print(s4.issuperset(s3))#是否为父集
s5 = {5}
s6 = (1,3,5,7,9)
print(s5.isdisjoint(s6))#是否重复，true为不重复，false为重复


