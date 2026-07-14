"""
   案例：减肥
    例如，小明同学当前体重是100kg。
    每当他跑步一次时，则会减少0.5kg;
    每当他大吃大喝一次时，则会增加2kg。
    请试着采用面向对象方式完成案例。
"""

class student():
    def __init__(self, name, weight): # 有参数方法
        self.name = name
        self.weight = weight
        # print(f'{self.name}的体重是{self.weight}kg')
    
    def run(self): # 无参数方法
        self.weight -= 0.5
        print(f'当前体重{self.weight}kg')

    def eat(self):
        self.weight += 2
        print(f'当前体重{self.weight}kg')
    
    def ___str__(self):
        return f'{self.name}的体重是{self.weight}kg'


if __name__ == '__main__':
    person = student('小明',100)
   
    # 执行动作
    person.run()
    person.eat()
    person.run()
    
