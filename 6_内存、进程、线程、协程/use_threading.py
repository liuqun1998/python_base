# 使用threading模块
import threading
import time


def loop():
	"""执行线程"""
	now_thread = threading.current_thread()
	print("now loop thread name:{0}".format(now_thread.name))
	n = 0
	while n < 5:
		print(n)
		time.sleep(1)
		n += 1


def use_thread():
	"""使用线程"""
	# 当前执行的线程名称
	now_thread = threading.current_thread()
	print("now thread name:{0}".format(now_thread.name))
	t = threading.Thread(target=loop, name="loop_thread")
	# 启动线程
	t.start()
	# 挂起线程
	t.join()


if __name__ == '__main__':
	use_thread()
