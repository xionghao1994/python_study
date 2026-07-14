'''
  在软件编程中，将属性和方法书写到类的里面的操作即为封装，封装可以为属性和方法添加私有权限。
'''
# 所有属性和方法
# 私有属性: __属性名 两个下划线
# 私有方法: def __方法名():

# 访问规则：
# 只能在定义它们的类内部直接访问
# 外部访问必须通过类提供的公共接口

class teacher(object):
    # 初始化属性
    def __init__(self):
        self.kongfu = '独创煎饼果子'
        self.__money = 1000000 # 私有属性

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')

    def get_money(self):
        print(f'获得{self.__money}')

    def __make_use(self):
        print(f'我是私有方法{self.__money}')

    def makePrivate(self):
        self.__make_use()

class student(teacher):
    pass

if __name__ == '__main__':
    # 创建学生对象
    s = student()
    # 访问父类继承过来的内容
    print(s.kongfu)
    s.make_cake()

    # 尝试访问父类的钱 (报错) 
    # print(f'(徒孙) 看到了 (徒弟)的私房钱：{s.__money}')
    # 访问父类的钱 (正确)
    s.get_money()

# 私有方法: def __方法名():
    s.makePrivate()

# 什么是封装
  # 将属性和方法写到类里面的操作

# 什么是私有属性和私有方法
  # 在属性和方法前面加__

# 获取私有属性的方法
  # 定义get_xx()方法获取私有属性值
  # 定义set_xx()方法修改私有属性值

# 获取私有方法的方式
