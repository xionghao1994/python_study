# 多态介绍:
# 概述:
# 多态指的是同一个事物在不同场景下表现出来的不同形态,状态
# Python中的多态指的是,同一个函数,传入不同的对象,会实现不同的结果
# 多态的前提条件:
    # 1.要有继承关系
    # 2.要有方法重写。
    # 3.要有父类引用指向子类对象
# an:Animal = Dog()
# an:Animal = Cat()
# 狗是动物,猫是动物
# 好处:
# 提高代码的可维护性.实现:1个函数,多种效果,
# 应用场景:
# 父类型充当函数形参的类型,这样可以接受其任意的子类对象,实现:传入什么(子类)对
# 就调用其对应的功能
# """ ""
# #案例:动物类案例.
#1.定义动物类,有speak()函数,表示:叫.
class Animal(object):
    def speak(self):
        pass

#2.定义狗类,继承自动物类,重写:speak()函数.
class Dog(Animal):
    def speak(self):
        print('狗汪汪汪叫')

#3.定义猫类,继承自动物类,重写:speak()函数.
class Cat(Animal):
    def speak(self):
        print('猫喵喵叫')

# 定义函数make_noise(动物类对象)，接收动物对象，实现：传入什么动物，就怎么叫
def make_noise(an: Animal): # an: Animal 要有父类的引用子类对象
    an.speak()

# 在main方法中测试
if __name__ == '__main__':
    c = Cat()
    d = Dog()
    make_noise(c)
