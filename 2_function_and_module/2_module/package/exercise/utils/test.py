from datetime import datetime

from transaction.tools import gen_trans_id as trans_tools
import work
from work import tools as work_tools


def test_trans_tool():
	"""
	测试trans包下的tools模块
	"""
	print(trans_tools())
	date = datetime(2015, 10, 2, 12, 30, 45)
	print(trans_tools(date))

def test_work_tool():
	"""
	测试work模块
	"""
	path = '/2_function_and_module/2_module/package/exercise/utils/transaction/tools.py'
	rest = work_tools.get_file_type(path)
	print(rest)


if __name__ == '__main__':
	test_work_tool()