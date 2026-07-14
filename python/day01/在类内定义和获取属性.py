# 在类内添加和获取对象属性
# 格式:

# 类外获取：直接通过对象名.属性名访问，如c1.color
# 类内获取：通过self.属性名访问，如self.num
# 核心区别：类外使用对象名，类内使用self，但本质都是访问对象属性

class Car():
    def run(self):
        print('汽车会跑')
    def show(self):
        # 类内获取：通过self.属性名访问，如self.num
        print(f'汽车颜色:{self.color},轮胎数:{self.num}')

if __name__ == '__main__':
    c1 = Car()
    c1.run()

    # 设置属性
    c1.color = 'red'
    c1.num = 4

    # 内外获取属性
    print(f'汽车颜色:{c1.color}')

