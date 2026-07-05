"""
    核心流程处理学生管理系统
"""
from .tool import add_student

student_list = []  # 学生列表

def cpu_student_system():
    while True:

        chooseId = input('请输入学生姓名: ')

        if chooseId == '1':
            print('登录学生管理系统')
        elif chooseId == '2':
            print('注册学生管理系统')
        elif chooseId == '3':
            print('退出学生管理系统')
            break