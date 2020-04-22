
def read_file():
	"""
	读取文件
	:return:
	"""
	#可以使用绝对路径
	file_name = 'test.txt'
	file_path = '/Users/liuqun/Desktop/python_base/3_document/test.txt'

	#使用普通方式打开文件
	f = open(file_name, encoding='utf-8')#utf-8:全球通用编码
	#读取文件所有内容
	#rest = f.read()
	#读取指定内容
	rest2 = f.read(10)
	#readline()：读取一行参数
	#随机读取
	f.seek(20)
	print(f.read())
	print(rest2)
	f.close()


def read_file_with():
	file_path = '/Users/liuqun/Desktop/python_base/3_document/test.txt'
	file_name = 'test.txt'
	with open(file_name, encoding='utf-8')as f:
		f.seek(20)
		print(f.read())

if __name__ == '__main__':
	read_file_with()