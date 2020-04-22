from datetime import datetime
import random


def gen_trans_id(date=None):
	"""
	根据所传入的时间得到一个唯一的交易流水
	：param data:日期
	：return：交易流水ID字符串
	"""
	#如果没有传入时间，使用系统默认时间
	if date is None:
		date = datetime.now()
	#日期+时间+毫秒+随机数（6位）
	return '{0}{1}'.format(date.strftime('%y%m%d%H%M%S%f'), str(random.randint(000000,999999)))