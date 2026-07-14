'''
  格式：
     class 子类名(父类名):
        pass
     例如
      class A(B):
        pass
    叫法：
      类A: 子类，派生类，扩展类
      类B: 父类，基类，超类
    好处：
     提高代码的复用性
    细节：
      所有的类都直接或者间接继承自object类，它是所有类的父类，基类
'''
#案例:定义父类Father类，属性:性别=男，
# 行为:散步。定义子类Son，继承父类，创建对象，并调用。

class Father():
    #  定义属性
    def __init__(self):
        self.gender = '男'
    #  定义行为
    def walk(self):
        print('我在散步')

class Son(Father): # 继承关系，Son继承了Father，Father继承了object类
    pass

if __name__ == '__main__':
    son = Son()
    print(son.gender)
    son.walk()

#  单继承
'''
   概念：单继承指的是，类只能继承自另外的1个类，从中继承过来属性，和行为
'''

# 需求：
# 一个摊煎饼的老师傅，在煎饼果子界摸爬滚打多年，研发了一套精湛的摊煎饼技术，师父
# 要把这套技术传授给他的唯一的最得意的徒弟。

class Master(object):
    def __init__(self):
        self.kongfu = '古法煎饼果子技术'

    def make_cake(self):
        print(f'采用{self.kongfu}制作的煎饼果子')

class Student(Master):
    pass

if __name__ == '__main__':
    student = Student()
    # student.make_cake()
    print(f'徒弟从师傅继承过来的属性：{student.kongfu}')


# 多继承
'''
  概念：多继承指的是，类可以继承多个父类，从中继承过来属性，和行为
  例如：孩子会继承父亲和母亲的方法和属性
  基本语法：
   # 父类1Father
    class Father(object):
       pass
    # 父类2Mother
    class Mother(object):
       pass
    # 子类
    class Son(Father,Mother):
       pass
       
    结论： 
    1.Python中1个类可以继承多个父类，写法格式为: class 子类名(父类1，父类2...):
    2.如果1个类继承了多个父类，则该子类可以拥有所有父类的 属性 和 行为，（前提:父类的私有成员除外）。
    3，如果1个类维承了多个父类，且多个父类有同名的属性 和行为，优先参考第1个父类的 内容，这个是根据MRO规则实现的.
    4.MRO 全称是:Method ResoLution Order，方法解折顺序，它规定了继承关系中，属性和行为的 查找顺序，即:先找谁，后找谁.
    调用方式如下:
      类名._mro_  # 属性的方式调用
      类名.mro()  #行为(函数)的方式调用.
'''
class Master(object):
    def __init__(self):
        self.kongfu = '古法煎饼果子技术'

    def make_cake(self):
        print(f'采用{self.kongfu}制作的煎饼果子')

class School(object):
    def __init__(self):
        self.school_name = '清华大学'

class Student(Master,School):
    pass

if __name__ == '__main__':
  p = Student()
  
  # 打印继承过来的属性和方法
  print(p.kongfu)

  print(p._mro_)
  print(p.mro())


# 继承- 方法重新
'''
   概念：
       1.子类中出现和父类一模一样的属性或者行为(函数)时,称为：方法重写
   应用场景：
     当子类需要从父类沿袭一些功能，但是功能主体又有自己独有需求的时候
     就可以考虑使用方法重写了
'''

class Master(object):
    def __init__(self):
        self.kongfu = '古法煎饼果子技术'

class School(object):
    def __init__(self):
        self.kongfu = '清华大学'


# 继承-子类访问父类成员
'''
   方式1：父类名.父类方法名(self) # self 本类当前对象中引用
   方式2：super().父类方法名()

   super: 关键字介绍：
       概述：它代表本类当前对象，父类的引用
       简单理解：self 代表自己， supper 代表父类
   细节：
      1.super()只能初始化第1个父类的成员,所以super写法不适用于多继承，更适用于单继承
      2、在单继承关系中，可以把super().父类方法名(self),简写成super().父类方法名()
      3、在多继承关系中,如果想精准的初始化某个父类成员，要通过 父类名.父类方法名(self) 来实现
'''

class Master(object):
    def __init__(self):
        pass
    def make_cake_master(self):
        self.kongfu = '古法煎饼果子技术'

class School(object):
    def make_cake_school(self):
        Master.__init__(self)
        Master.make_cake_master(self)

class student(School):
    def make_cake_student(self):
        super().make_cake_school()


# 继承-多层继承
'''
  继承的传递性， 类A -> 继承 类B -> 继承 类C -> 继承 object
'''

class grandfather(object):
    pass

class father(grandfather):
    pass

class Son(father):
    pass

if __name__ == '__main__':
    son = Son()
