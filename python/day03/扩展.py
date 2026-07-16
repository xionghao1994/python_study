"""
扩展1： dict属性
  概述：
    它是类的内置属性，类似于：魔法方法一样，是可以被直接调用的
  格式：
    对象名.__dict__
  作用：
    把对象的各个属性信息，封装成字典形式，属性名做键，属性值为值
"""
# 导包

from student import Student

if __name__ == '__main__':
    # 创建3个学生信息
    s1 = Student('小王', '男', 18, '12345678901', '无')
    s2 = Student('小绿', '女', 19, '12345678902', '有')
    s3 = Student('小蓝', '男', 20, '12345678903', '有')
   
    # 方式1，手动封装
    # dict1 = {'name': s1.name, 'gender': s1.gender, 'age': s1.age, 'mobile': s1.mobile, 'des': s1.des}
    # print(dict1)

    # 方式2，使用内置属性(推荐方式)
    # dict2 = s1.__dict__
    # print(dict2)

    # 列表推导式，封装3个学生信息(推荐方式)
    list = [stu.__dict__ for stu in [s1, s2, s3]]
    print(list)