import random
from datetime import datetime
def write_file():
	"""写入文件"""
	file_name = 'write_test.txt'
	#以写入的方式打开文件
	f = open(file_name,'w')
	f.write('hello\n')
	f.write('world')

	f.close()

def write_mult_line():
	"""写入多行"""
	file_name = 'write_test.txt'
	with open(file_name, 'w',encoding='utf-8')as f:
		l = ['第一行', '\n', '第二行',  '第三行']
		f.writelines(l)

def write_user_log():
	"""记录用户的日志"""
	#记录时间+用户的ID
	rest = '用户：{0} - 访问时间{1}'.format(random.randint(1000,9999), datetime.now())
	print(rest)
	file_name = 'write_user_log.txt'
	with open(file_name, 'a', encoding='utf-8')as f:
		f.write(rest)
		f.write('\n')

def read_and_write():
	"""先读再写"""
	file_name = 'read_and_write.txt'
	with open(file_name, 'r+', encoding='utf-8')as f:
		read_rest = f.read()
		# 如果里面没有1，就写一行aaa
		# 如果有1，就写bbb
		if '1' in read_rest:
			f.write('bbb')
		else:
			f.write('aaa')
		f.write("\n")


if __name__ == '__main__':
	write_user_log()
	write_user_log()
	write_user_log()
	write_user_log()
	read_and_write()