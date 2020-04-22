from functools import wraps


def log(name=None):
	"""记录函数执行的日志"""

	def decorator(func):
		@wraps(func)  # 用来保证函数文档的原始性
		def wrapper(*args, **kwargs):  # 魔法传参
			"""装饰器内部的文档"""
			print("{0}start...".format(name))
			func(*args, **kwargs)
			print("{0}end...".format(name))

		return wrapper

	return decorator


@log('test')
def hello():
	"""简单功能模拟"""
	print('hello world')


if __name__ == '__main__':
	print('doc:{0}'.format(hello.__doc__))
	print('name:{0}'.format(hello.__name__))
	hello()
