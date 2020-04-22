# 函数使用技巧
# 为参数设置默认值，只需要设置初始形参
def calc_exchange_rate(amt, source, target="USD"):
    if source == "CNY" and target == "USD":
        result = amt / 6.7516
        print("汇率计算成功")
        return result
    elif source == "CNY" and target == "EUR":
        result = amt / 7.7512
        print("汇率计算成功")
        return result


money = calc_exchange_rate(100, 'CNY')
print(money)


# 以形参形式传参
def health_check(name, age, height, weight, hr, hbp, lbp, glu):
    print("您的健康状况良好")


health_check("张三", age=32, height=178, weight=85.5, hr=70, hbp=120, lbp=80, glu=4.3)


# *代表之后所有参数需要使用关键字传参
def health_check1(name, age, height, weight, hr, hbp, *, lbp, glu):
    print("您的健康状况良好")


health_check1("张三",32,178,85.5,70,120,lbp=80,glu=4.3)