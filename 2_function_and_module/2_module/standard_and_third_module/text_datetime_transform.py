from datetime import datetime,date,time,timedelta

#自定义时间和日期
d = datetime(2020,10,30,14,5)
print(d)

d2 = date(2019,3,23)
print(d2)

t = time(9,0)
print(t)
#时间日期与字符串之间的转换
ds = '2018-10-3 13:42:09'
ds_t = datetime.strptime(ds,'%Y-%m-%d %H:%M:%S')
print(ds_t.second)
#datetime对象转换为字符串
n = datetime.now()
print(n)
n_str = n.strftime('%Y/%m/%dT%H:%M:%S')
print(n_str)

#datetime之间的加减操作
print('----------')
n = datetime.now()
n_next = n + timedelta(days=5, hours=42)
print(n_next)

#时间的减法
d1 = datetime(2018, 10, 15)
d2 = datetime(2018, 11, 12)
rest = d2 - d1
print(type(rest))
print(rest)