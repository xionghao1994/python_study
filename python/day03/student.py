# 自定义学生类，描述学生信息，属性，姓名，性别，年龄，联系方式，描述信息

class Student(object):
    # 初始化属性信息
    def __init__(self, name, gender, age, mobile, des):
        '''
         魔法方法 init, 初始化学生的信息
         : param name: 姓名
         : param gender: 性别
         : param age: 年龄
         : param mobile: 联系方式
         : param des: 描述信息
        '''
        self.name = name
        self.gender = gender
        self.age = age
        self.mobile = mobile
        self.des = des

    # 打印学生对象的各个属性信息
    def __str__(self):
        return f'姓名:{self.name},性别:{self.gender},年龄:{self.age},联系方式:{self.mobile},描述信息:{self.des}'

# 测试代码，防止在调用者中，执行当前的测试内容
if __name__ == '__main__':
    # 测试学生表
    s = Student('张三', '男', 18, '12345678901', '我是学生表')
    print(s)
