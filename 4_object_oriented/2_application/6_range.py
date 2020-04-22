# 模拟range函数


class IterRange(object):
	"""使用迭代器模拟range函数"""

	def __init__(self, start, end):
		self.start = start - 1
		self.end = end

	def __next__(self):
		self.start += 1
		if self.start >= self.end:
			raise StopIteration  # 结束迭代器
		return self.start

	def __iter__(self):  # 对自己进行迭代
		return self


if __name__ == '__main__':
	iter = IterRange(5, 10)
	print(next(iter))
