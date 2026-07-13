""" 
  self 关键字介绍：
  概述:
      它代表本类当前对象的引用,一般用于:函数中,即:谁调用这个函数,self就代表谁(哪个对象)
      简单记忆： 谁调用，self就代表谁
"""

# 需求1:创建汽车类Car,分别创建两个对象,观察结果.
class Car:
    #定义行为,跑.
    def run(self):
        print('汽车会跑!')

# 测试代码一般写道main方法中
# 创建对象
if __name__ == '__main__':
   c1 = Car()
   c2 = Car()

   # 调用成员
   c1.run()
   print(c1)


# 需求:定义汽车类,其有 run()和Work()两个函数,run()表示跑的功能,在work()函数中调用run()函数,并在main方法中,创建对象,调用并测试
class Car():
    def run (self):
        print('我是run函数')
    def work(self):
        print('我是work函数')
        self.run()

if __name__ == '__main__':
    c1 = Car()
    c1.work()
    # 打印：print('我是work函数') print('我是run函数')



