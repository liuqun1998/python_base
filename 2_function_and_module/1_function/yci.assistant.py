# 生活小助理
import random

phone_numbers_str = "匪警[110],火警[119],急救中心[120],道路交通事故报警[122],公安短信报警[12110],通用紧急求救[112]信产部IP/网站备案[010-66411166]"

weather_str = "北京,2019年12月1日,小雨,9℃~上海,2019年12月1日,大雪,1℃"

#生成号码
def generate_unionlotto(number):
    for j in range(0,int(number)):
        print("第%d组:" % (j + 1), end=" ")
        for i in range(0,6):
            red = random.randint(1,33)
            print(red,end=" ")
        blue = random.randint(1,16)
        print(blue)

#查找关键词
def find_phone(keyword):
    phone_list = phone_numbers_str.split(",")  # split会得到一个列表
    for p in phone_list:
        if p.find(keyword) != -1:  # 判断n是否在p中包含或部分包含
            print(p)

#天气
def get_weather(city):
    city_list = weather_str.split("~")
    weather_data = {}
    for i in range(0, len(city_list)):
        w = city_list[i].split(",")
        weather = {"name": w[0], "data": w[1], "weather": w[2], "max": w[3]}
        weather_data[weather["name"]] = weather
    if city in weather_data:
        return weather_data.get(city)#得到字典的值
    else:
        return {}


while (True):
    print("1-双色球随机选号")
    print("2-号码百事通")
    print("3-明日天气预报")
    print("0-结束程序")
    c = input("请输入功能编号：")
    if c == "1":
        n = input("您要生成几组双色球：")
        generate_unionlotto(n)
    elif c == "2":
        n = input("请输入您要查询的机构或号码")
        find_phone(n)
    elif c == "3":
        n = input("请输入城市：")
        w = get_weather(n)
        if "name" in w:
            print("{data} {name} {weather} {max}".format_map(w))
        else:
            print("未找到该城市")
    elif c == "0":
        break
    else:
        print("您的输入有误，请重新输入")
print("感谢您的使用，祝您生活愉快，再见！")
