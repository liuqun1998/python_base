#函数使用技巧2
#1.序列传参
def calc(a,b,c):
    return (a + b) * c


l = [1,5,10]
print(calc(*l))

#2.字典传参：前面两个星号
#3.返回值包含多个数据
def get_detail_info():
    dict1 = {
        "employee":[
            {"name":"张三","salary":1800},
            {"name":"李四","salary":2000}
        ],
        "device":[
            {"id":"9873833","title":"XX笔记本"},
            {"id":"2345677","title":"XX台式机"}
        ],
        "asset":[{},{}],
        "project":[{},{}]
    }
    return dict1


print(get_detail_info())
d = get_detail_info()
salary = d.get("employee")[0].get("salary")
print(salary)