

class Cat(object):
	"""
	猫科动物类
	"""
	tag = '我是家猫'

	def __init__(self, name, age, sex=None):
		self.name = name
		self.__age = age
		self.sex = sex

	def set_age(self, age):
		"""
		改变猫的年龄
		:param age: int 年龄
		"""
		self.__age = age

	def show_info(self):
		"""
		显示猫的信息
		:return:
		"""
		rest = "我叫：{0}，今年{1}岁，我的性别是{2}".format(self.name, self.__age, self.sex)
		print(rest)
		return rest

	def eat(self):
		"""
		吃
		"""
		print("猫喜欢吃鱼")

	def catch(self):
		"""
		猫捉老鼠
		"""
		print("我要捉老鼠")


if __name__ == '__main__':
	"""实例化小黑"""
	cat_black = Cat('小黑', 2)

