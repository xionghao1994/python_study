'''
   需求： 定义个地瓜类， 属性被烤的时间cookie_time和烤出来的状态cookie_status
   行为有：cook() 表示烘烤， ad_condiment() 表示添加调料料
   请用面向对象完成这个程序
'''

# 定义地瓜类
class SweetPotato():
    def __init__(self):
        self.cookie_time = 0
        self.cookie_status = '生的'

    def cook(self,cookie_time):
        if cookie_time < 3:
            self.cookie_status = '生的'
        elif cookie_time < 5:
            self.cookie_status = '半生不熟'
        elif cookie_time < 8:
            self.cookie_status = '熟了'
        else:
            self.cookie_status = '烤糊了'
        print(f'地瓜已经{cookie_time}分钟，{self.cookie_status}')
    
    def __str__(self):
        return f'地瓜已经{self.cookie_time}分钟，{self.cookie_status}'

if __name__ == '__main__':
    c1 = SweetPotato()
    c1.cook(5)

    print(c1)
