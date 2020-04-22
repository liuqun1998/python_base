

class BaseCat(object):
	"""
	猫科动物的基础类
	"""
	tag = '猫科动物'

	def __init__(self, name):
		self.name = name

	def eat(self):
		print('猫都要吃东西')


class Tiger(BaseCat):
	"""
	老虎类 猫科
	"""
	tag = '老虎'

	def __init__(self, name, colour):
		super().__init__(name)
		self.colour = colour

	def eat(self):
		super().eat()
		print('老虎喜欢吃肉')

	def show_info(self):
		"""展示信息"""
		print('Tiger:{0} 颜色:{1}'.format(self.name, self.colour))


if __name__ == '__main__':
	cat = Tiger('小黄')
	cat.eat()


