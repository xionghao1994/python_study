# 类外面添加和获取对象属性
# 格式:
# 添加语法：对象名.属性名 = 属性值（如car.color = "红色"）
# 获取语法：直接通过对象名.属性名访问（如print(car.color)）
# 格式化输出：可用%s(字符串)、%d(整数)、%.2f(保留两位小数)等占位符

#案例:定义汽车类,在类外给汽车对象设置属性,颜色=经[色,轮胎=4,获取属性值并打印。

class Car():
    def run(self):
        print('汽车会跑')

if __name__ == '__main__':
    c1 = Car()
    c1.run()

    # 设置属性
    c1.color = 'red'
    c1.num = 4

    # 获取属性
    print(f'汽车颜色:{c1.color}')

    #7.我们再次创建1个汽车对象,请问:有上述的 color,num属性吗?
    c2 = Car()
    c2.run
    print(f'汽车颜色:{c2.color},轮胎数:{c2.num}')

