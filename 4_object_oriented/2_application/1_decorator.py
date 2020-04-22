# 这样写太复杂
# def hello():
# 	"""简单功能模拟"""
# 	print("hello world")
#
#
# def test():
# 	print("test...")
#
#
# def hello_wrapper():
# 	"""新的函数，包裹原来的hello"""
# 	print("开始执行hello")
# 	hello()
# 	print("结束执行hello")
#
#
# if __name__ == '__main__':
#  6485a9403e
# 	hello_wrapper()


def log(func):
	"""记录函数执行的日志"""

	def wrapper():
		print("开始执行")
		func()
		print("结束执行")
	return wrapper


def log_in(func):
	"""记录函数执行的日志"""

	def wrapper():
		print("start")
		func()
		print("end")
	return wrapper


@log
@log_in
def hello():
	"""简单功能模拟"""
	print("hello world")


@log
def test():
	print("test...")


if __name__ == '__main__':
	hello()


