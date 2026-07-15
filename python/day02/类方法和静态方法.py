'''
  类方法和静态方法详情：
  概述：
       类方法：
           1. 第1个参数必须是当前类的对象，一般用cls当做变量名(即: class)
           2. 类方法必须通过@classmethod 来修饰
           3. 类方法是属于类的方法，能被该类下所有的对象所共享
           4、可以通过 类名 或者 对象名，的方式调用，推荐：前者
           5 类名.类方法名()
       静态方法：
           1、静态方法没有参数的硬性要求，可以1个参数都不传
           2. 静态方法使用@staticmethod装饰器
  区别：
    要不要传参，即第一个参数是写还是不写，写就是类方法，不写就是静态方法
'''
class Student(object):
    teacher_name = '航哥' # 类属性，每个对象所共享

    def __init__(self, name):
        self.name = '张三'  # 对象属性

    # 定义类方法，访问 teacher_name这个类变量
    @classmethod
    def method01(cls):
        print(cls.teacher_name) # 类，的方式，访问：类变量

    # 定义静态方法，访问 teacher_name这个类变量
    @staticmethod
    def method01():
        print(Student.teacher_name) # 类，的方式，访问：类变量
    
if __name__ == '__main__':
    # 创建学生对象
    s = Student()
    s.method01()   # 对象名，的方式 访问静态方法，可以，但是不推荐

    Student.method01() # 类名的方式，访问静态方法，推荐



