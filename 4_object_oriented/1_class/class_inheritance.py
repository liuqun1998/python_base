

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

	def eat(self):
		super(Tiger, self).eat()
		print('老虎喜欢吃肉')

class Panda(BaseCat):
	"""
	熊猫 猫科
	"""
	tag = '熊猫'


class PetCat(BaseCat):
	"""
	家猫 猫科
	"""
	tag = '家猫'

	def eat(self):
		super(PetCat, self).eat()
		print('家猫喜欢吃猫粮')


class HuaCat(PetCat):
	"""
	中华猫
	"""
	tag = '中华猫'
	def eat(self):
		super(HuaCat, self).eat()
		print('中华猫喜欢吃粮食')


if __name__ == '__main__':
	cat = HuaCat('小黄')
	cat.eat()


