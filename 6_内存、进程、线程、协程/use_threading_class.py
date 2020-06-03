from threading import Thread, current_thread
import time


class LoopThreading(Thread):
	"""自定义线程"""
	n = 0

	def run(self):
		while self.n < 5:
			print(self.n)
			now_thread = current_thread()
			print("now loop thread name:{0}".format(now_thread.name))
			time.sleep(1)
			self.n += 1


if __name__ == "__main__":
	t = LoopThreading(name="loop_threading_loop")
	t.start()
	t.join()