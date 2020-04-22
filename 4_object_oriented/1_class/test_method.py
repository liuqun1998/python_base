class Cat(object):
	tag = '猫科动物'

	def __init__(self, name):
		self.name = name

	@staticmethod
	def breath():
		"""呼吸"""
		print('所有猫都需要呼吸')

	@classmethod
	def show_info(cls, name):  # cls表示类，self表示实例
		"""显示信息"""
		print('猫的属性{0} '.format(cls.tag))
		return cls(name)


if __name__ == '__main__':
	# 静化方法可以直接通过类名来调用
	cat_block = Cat('小黑')
	cat_block.show_info('小黑')
