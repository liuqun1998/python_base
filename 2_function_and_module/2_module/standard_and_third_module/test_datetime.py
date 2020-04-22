#datetime.strftime   转换为字符串
#datetime.strptime   转换为datetime对象
#datetime.now    现在的时间

import datetime
import time

print(dir(datetime))#查看模块属性
now_time = datetime.datetime.now()#当前日期
now_day = now_time.date()
now_year = now_time.year#年  类里面还有月、日，都可以这样拿到
time.sleep(2)#休息两秒
print(time.time())#准确时间 毫秒数


