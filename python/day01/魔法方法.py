
"""
  案例：演示魔法方法 init()之无参数情况
  魔法方法解释：
  概述:
    在Python中，有一类方法是用来 对Python类的功能做 加强(扩展)的，且这一类方法都无需手动调用.
    在满足特定情况的场景下，会被白动调用，它们就称之为:魔法方法
  格式：
     __魔法方法名__()   注意：双下划线
  常用魔法方法：
     __init__()   初始化对象的属性值的，在创建对象的时候，会被自动调用.
     __str__()   用于快速打印对象的各个属性值的，在输出语句打印对象的时候会被自动调用.
     __del__()   当删除对象的时候，或者main函数执行完毕后，会自动调用
"""
#需求:给车类的所有对象，默认设置 颜色为黑色，轮胎数为3 这两个属性值。
#场景1:不使用魔法方法。

class Car:
    pass

# 场景2，使用魔法方法
class Car: # 类遵循大驼峰命名法
    def __init__(self):
        self.color = '黑色'
        self.number = 3

# main 函数一般用于测试代码
if __name__ == '__main__':
    car1 = Car()
    car2 = Car()
    print(car1)
    print(car2)

    print(f'车1的颜色是{car1.color}，轮胎数是{car1.number}')
    print(f'车2的颜色是{car2.color}，轮胎数是{car2.number}')

# 场景3，使用魔法方法，有参数情况
class Car: # 类遵循大驼峰命名法
    def __init__(self,color,number):
        self.color = color
        self.number = number

if __name__ == '__main__':
    car1 = Car('黑色',3)
    car2 = Car('蓝色',4)
    print(car1)
    print(car2)

    print(f'车1的颜色是{car1.color}，轮胎数是{car1.number}')
    print(f'车2的颜色是{car2.color}，轮胎数是{car2.number}')


# str 和 del 魔法方法

class Car: # 类遵循大驼峰命名法
    def __str__(self,color,number):
        self.color = color
        self.number = number
    
if __name__ == '__main__':
    car1 = Car('黑色',3)
    print(car1)
   # 打印输出对象的时候被调用
    print(f'车1的颜色是{car1.color}，轮胎数是{car1.number}')


    del car1  # 删除对象时，被调用, 手动释放对象的内存空间
