
import  math
def func(x):
    if x >= 3:
        return x


y = filter(func, (1, 2, 3, 4))
print(y)
print(list(y))

y = filter(lambda x: (x >= 3), (1, 2, 3, 4))
print(list(y))

def division(a,b):
    return a/b


numbers= list(map(lambda x:x*2,[1,2,3,4,5]))
print(numbers)

sort=sorted(['d','3','df','5','1','b'])
print(sort)


print(math.pi)
print(math.sqrt(16))
print(math.pow(5,2))
print(math.hypot(4,3))