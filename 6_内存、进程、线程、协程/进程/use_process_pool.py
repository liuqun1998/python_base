import time
import random
from multiprocessing import Pool, current_process


def run(file_name, num):
	"""
	进程执行的业务逻辑
	写入数据
	:param file_name: 文件名
	:param num: 写入的数字
	:return str: 写入的结果
	"""
	with open(file_name, 'a+', encoding='utf-8') as f:
		now_process = current_process()
		content = '{0} - {1} - {2}'.format(
			now_process.name,
			now_process.pid,
			num
		)
		f.write(content)
		f.write('\n')
		time.sleep(random.randint(1, 5))
		print(content)
	return 'ok'


if __name__ == '__main__':
	file_name = 'test_poop.txt'
	pool = Pool(2)
	rest_list = []
	for i in range(20):

		# 同步添加任务
		# rest = pool.apply(run, args=(file_name, i))
		# print('{0}---{1}'.format(i, rest))

		# 异步添加任务
		rest = pool.apply_async(run, args=(file_name, i))
		rest_list.append(rest)
		print('{0}---{1}'.format(i, rest))

	pool.close()
	pool.join()

	# 查看异步结果
	print(rest_list[0].get())
