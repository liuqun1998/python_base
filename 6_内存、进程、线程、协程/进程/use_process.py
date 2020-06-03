import time
from multiprocessing import Process
import os


def do_sth(name):
	"""进程要做的事情"""
	print("进程名称{0} : {1}".format(name, os.getpid()))
	time.sleep(5)
	print("进程要做的事情")


class MyProcess(Process):

	def __init__(self, name, *args, **kwargs):
		self.my_name = name
		super().__init__(*args, **kwargs)

	def run(self):
		print("进程名称{0} : {1}".format(self.my_name, os.getpid()))
		time.sleep(15)
		print("进程要做的事情")


if __name__ == "__main__":
	# p = Process(target=do_sth, args=('my process', ))
	p = MyProcess("my process111")
	p.start()
	p.join()
