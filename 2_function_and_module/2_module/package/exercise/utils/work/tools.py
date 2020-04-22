import os.path

def get_file_type(file_name):
	"""
	根据文件名称来判断文件的类型
	：param file_name：str 文件名称
	：return：int 文件类型
	-1:未知类型
	0:图片类型
	1:word文档
	2:excel文档
	3:ppt文档
	4:py文件
	"""
	#默认文档类型未知
	result = -1
	#传进来的是文件的名称
	if not os.path.isfile(file_name):
		return result
	path_name, ext = os.path.splitext(file_name)
	# 转为小写
	ext = ext.lower()
	#图片类型
	if ext in ('.png', '.jpg', '.gif', 'bmp'):
		result =  0
	#word文档
	elif ext in ('.doc', '.docx'):
		result = 1
	#Excel文档
	elif ext in ('.xls', '.xlsx'):
		result = 2
	#ppt文档
	elif ext in ('.ppt', 'pptx'):
		result = 3
	elif ext in ('.py'):
		result = 4

	return result