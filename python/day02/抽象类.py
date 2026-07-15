'''
  介绍： 抽象类也叫抽象接口,指的是有抽象方法的类，就叫抽象类
  抽象方法： 没有具体实现的方法，只定义了方法名，没有方法体，或者用pass占位
  例如：
  def get_name(s):
    pass
  用法：抽象类一般充当父类，即：制定整个继承体系的标准
  具体体现，实现交由子类完成
'''
#需求:定义空调类(AC)，制定标准:制冷，制热，左右摆风. 两个厂商(关的，格力)根据标准，制作空调.

# 1.定义空调类(AC)，制定标准:制冷，制热，左右摆风.
class Ac(object):
    def __init__(self):
        self.model = '空调'
    def cool_wind(self):
        print('制冷')
    def heat_wind(self):
        print('制热')
    def left_right_wind(self):
        print('左右摆风')
    
# 2.美的空调
class Midea(Ac):
    def cool_wind(self):
        print('美的制冷， Ai技术')

    def heat_wind(self):
        print('美的制热， Ai技术')

    def left_right_wind(self):
        print('美的左右摆风， Ai技术')

# 3.格力空调
class Gree(Ac):
    def cool_wind(self):
        print('格力制冷，支持自动档')

    def heat_wind(self):
        print('格力制热,支持自动档')

    def left_right_wind(self):
        print('格力左右摆风，支持自动档')

if __name__ == '__main__':
    midea = Midea()
    midea.cool_wind()
    midea.heat_wind()
    midea.left_right_wind()

    gree = Gree()
    gree.cool_wind()
    gree.heat_wind()
    gree.left_right_wind()