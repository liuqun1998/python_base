import os


class FileBackup(object):
	"""
	文件备份
	"""

	def __init__(self, src, dist):
		"""
		构造方法
		:param src:需要备份的文件目录
		:param dist:目录 备份后的目录
		"""
		self.src = src
		self.dist = dist

	def read_files(self):
		"""
		读取src目录下的所有文件
		"""
		ls = os.listdir(self.src)
		print(ls)
		# 循环处理每一个文件
		for i in ls:
			self.backup_file(i)
		for i in ls:
			self.backup_file2(i)

	def backup_file(self, file_name):
		"""处理备份"""
		# 判断dist目录存不存在，不存在要创建
		if not os.path.exists(self.dist):
			os.makedirs(self.dist)
			print('指定的目录不存在，创建完成')
		# 拼接完整路径
		full_src_path = os.path.join(self.src, file_name)
		full_dist_path = os.path.join(self.dist, file_name)
		# 判断是否需要备份 通过后缀名
		if os.path.isfile(full_src_path) and os.path.splitext(full_src_path)[-1].lower() == '.txt':
			# 读取文件内容
			with open(full_dist_path, 'w', encoding='utf-8')as f_dist:
				print('>>开始备份【{0}】'.format(file_name))
				with open(full_src_path, 'r', encoding='utf-8')as f_src:
					while True:
						rest = f_src.read(100)
						if not rest:
							break
						# 把读取的内容写入新的内容中
						f_dist.write(rest)
					f_dist.flush()
				print('>>备份完成【{}】'.format(file_name))

		else:
			print('文件类型不符合备份要求【{0}】'.format(file_name))

	def backup_file2(self, file_name):
		"""处理备份-优化版"""
		# 判断dist目录存不存在，不存在要创建
		if not os.path.exists(self.dist):
			os.makedirs(self.dist)
			print('指定的目录不存在，创建完成')
		# 拼接完整路径
		full_src_path = os.path.join(self.src, file_name)
		full_dist_path = os.path.join(self.dist, file_name)
		# 判断是否需要备份 通过后缀名
		if os.path.isfile(full_src_path) and os.path.splitext(full_src_path)[-1].lower() == '.txt':
			# 读取文件内容
			with open(full_dist_path, 'w', encoding='utf-8')as f_dist, \
					open(full_src_path, 'r', encoding='utf-8')as f_src:
				print('>>开始备份【{0}】'.format(file_name))
				while True:
					rest = f_src.read(100)
					if not rest:
						break
					# 把读取的内容写入新的内容中
					f_dist.write(rest)
				f_dist.flush()
				print('>>备份完成【{}】'.format(file_name))


if __name__ == '__main__':
	# 得到目录名称
	base_path = os.path.dirname(os.path.abspath(__file__))
	src_path = os.path.join(base_path, 'src')
	dist_path = os.path.join(base_path, 'dist')
	bak = FileBackup(src_path, dist_path)
	bak.read_files()
