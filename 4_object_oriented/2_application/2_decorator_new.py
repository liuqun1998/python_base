
def log(name=None):
	"""记录函数执行的日志"""

	def decorator(func):

		def wrapper(*args, **kwargs):  # 魔法传参
			print("{0}start...".format(name))
			print(args)  #元组
			print(kwargs)  # 字典
			func(*args, **kwargs)
			print("{0}end...".format(name))

		return wrapper

	return decorator

@log('test')
def hello():
	"""简单功能模拟"""
	print('hello world')


@log('from add ')
def add(a,b):
	return a+b


if __name__ == "__main__":
	#  hello()
	add(5, 6)
