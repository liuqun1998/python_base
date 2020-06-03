import time
import random
from multiprocessing import Process, Queue, current_process


class WriteProcess(Process):
	"""写的进程"""

	def __init__(self, q, *args, **kwargs):
		self.q = q
		super().__init__()

	def run(self):
		ls = [
			"第一行",
			"第二行了",
			"三了",
			"4行",
		]
		for line in ls:
			print("写入内容： {0} - {1}".format(line, current_process().name))
			self.q.put(line)
			time.sleep(random.randint(1, 5))


class ReadProcess(Process):
	"""读取内容数据"""
	def __init__(self, q, *args, **kwargs):
		self.q = q
		super().__init__(*args, **kwargs)

	def run(self):
		while True:
			content = self.q.get()
			print("读取的内容: {0} - {1}".format(content, current_process().name))


if __name__ == "__main__":
	# 通过queue共享数据
	q = Queue()
	# 写入
	t_write = WriteProcess(q)
	t_write.start()
	# 读取
	t_read = ReadProcess(q)
	t_read.start()
	t_write.join()
	t_write.join()

	# 终结进程
	t_read.terminate()
