import time
import random
from multiprocessing import Process, Lock


class WriteProcess(Process):
	"""写入"""

	def __init__(self, files_name, number, locks, *args, **kwargs):
		self.files_name = files_name
		self.number = number
		self.locks = locks
		super().__init__(*args, **kwargs)

	def run(self) -> None:
		try:
			self.locks.acquire()  # 添加锁
			for i in range(5):
				content = '现在是： {0}  ID:{1}  ---{2}\n'.format(self.name, self.pid, self.number)
				with open(self.files_name, 'a+', encoding='utf-8') as f:
					f.write(content)
					time.sleep(random.randint(1, 5))
					print(content)
		finally:
			self.locks.release()  # 释放锁


if __name__ == "__main__":
	file_name = 'test.txt'
	lock = Lock()
	for x in range(5):
		p = WriteProcess(file_name, x, lock)
		p.start()
		p.join()