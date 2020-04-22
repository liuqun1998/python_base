#利用range遍历其他序列
c = "abcdefg"
for i in range(0,len(c)):
    letter = c[i]
    print(letter,end="")

#斐波那契数列
#1,1,2,3,5,8,13……
result = []
for i in range(0,50):
    if i == 0 or i == 1:
        result.append(1)
    else:
        result.append(result[i-2]+result[i-1])
print(result)

#判断质数
l = 776351721
is_prime = True
for i in range(2,l):
    if l % i == 0:
        is_prime = False
        print('被{}整除'.format(i))
        break
    i += 1
print(is_prime)