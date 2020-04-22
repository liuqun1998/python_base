

class Cat(object):
	"""家猫类"""

	# 不允许添加其他属性和方法
	__slots__ = ('name', 'age')

	def __init__(self, name, age):
		"""
		构造方法
		:param name:
		:param age:
		"""
		self.name = name
		self.age = age

	@property
	def show_info(self):
		"""显示名称"""
		return '我叫{0}, 今年{1}岁'.format(self.name, self.age)

	#打印类的描述
	def __str__(self):
		return self.show_info()

if __name__ == '__main__':
	cat_block = Cat('小黑', 8)
	rest = cat_block.show_info
	print(rest)
	cat_block.color = '白色'
	print(cat_block.color)
