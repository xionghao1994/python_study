"""
学生管理系统入口文件
"""
from tool_module.cpu import cpu_student_system
def main():
    print('*****欢迎来到学生管理系统*******')
    print('    1.登录学生管理系统')
    print('    2.注册学生管理系统')
    print('    3.退出学生管理系统')
    print('    4.新增学生信息')
    print('    5.查询学生信息')
    print('    6.修改学生信息')
    print('    7.删除学生信息')
    print('    8.查询所有学生信息')
    print('    9.查询单个学生信息')

# 入口文件
if __name__ == '__main__':
    main()
    cpu_student_system()