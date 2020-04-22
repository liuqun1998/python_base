

class Cat(object):
	"""家猫类"""

	def __init__(self, name, age):
		"""
		构造方法
		:param name:
		:param age:
		"""
		self.name = name
		self.__age = age

	@property
	def age(self):
		return self.__age

	@age.setter
	def age(self, value):
		if not isinstance(value, int):
			print('年龄只能是整数')
		if value < 0 or value > 100:
			print('年龄在0-100之间')
		self.__age = value


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