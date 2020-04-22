#lambda函数是一种表达式，是一种匿名函数，没有名称的函数
#filter函数：返回一个列表，包含对其执行函数结果为真的元素
#   filter使用了lambda

from functools import reduce

def use_filter(l):
	"""
	获取列表/元组中的奇数
	"""
	rest = filter(lambda n: n % 2 != 0, l)
	return rest

if __name__ == '__main__':
	l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
	rest = use_filter(l)
	print(list(rest))

#map函数：创建一个列表，其中包含对制定序列包含的项执行指定函数返回的值

def pow_number(l):
	"""
	根据给定的列表数据，计算立方
	:param l: list/type int类型的列表或者元组
	:return:原来列表中每一项的立方
	"""
	rest_list = []
	for x in l:
		rest_list.append(x ** 3)
	return rest_list


def pow_num_use_map(l):
	"""
	根据给定的列表数据，计算立方
	:param l: list/type int类型的列表或者元组
	:return:原来列表中每一项的立方
	"""
	return map(lambda n: n ** 3, l)


if __name__ == '__main__':
	l = [1, 2, 3, 4, 5, 6, 7, 9]
	print(pow_number(l))
	print(list(pow_num_use_map(l)))


#reduce

def get_sum(l):
	"""
	根据给定列表求各个数字总和
	:param l: 列表，里面是整数
	:return: 和
	"""
	rest = 0
	for i in l:
		rest += i
	return rest


def get_sum_use_py(l):
	"""
	使用python内置的函数进行求和
	:param l:列表
	:return:和
	"""
	return sum(l)

def get_sun_use_reduce(l):
	"""
	使用python内置的函数进行求和
	:param l:列表
	:return:和
	"""
	return reduce(lambda m, n: m + n, l)

if __name__ == '__main__':
	l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	print(get_sum(l))
	print(get_sum_use_py(l))
	print(get_sun_use_reduce(l))
